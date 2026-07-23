import csv 
import random 
import string 
from pathlib import Path 

from faker import Faker 

# defining dataset location
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

OUTPUT_FILE = DATA_DIR / "synthetic_users.csv"

# password categories 

WEAK_PASSWORDS = [
    "123456",
    "password",
    "password123",
    "qwerty123",
    "admin123",
    "football2025"
]


MEDIUM_PASSWORDS = [
    "Summer2026!",
    "Bhutan@123",
    "Coffee#99",
    "Denyel2005!",
]


STRONG_PASSWORDS = [
    "Mountain-River-Sky-92",
    "CyberDefense#2026",
    "PurpleTiger!482",
]


PASSPHRASES = [
    "correct-horse-battery-staple",
    "the-moon-shines-over-bhutan",
    "coffee-mountains-rain-forest"
]

# generating random passwords 

def generate_random_password(length=16):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    return "".join(
        random.choice(characters)
        for _ in range(length)
    )

# generating user dataset 

def generate_dataset(size=1000):

    fake = Faker()

    DATA_DIR.mkdir(exist_ok=True)

    with open(
        OUTPUT_FILE,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)


        writer.writerow(
            [
                "user_id",
                "username",
                "password",
                "category",
                "length"
            ]
        )


        for user_id in range(1, size + 1):

            category = random.choice(
                [
                    "weak",
                    "medium",
                    "strong",
                    "passphrase",
                    "random"
                ]
            )


            if category == "weak":
                password = random.choice(
                    WEAK_PASSWORDS
                )

            elif category == "medium":
                password = random.choice(
                    MEDIUM_PASSWORDS
                )

            elif category == "strong":
                password = random.choice(
                    STRONG_PASSWORDS
                )

            elif category == "passphrase":
                password = random.choice(
                    PASSPHRASES
                )

            else:
                password = generate_random_password()


            writer.writerow(
                [
                    user_id,
                    fake.user_name(),
                    password,
                    category,
                    len(password)
                ]
            )


if __name__ == "__main__":
    generate_dataset()