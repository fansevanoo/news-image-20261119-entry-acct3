#!/usr/bin/env python3
"""Copy entry.png to the grader output directory.

The entry image is pre-rendered (see compose.py in the work directory);
this program only places it where the grader expects it.
"""
import os
import shutil


def main():
    """Copy entry.png next to this file into MAKEFUN_OUTPUT_DIR."""
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    return dest


if __name__ == "__main__":
    main()
