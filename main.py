"""Entry for make.fun coolest-art-01: writes the bundled artwork to the output.

The artwork ships in this repository as entry.png (JPEG bytes under a .png
name; the competition's gate tells PNG from JPEG by the file's first bytes,
and the name stays entry.png either way). The program only copies that file,
so every run writes exactly the same bytes.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
MAX_BYTES = 1_048_576  # the competition's gate cap for the image file


def main() -> None:
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the {MAX_BYTES} cap")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    written = target.read_bytes()
    if written != data:
        raise SystemExit("copied file differs from the bundled artwork")
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {target} ({len(written)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
