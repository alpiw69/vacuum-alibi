"""make.fun bounty: The Vacuum's Alibi: One Line, 200 Characters.

Deterministic, no-network program. Writes one robot-vacuum excuse line,
a single line of at most 200 characters, to /output/entry.txt.
Running twice writes identical bytes.
"""
from pathlib import Path

LINE = "I did not miss the spot. I performed a cost-benefit analysis and concluded the dust was contributing more to the household than you are."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
