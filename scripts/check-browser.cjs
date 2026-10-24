// Requires Playwright and Chrome. No network requests or public server.
const { chromium } = require('playwright');
const fs = require('node:fs/promises');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { createHash } = require('node:crypto');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const update = process.argv.includes('--update-previews');
function luminance(rgb) {
  const c = rgb.match(/[\d.]+/g).slice(0, 3).map(Number).map(v => {
    v /= 255; return v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4;
  });
  return .2126 * c[0] + .7152 * c[1] + .0722 * c[2];
}
(async () => {
  const browser = await chromium.launch({ headless: true, channel: 'chrome' });
  try {
    const page = await browser.newPage({ deviceScaleFactor: 1 });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('requestfailed', req => errors.push(`Failed resource: ${req.url()}`));
    await page.route(/^https?:/, route => route.abort());
    const results = [];
    for (const [width, height, name] of [[1440, 1000, 'desktop'], [390, 844, 'mobile'], [320, 700, null]]) {
      await page.setViewportSize({ width, height });
      await page.goto(pathToFileURL(path.join(root, 'docs/index.html')).href);
      await page.evaluate(() => document.fonts.ready);
      assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `Overflow at ${width}`);
      assert(await page.evaluate(() => [...document.images].every(i => i.complete && i.naturalWidth > 0)), 'Broken image');
      assert(await page.evaluate(() => [...document.fonts].every(f => f.status === 'loaded')), 'Font not loaded');
      assert(await page.evaluate(() => [...document.querySelectorAll('a[href^="#"]')].every(a => document.getElementById(a.hash.slice(1)))), 'Broken anchor');
      const pairs = await page.evaluate(() => ['body', '.button', '.eyebrow'].map(selector => {
        const s = getComputedStyle(document.querySelector(selector));
        return { selector, fg: s.color, bg: selector === '.button' ? s.backgroundColor : getComputedStyle(document.body).backgroundColor };
      }));
      for (const pair of pairs) {
        const a = luminance(pair.fg), b = luminance(pair.bg);
        pair.ratio = (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
        assert(pair.ratio >= 4.5, `${pair.selector} contrast ${pair.ratio}`);
      }
      await page.keyboard.press('Tab');
      assert(await page.locator('.skip').evaluate(el => el === document.activeElement), 'Skip link not first focus');
      assert(await page.locator('.skip').evaluate(el => el.getBoundingClientRect().top >= 0), 'Skip link not visible');
      await page.keyboard.press('Enter');
      assert(await page.locator('#main').evaluate(el => el === document.activeElement), 'Skip link did not focus main');
      const summary = page.locator('details').nth(1).locator('summary');
      await summary.focus();
      assert(await summary.evaluate(el => getComputedStyle(el).outlineStyle !== 'none'), 'No keyboard focus outline');
      await page.keyboard.press('Enter');
      assert(await page.locator('details').nth(1).evaluate(el => el.open), 'Disclosure did not open');
      await page.keyboard.press('Enter');
      assert(await page.locator('details').nth(1).evaluate(el => !el.open), 'Disclosure did not close');
      if (update && name) {
        await page.goto('about:blank');
        await page.goto(pathToFileURL(path.join(root, 'docs/index.html')).href);
        await page.evaluate(() => document.fonts.ready);
        await page.screenshot({ path: path.join(root, `docs/previews/${name}.jpg`), type: 'jpeg', quality: 90, fullPage: true });
      }
      results.push({ width, height, overflow: false, contrast: pairs });
    }
    assert.deepEqual(errors, [], 'Browser errors');
    if (update) {
      const files = ['docs/index.html', 'docs/style.css', 'docs/illustration.svg', 'docs/fonts/inter.woff2', 'docs/fonts/league.woff2', 'docs/previews/desktop.jpg', 'docs/previews/mobile.jpg', 'scripts/check-browser.cjs'];
      const sha256 = {};
      for (const file of files) sha256[file] = createHash('sha256').update(await fs.readFile(path.join(root, file))).digest('hex');
      await fs.writeFile(path.join(root, 'docs/previews/manifest.json'), JSON.stringify({ capturedAt: new Date().toISOString(), browser: browser.version(), playwright: require('playwright/package.json').version, fullPage: true, results, sha256 }, null, 2) + '\n');
    }
    console.log(JSON.stringify({ passed: true, results }, null, 2));
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });
