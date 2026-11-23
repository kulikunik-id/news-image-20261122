"""Entry program for news-image-20261122.

Copies the bundled front-page image (news.png) to the output path
the grader reads (/output/entry.png, or $MAKEFUN_OUTPUT_DIR/entry.png).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print(f"Wrote {dst}")


if __name__ == "__main__":
    main()
