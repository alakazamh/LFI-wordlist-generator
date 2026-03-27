#!/usr/bin/env python3

import argparse
from pathlib import Path


def uniq(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def gen_prefixes(depth: int, variants: bool, backslash: bool) -> list[str]:
    prefixes = [""]

    slash_bases = ["../"]
    if backslash:
        slash_bases.append(r"..\\")

    for base in slash_bases:
        for i in range(1, depth + 1):
            prefixes.append(base * i)

            if variants:
                if base == "../":
                    prefixes.append("..//" * i)
                    prefixes.append(".././" * i)
                    prefixes.append("....//" * i)
                else:
                    prefixes.append(r"..\\.\\" * i)

    return uniq(prefixes)


def main():
    ap = argparse.ArgumentParser(description="Expand a wordlist with traversal prefixes")
    ap.add_argument("-w", "--wordlist", required=True, help="input wordlist")
    ap.add_argument("-d", "--depth", type=int, required=True, help="max traversal depth")
    ap.add_argument("-o", "--output", required=True, help="output file")
    ap.add_argument(
        "-v",
        "--variants",
        action="store_true",
        help="add variants: ..//, .././, ....//",
    )
    ap.add_argument(
        "-b",
        "--backslash",
        action="store_true",
        help=r"also generate backslash variants like ..\foo",
    )
    args = ap.parse_args()

    if args.depth < 0:
        raise SystemExit("depth must be >= 0")

    inp = Path(args.wordlist)
    if not inp.is_file():
        raise SystemExit(f"input not found: {inp}")

    prefixes = gen_prefixes(args.depth, args.variants, args.backslash)

    seen = set()
    out = []

    with inp.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            word = raw.strip()
            if not word:
                continue

            for p in prefixes:
                line = f"{p}{word}"
                if line not in seen:
                    seen.add(line)
                    out.append(line)

    Path(args.output).write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
