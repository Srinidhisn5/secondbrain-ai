"""
duplicate_hash.py

Computes a SHA256 hash for an image file and checks it against a local
record of previously-seen hashes (or a Google Sheet export as CSV).

This mirrors the logic used inside the n8n Code node ("Compute Hash + Dedup Check").
Useful for testing the dedup logic standalone against your dataset before
wiring the equivalent JS into n8n.

Usage:
    python duplicate_hash.py path/to/screenshot.png --log hashes.json
"""

import argparse
import hashlib
import json
import os
import sys


def compute_sha256(filepath: str) -> str:
    """Compute SHA256 hash of a file's binary contents."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_hash_log(log_path: str) -> dict:
    """Load existing hash -> filename record, or start fresh."""
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            return json.load(f)
    return {}


def save_hash_log(log_path: str, log: dict) -> None:
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2)


def check_and_register(filepath: str, log_path: str) -> dict:
    """
    Returns:
        {
          "hash": str,
          "is_duplicate": bool,
          "original_filename": str or None  # only set if duplicate
        }
    """
    file_hash = compute_sha256(filepath)
    log = load_hash_log(log_path)

    if file_hash in log:
        return {
            "hash": file_hash,
            "is_duplicate": True,
            "original_filename": log[file_hash],
        }

    log[file_hash] = os.path.basename(filepath)
    save_hash_log(log_path, log)
    return {"hash": file_hash, "is_duplicate": False, "original_filename": None}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check a screenshot for duplicates via SHA256.")
    parser.add_argument("filepath", help="Path to the screenshot image file")
    parser.add_argument("--log", default="hashes.json", help="Path to the hash log JSON file")
    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print(f"Error: file not found: {args.filepath}", file=sys.stderr)
        sys.exit(1)

    result = check_and_register(args.filepath, args.log)
    print(json.dumps(result, indent=2))

    if result["is_duplicate"]:
        print(f"\n⚠ DUPLICATE of: {result['original_filename']}")
    else:
        print("\n✓ New file, registered.")


# --- Equivalent n8n Code node (JavaScript) for reference ---
#
# const crypto = require('crypto');
# const binaryData = $input.item.binary.data.data; // base64 string
# const buffer = Buffer.from(binaryData, 'base64');
# const hash = crypto.createHash('sha256').update(buffer).digest('hex');
#
# // Look up `hash` against a Google Sheets column (via a prior Sheets "lookup" node)
# // rather than a local file, since n8n workflows don't have persistent local disk state.
#
# return [{ json: { ...$input.item.json, sha256_hash: hash } }];
