#!/usr/bin/env python3
"""Write the cutest-dog picture to /output/entry.png.

The image ships beside this file as entry.png (JPEG magic, name entry.png).
Deterministic copy, standard library only, no network.
"""
from __future__ import annotations
import os
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"

def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.png").write_bytes(ENTRY.read_bytes())

if __name__ == "__main__":
    main()
