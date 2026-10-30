# Validation and preview maintenance

## Run the checks

From the repository root, run the dependency-free structural checks with Python 3.10 or newer:

```text
python scripts/validate.py
```

This checks local inline Markdown links and heading anchors, HTML links/anchors, unique IDs, one H1, image alt attributes, CSS asset paths, required skill front matter, and preview source/image hashes. It understands this repository's simple Markdown syntax, not every Markdown extension. External URLs are skipped; these checks do not validate research claims.

Browser checks require Node.js, Google Chrome, and Playwright 1.62.1. Install the validation dependency outside the checkout, then run in PowerShell:

```powershell
$validationTools = Join-Path $env:TEMP 'shatterstar-validation-tools'
npm install --prefix $validationTools --no-save --package-lock=false playwright@1.62.1
$env:NODE_PATH = Join-Path $validationTools 'node_modules'
node scripts/check-browser.cjs
```

The browser script opens local files and blocks HTTP/HTTPS requests. It checks 1440 x 1000, 390 x 844 and 320 x 700 viewports for horizontal page overflow, images/fonts loading, internal anchors, script/resource errors, skip-link keyboard focus and native disclosure opening/closing. It calculates the body, primary button and eyebrow contrast against their current backgrounds and requires 4.5:1. These selected pairs do not cover every rendered pixel or opacity combination.

## Refresh previews

After page, style or asset changes, use the same browser setup:

```text
node scripts/check-browser.cjs --update-previews
python scripts/validate.py
```

The first command replaces `previews/desktop.jpg` and `previews/mobile.jpg` with full-page captures and writes `previews/manifest.json` containing the UTC capture time, viewport sizes, browser/Playwright versions, measured contrast and SHA-256 hashes of page inputs, captures and the browser script. Inspect both images before accepting the update. A matching manifest establishes freshness, not visual quality. Ordinary checks do not replace previews.

## Latest local run: 2026-10-24

Structural checks and all three browser viewports passed. The lowest selected contrast ratio was 4.9237:1. Full-page desktop and mobile previews were regenerated and visually reviewed. The PowerShell installation procedure was exercised in an isolated temporary project and copied all three skill files byte-for-byte; its existing-installation guard was also checked.

No end-to-end agent discovery, skill efficacy, human usability study, full accessibility audit or public deployment was tested. External links were not comprehensively rechecked in this pass. Research wording for W3C and Nielsen was reviewed against the cited source pages. Earlier validation notes described one-off local checks; the scripts above now provide repeatable checks within their stated scope. No CI workflow is configured.

## Portable preview hashes

HTML, CSS, SVG and CJS hashes normalize CRLF to LF in both scripts. Fonts and images remain byte-exact. The 2026-10-30 migration retains the original capture date and images; it does not claim a new browser capture. Run `python scripts/test_line_endings.py --artifact-root C:/local-artifacts/shatterstar --task-id review-001` for LF/CRLF and failure-exit regression checks.

Windows regression run (2026-10-30): LF and CRLF copies returned exit code 0; genuine text and binary changes returned exit code 1. Fixtures use unique sibling directories with inherited workspace permissions to avoid restrictive temporary-directory ACLs. Evidence is retained; existing permissions are unchanged. This tests both byte formats on Windows, not native Linux. The initial browser rerun hit sandbox spawn EPERM. An authorized rerun outside the sandbox on 2026-10-30 passed at 1440 x 1000, 390 x 844 and 320 x 700: no horizontal overflow, all resource/anchor checks passed, skip-link and disclosure keyboard checks passed, and the lowest selected contrast ratio was 4.9237:1. HTTP/HTTPS requests were blocked by the script. This check did not regenerate previews or change their capture date.

## Bounded regression artifacts

The line-ending runner requires an explicit local artifact root outside the checkout and a unique task ID. Select a nonsynced location. Its default proposed budget is 20,000,000 logical bytes across that root; override with `--budget-bytes` only after reviewing the required size. It reserves metadata space before copying, refuses existing task folders, and retains a register plus exact-file cleanup review on completion/failure. No files are deleted. The full-tree fixture preserves integration coverage; no claim is made that this is a minimal fixture. Budget checks are admission/completion checks, not a filesystem quota or continuous peak monitor. Do not run concurrent writers against the same budget root.
