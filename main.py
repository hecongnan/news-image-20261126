#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261126.

Copies the entry image (entry.png, held in this repository) to the
output directory named by MAKEFUN_OUTPUT_DIR (default "out"), always
as entry.png. Standard library only, no network, deterministic: the
bytes written are exactly the bytes of the image in this repository,
so two runs produce byte-identical output.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"error: {source} not found", file=sys.stderr)
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    # copyfile copies bytes exactly; no timestamps or metadata leak in.
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
