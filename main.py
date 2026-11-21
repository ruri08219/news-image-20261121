"""news-image-20261121: sum up 21 November 2026's world news in one image.

Reads the repo's ``entry.jpg`` (the single image that summarises the day's
world news) and writes it byte-for-byte to ``/output/entry.png``.

The image covers these 8 stories from 21 November 2026:

1. Trump, Xi and Putin wrap historic trilateral summit in Shenzhen.
2. Russian missiles hit Poland - NATO calls it a grave violation.
3. S&P 500 and Dow enter correction as AI stocks plunge.
4. ICJ rules Myanmar committed genocide against the Rohingya.
5. UK and EU sign deals on food trade, carbon markets and youth mobility.
6. Saudi coalition intercepts Houthi missiles over Riyadh and strikes
   Hodeidah.
7. Iran war nears ninth month; Trump says he is not rushing decisions.
8. NASA confirms Voyager 1 passes one light-day from Earth.

No network access is needed; the program is fully deterministic: the output
is always an exact copy of the bundled entry.jpg bytes.
"""

import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        raise FileNotFoundError(
            f"entry.jpg is missing from the repo directory: "
            f"expected it at {SOURCE}. Re-add the image file, then re-run."
        )
    with open(SOURCE, "rb") as f:
        data = f.read()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(f"Wrote {len(data)} bytes to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
