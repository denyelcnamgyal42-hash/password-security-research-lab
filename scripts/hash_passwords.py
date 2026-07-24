import csv
from pathlib import Path

from scripts.hash_generator import (
    hash_md5,
    hash_sha256,
    hash_bcrypt,
    hash_argon2id,
)

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "synthetic_users.csv"

HASH_DIR = BASE_DIR / "hashes"

HASH_DIR.mkdir(exist_ok=True)


ALGORITHMS = {
    "md5": hash_md5,
    "sha256": hash_sha256,
    "bcrypt": hash_bcrypt,
    "argon2id": hash_argon2id,
}


def generate_hash_database(name, hash_function):

    output_file = HASH_DIR / f"{name}_hashes.csv"

    with open(DATA_FILE, newline="") as infile, \
         open(output_file, "w", newline="") as outfile:

        reader = csv.DictReader(infile)

        writer = csv.writer(outfile)

        writer.writerow(
            [
                "user_id",
                "username",
                "password_hash",
                "category",
                "algorithm",
            ]
        )

        for row in reader:

            hashed = hash_function(
                row["password"]
            )

            writer.writerow(
                [
                    row["user_id"],
                    row["username"],
                    hashed,
                    row["category"],
                    name,
                ]
            )

    print(f"✓ Generated {output_file.name}")


def main():

    for name, function in ALGORITHMS.items():

        generate_hash_database(
            name,
            function,
        )


if __name__ == "__main__":
    main()