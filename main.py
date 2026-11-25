#!/usr/bin/env python3
"""Print the fortune-cookie entry stored in entry.txt.

The entry file sits next to this script, so it is found no matter
which directory the program is run from.
"""

from pathlib import Path
import sys


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").strip()
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
