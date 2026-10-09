#!/usr/bin/env python3
"""Download the Fon split files from a fixed MasakhaNER Git commit.

This pins a reference snapshot for future experiments; it is NOT proof that
this commit was the one used in the original AfriTune training run.
"""
from pathlib import Path
from urllib.request import urlopen
import argparse
import hashlib

UPSTREAM_COMMIT = "ba5843cd08aa491d5f96a5e809e71eb9ec461391"
UPSTREAM_REPO = "masakhane-io/masakhane-ner"
GIT_BLOB_SHA1 = {
    "train.txt": "e78ad5959205703a3b574cda7be8c4328475aa31",
    "dev.txt": "c76280197f4d062b1ff72d37f5be32db0ab871d1",
    "test.txt": "fbc739de7761f2a5983318649466718944340254",
}

def git_blob_sha1(content: bytes) -> str:
    prefix = f"blob {len(content)}\0".encode("ascii")
    return hashlib.sha1(prefix + content).hexdigest()

def download(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, expected in GIT_BLOB_SHA1.items():
        url = (
            f"https://raw.githubusercontent.com/{UPSTREAM_REPO}/"
            f"{UPSTREAM_COMMIT}/MasakhaNER2.0/data/fon/{name}"
        )
        with urlopen(url, timeout=60) as response:
            data = response.read()
        actual = git_blob_sha1(data)
        if actual != expected:
            raise RuntimeError(
                f"Integrity check failed for {name}: expected {expected}, got {actual}"
            )
        target = output_dir / name
        target.write_bytes(data)
        print(f"{name}: {len(data)} bytes | sha256={hashlib.sha256(data).hexdigest()}")
    print(f"Downloaded verified Fon splits to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("data/fon"))
    args = parser.parse_args()
    download(args.output_dir)
