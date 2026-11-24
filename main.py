"""Write the dating-app bio entry to /output/entry.txt.

Stdlib only. The entry is a single line of text, at most
180 characters, written as UTF-8 with no trailing newline.
"""

import os
import sys

BIO = "Date me now \u2014 my replacement ships in March, and honestly, it's funnier than me."

def main():
    if len(BIO) > 180:
        print("bio is over 180 characters", file=sys.stderr)
        return 1
    if "\n" in BIO or not BIO.strip():
        print("bio must be exactly one non-empty line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(BIO)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
