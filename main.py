"""Entry program for news-image-20261122.

Copies the bundled front-page image (news.png) to the output path
the grader reads (/output/entry.png, or $MAKEFUN_OUTPUT_DIR/entry.png).
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")


MAX_BYTES = 1_048_576  # competition cap: image at most 1 MiB


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    size = os.path.getsize(SRC)
    assert size <= MAX_BYTES, f"news.png is {size} bytes, over the 1 MiB cap"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    assert _sha256(dst) == _sha256(SRC), "copied entry.png differs from news.png"
    print(f"Wrote {dst} ({size} bytes, sha256 verified)")


if __name__ == "__main__":
    main()
