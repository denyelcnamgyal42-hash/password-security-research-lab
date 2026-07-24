import csv
from pathlib import Path


from scripts.constants import DEFAULT_DATASET_SIZE
from scripts.password_analysis import calculate_entropy
from scripts.password_generator import generate_password
from scripts.user_generator import generate_username



BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

OUTPUT_FILE = DATA_DIR / "synthetic_users.csv"



def generate_dataset(size: int = DEFAULT_DATASET_SIZE):

    DATA_DIR.mkdir(
        exist_ok=True
    )


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
                "length",
                "entropy",
            ]
        )


        for user_id in range(
            1,
            size + 1
        ):


            username = generate_username()


            password, category = generate_password()


            entropy = calculate_entropy(
                password
            )


            writer.writerow(
                [
                    user_id,
                    username,
                    password,
                    category,
                    len(password),
                    entropy,
                ]
            )


if __name__ == "__main__":

    generate_dataset()