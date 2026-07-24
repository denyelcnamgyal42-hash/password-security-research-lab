import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

HASH_DIR = BASE_DIR / "hashes"

EXPORT_DIR = BASE_DIR / "exports"

EXPORT_DIR.mkdir(exist_ok=True)


HASH_FILES = [
    "md5",
    "sha256",
    "bcrypt",
    "argon2id",
]


def export_hash_file(algorithm):

    input_file = (
        HASH_DIR /
        f"{algorithm}_hashes.csv"
    )

    output_file = (
        EXPORT_DIR /
        f"{algorithm}_hashes.txt"
    )

    metadata_file = (
        EXPORT_DIR /
        f"{algorithm}_metadata.csv"
    )


    with open(input_file, newline="") as infile, \
         open(output_file, "w") as outfile, \
         open(metadata_file, "w", newline="") as meta:


        reader = csv.DictReader(infile)

        metadata_writer = csv.writer(meta)


        metadata_writer.writerow(
            [
                "username",
                "category",
                "algorithm"
            ]
        )


        for row in reader:

            # John/Hashcat format
            outfile.write(
                f"{row['username']}:{row['password_hash']}\n"
            )


            metadata_writer.writerow(
                [
                    row["username"],
                    row["category"],
                    row["algorithm"]
                ]
            )


    print(
        f"✓ Exported {algorithm}"
    )


def main():

    for algorithm in HASH_FILES:

        export_hash_file(
            algorithm
        )


if __name__ == "__main__":
    main()