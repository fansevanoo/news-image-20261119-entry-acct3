#!/usr/bin/env python3
"""Copy this entry's image to the grader output directory.

Stdlib only. The entry image (entry.png, 1024x1024) lives next to this
script in the repo; this script copies it byte-for-byte to
MAKEFUN_OUTPUT_DIR (default /output) and never writes to the CWD.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not os.path.isfile(SRC):
        print(f"error: entry image not found next to this script: {SRC}",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        print(f"error: size mismatch after copy: {src_size} != {dst_size}",
              file=sys.stderr)
        return 1
    if sha256_of(SRC) != sha256_of(dst):
        print("error: sha256 mismatch after copy", file=sys.stderr)
        return 1
    print(f"copied {SRC} -> {dst} ({dst_size} bytes)")
    print(f"sha256 {sha256_of(dst)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
