"""Offline repository checks. Run with Python 3.10+; no dependencies."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.refs, self.images = [], [], []
        self.h1 = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        self.refs.extend(attrs[k] for k in ('href', 'src') if k in attrs)
        if tag == 'img':
            self.images.append(attrs)
        self.h1 += tag == 'h1'


def anchors(path):
    text = path.read_text(encoding='utf-8')
    if path.suffix == '.html':
        return set(Page(text).ids)
    # GitHub-style heading IDs for this repository's simple Markdown headings.
    result, seen = set(), Counter()
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        result.add(slug if not seen[slug] else f'{slug}-{seen[slug]}')
        seen[slug] += 1
    return result


def preview_hash(path):
    data = path.read_bytes()
    if path.suffix in ('.html', '.css', '.svg', '.cjs'):
        data = data.replace(b'\r\n', b'\n')
    return hashlib.sha256(data).hexdigest()


def validate(root=ROOT):
    errors, count = [], 0
    for path in sorted(root.rglob('*')):
        if '.git' in path.parts or not path.is_file():
            continue
        if path.suffix not in ('.md', '.html', '.css'):
            continue
        text = path.read_text(encoding='utf-8')
        refs = []
        if path.suffix == '.md':
            text = re.sub(r'```.*?```', '', text, flags=re.S)
            refs = re.findall(r'\]\(([^)\s]+)\)', text)
        elif path.suffix == '.css':
            refs = re.findall(r'url\([\"\']?([^\)\"\']+)', text)
        else:
            page = Page(text)
            refs = page.refs
            if page.h1 != 1:
                errors.append(f'{path.name}: expected one H1')
            if len(page.ids) != len(set(page.ids)):
                errors.append(f'{path.name}: duplicate IDs')
            if any('alt' not in img for img in page.images):
                errors.append(f'{path.name}: image missing alt attribute')
        for ref in refs:
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc:
                continue
            count += 1
            target = path.parent / unquote(parsed.path) if parsed.path else path
            if not target.exists():
                errors.append(f'{path.name}: missing {ref}')
            elif parsed.fragment and target.suffix in ('.md', '.html'):
                if unquote(parsed.fragment) not in anchors(target):
                    errors.append(f'{path.name}: missing anchor {ref}')
    skill = root / 'skills/shatterstar-product-simplification/SKILL.md'
    text = skill.read_text(encoding='utf-8')
    front = re.match(r'\A---\r?\n(.*?)\r?\n---', text, re.S)
    if not front or not re.search(r'^name: shatterstar-product-simplification$', front[1], re.M) or not re.search(r'^description: \S.+$', front[1], re.M):
        errors.append('Skill name/description front matter is missing or invalid')
    manifest = root / 'docs/previews/manifest.json'
    if not manifest.exists():
        errors.append('Preview manifest missing; run browser checks with --update-previews')
    else:
        for name, expected in json.loads(manifest.read_text())['sha256'].items():
            path = root / name
            if not path.exists() or preview_hash(path) != expected:
                errors.append(f'Stale preview evidence: {name}')
    return count, errors


if __name__ == '__main__':
    count, errors = validate()
    print(f'{count} local references checked')
    for error in errors:
        print(f'FAIL: {error}')
    print('PASS' if not errors else f'{len(errors)} failure(s)')
    sys.exit(bool(errors))
