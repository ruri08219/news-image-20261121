"""news-image-20261121 — one image summing up 21 November 2026 world news.

The entry image (entry.jpg, kept alongside this script) is a front page that
packs the day's eight biggest stories into a single frame:

1. Trump, Xi and Putin wrap historic trilateral summit in Shenzhen.
2. Russian missiles hit Poland — NATO calls it a grave violation.
3. S&P 500 and Dow enter correction as AI stocks plunge (~3.7%).
4. ICJ rules Myanmar committed genocide against the Rohingya.
5. UK and EU sign deals on food trade, carbon markets and youth mobility.
6. Saudi coalition intercepts Houthi missiles over Riyadh and strikes Hodeidah.
7. Iran war nears ninth month; Trump says he is not rushing decisions,
   may wait until 2027.
8. NASA confirms Voyager 1 passes one light-day from Earth.

This script does one small, honest job: it copies the entry image, byte for
byte, to /output/entry.png so the competition runner can find it.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.jpg"
DESTINATION = Path("/output/entry.png")


def load_entry_image() -> bytes:
    """Read entry.jpg next to this script; fail loudly if it is absent."""
    if not SOURCE.is_file():
        raise FileNotFoundError(
            f"entry image not found next to this script: {SOURCE}"
        )
    data = SOURCE.read_bytes()
    if not data:
        raise ValueError(f"entry image is empty: {SOURCE}")
    return data


def main() -> int:
    """Copy entry.jpg to /output/entry.png and report the size."""
    data = load_entry_image()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(data)
    print(f"Wrote {len(data)} bytes to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
