import csv
from pathlib import Path
from collections import Counter
import sys

BASE_DIR = Path(__file__).resolve().parent.parent


DATA_FILE = (
    BASE_DIR /
    "data" /
    "synthetic_users.csv"
)


ALGORITHM = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "md5"
        )

CRACK_FILE = (
    BASE_DIR /
    "results" /
    f"{ALGORITHM}_show.txt"
)

OUTPUT_FILE = (
    BASE_DIR /
    "results" /
    "md5_analysis.csv"
)


def load_original_dataset():

    users = {}

    with open(DATA_FILE, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            users[row["username"]] = {
                "password": row["password"],
                "category": row["category"]
            }

    return users



def load_cracked_passwords():

    cracked = {}

    with open(CRACK_FILE) as file:

        for line in file:

            line = line.strip()

            if ":" not in line:
                continue

            username, password = line.split(
                ":",
                1
            )

            cracked[username] = password

    return cracked



def analyze():

    original = load_original_dataset()

    cracked = load_cracked_passwords()


    results = []


    for username, password in cracked.items():

        if username in original:

            results.append(
                {
                    "username": username,
                    "recovered_password": password,
                    "category":
                    original[username]["category"],
                    "algorithm": ALGORITHM.upper()
                }
            )


    with open(
        OUTPUT_FILE,
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "username",
                "recovered_password",
                "category",
                "algorithm"
            ]
        )

        writer.writeheader()

        writer.writerows(results)



    print(
        f"Recovered accounts: {len(results)}"
    )


    print("\nCategory Breakdown")

    categories = Counter(
        r["category"]
        for r in results
    )


    total_by_category = Counter(
    r["category"]
    for r in original.values()
)


    print("\nDetailed Category Analysis")

    for category in total_by_category:

        cracked_count = categories.get(
            category,
            0
     )

        total_count = total_by_category[category]

        percentage = (
            cracked_count / total_count
     ) * 100


        print(
            f"{category}: "
            f"{cracked_count}/{total_count} "
            f"({percentage:.2f}%)"
    )



if __name__ == "__main__":

    analyze()
