"""One-Line Office Jokes -- make.fun entry.

Writes one original one-line office joke to ``entry.txt`` in the output
directory (``MAKEFUN_OUTPUT_DIR``, default ``/output``) and prints the
same line to stdout. Pure Python 3.13 standard library, deterministic,
no network, no randomness.
"""

import os

JOKE = "Our printer only jams on documents marked urgent, which is how I know it can read."


def main() -> None:
    # The gate requires entry.txt to be UTF-8 text of 1 to 199 characters,
    # on a single line: fail loudly rather than submit an invalid line.
    if not 1 <= len(JOKE) <= 199 or "\n" in JOKE or JOKE != JOKE.strip():
        raise ValueError("joke violates the one-line, 1-199 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
