"""Build a source/results bundle from the local validated Track 2 package.

No Git metadata, private data, downloaded reference cache or virtual environment
is included. This command neither publishes nor submits the bundle.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    subprocess.run([sys.executable, str(ROOT / 'submission/validate_package.py')], check=True)
    manifest = json.loads((ROOT / 'submission/validation.json').read_text())
    files = sorted(set(manifest['file_sha256']) | {'submission/validation.json'})
    output = ROOT / 'submission/ivillafuerte_track2_bundle.zip'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for relative in files:
            path = ROOT / relative
            if relative in manifest['file_sha256']:
                assert hashlib.sha256(path.read_bytes()).hexdigest() == manifest['file_sha256'][relative]
            archive.write(path, 'track2/' + relative)
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
    print(f'Created {output}: {len(files)} files; submission remains pending.')


if __name__ == '__main__':
    main()
