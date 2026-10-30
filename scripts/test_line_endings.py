"""Exercise complete validator subprocesses without modifying the checkout."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import argparse
import hashlib
import os

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--artifact-root', type=Path, required=True,
                    help='Dedicated local artifact directory outside the checkout; not a cloud-sync folder')
parser.add_argument('--task-id', required=True)
parser.add_argument('--budget-bytes', type=int, default=20_000_000)
args = parser.parse_args()
if not __import__('re').fullmatch(r'[a-zA-Z0-9_-]{1,80}', args.task_id):
    parser.error('task-id must contain 1-80 letters, digits, underscores or hyphens')
base = args.artifact_root.resolve()
if base == root or root in base.parents:
    parser.error('artifact-root must be outside the source tree')
if args.budget_bytes <= 0:
    parser.error('budget-bytes must be positive')
# Refuse links/junctions rather than following them in measurement or copying.
def files(folder):
    result = []
    if not folder.exists():
        return result
    for current, dirs, names in os.walk(folder, followlinks=False):
        for name in dirs + names:
            path = Path(current) / name
            if path.is_symlink() or getattr(path, 'is_junction', lambda: False)():
                raise RuntimeError(f'Linked artifact/source requires review: {path}')
        result.extend(Path(current) / name for name in names)
    return result

sources = [p for name in ('docs', 'skills', 'scripts') for p in files(root / name)]
sources += list(root.glob('*.md'))
baseline = sum(p.stat().st_size for p in files(base))
planned = sum(p.stat().st_size for p in sources)
# Reserve space for register/review and temporary mutation growth.
reserve = max(65536, len(sources) * 2048)
if baseline + planned + reserve > args.budget_bytes:
    parser.error(f'Budget exceeded before generation: baseline={baseline}, fixture={planned}, reserve={reserve}, limit={args.budget_bytes}')
base.mkdir(parents=True, exist_ok=True)
task = base / args.task_id
# Exclusive creation prevents overwriting user edits or accumulating reruns silently.
try:
    task.mkdir()
except FileExistsError:
    parser.error(f'Task artifacts already exist: {task}. Review them; do not generate another run automatically.')
target = task / 'fixture'
target.mkdir()
register = task / 'artifact-register.json'
review = task / 'cleanup-review.json'
results = []

def record(status):
    entries = []
    for path in files(target):
        entries.append(dict(path=str(path.resolve()), bytes=path.stat().st_size,
            purpose='Isolated LF/CRLF regression input', task=args.task_id,
            category='disposable-intermediate', regeneration='Rerun documented command against recorded source revision',
            retention='Hold until task review and explicit exact-file deletion authorization',
            sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    evidence = [dict(path=str(p), purpose=purpose, category='review-evidence', task=args.task_id,
                    retention='Preserve through owner review') for p, purpose in
                [(register, 'Artifact register and validation results'), (review, 'Exact-file cleanup proposal; not authorization')]]
    payload = dict(status=status, task=args.task_id, sourceRoot=str(root),
        sourceRevision=subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip(),
        sourceHashes={str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        command=sys.argv, baselineBytes=baseline, budgetBytes=args.budget_bytes,
        results=results, artifacts=entries, evidence=evidence)
    register.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    review.write_text(json.dumps(dict(deletionAuthorized=False, candidates=[dict(
        **entry, dependencyStatus='Isolated test copy; external references and user edits require recheck',
        unresolved=['Owner approval', 'Revalidate identity and preservation before removal']) for entry in entries],
        preservedEvidence=evidence), indent=2), encoding='utf-8')
    measured = sum(p.stat().st_size for p in files(base))
    payload.update(retainedRootBytes=measured, netLogicalGrowthBytes=measured-baseline,
                   allocatedBytes=None, measurementScope='Logical bytes under artifact root; not a peak or allocated-space measurement')
    register.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    if measured > args.budget_bytes:
        raise RuntimeError('Measured artifact budget exceeded; stop and review, no automatic cleanup')

record('started')
status = 'failed-or-interrupted'
try:
    for name in ('docs', 'skills', 'scripts'):
        shutil.copytree(root / name, target / name)
    for path in root.glob('*.md'):
        shutil.copy2(path, target / path.name)
    manifest = json.loads((target / 'docs/previews/manifest.json').read_text())

    def run(expected):
        result = subprocess.run([sys.executable, str(target / 'scripts/validate.py')], capture_output=True, text=True)
        results.append(dict(expectedExit=expected, actualExit=result.returncode, output=result.stdout[-8192:], error=result.stderr[-8192:]))
        assert result.returncode == expected, result.stdout + result.stderr
        return result.stdout

    for ending in (b'\n', b'\r\n'):
        for name in manifest['sha256']:
            path = target / name
            if path.suffix in ('.html', '.css', '.svg', '.cjs'):
                path.write_bytes(path.read_bytes().replace(b'\r\n', b'\n').replace(b'\n', ending))
        run(0)
    page = target / 'docs/index.html'
    original = page.read_bytes()
    page.write_bytes(original + b'<!-- actual content change -->')
    assert 'Stale preview evidence: docs/index.html' in run(1)
    page.write_bytes(original)
    picture = target / 'docs/previews/desktop.jpg'
    picture.write_bytes(picture.read_bytes() + b'changed')
    assert 'Stale preview evidence: docs/previews/desktop.jpg' in run(1)
    print('PASS: LF, CRLF, changed text and binary; exit codes 0/1 verified')
    print(f'Evidence retained at {target}')
    status = 'passed'
finally:
    record(status)
