import os

PLAN = "Days 1-2: scan every open make.fun bounty and rank by expected value: prize divided by entries divided by hours. Enter only the 5 thinnest fields; each $1 entry fee comes from the $100. Days 3-7: build one tiny paid tool (invoice-to-sheet converter) and list it at $49. Days 8-30: each morning re-rank bounties and enter 2; each afternoon pitch the tool to 20 small businesses with a live demo link, asking no payment before they see it work. Keep $20 in reserve for fees. Kill any line earning $0 for 5 days; double the one that pays. Target: 3 bounty placements plus 8 tool sales, about $500. Rule: verify payment exists before building; never spend on ads until a stranger has paid once."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
