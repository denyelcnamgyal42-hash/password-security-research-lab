import random
import string

from scripts.constants import (
    WEAK_PASSWORDS,
    MEDIUM_PASSWORDS,
    PASSPHRASES,
)


# Word banks for generating realistic passwords

WORDS = [
    "Mountain",
    "River",
    "Forest",
    "Ocean",
    "Silver",
    "Golden",
    "Tiger",
    "Falcon",
    "Eagle",
    "Cloud",
    "Storm",
    "Shadow",
    "Dragon",
    "Phoenix",
]


PASSPHRASE_WORDS = [
    "mountain",
    "river",
    "forest",
    "cloud",
    "moon",
    "star",
    "coffee",
    "rain",
    "garden",
    "dream",
    "ocean",
    "flower",
]


def generate_random_password(length: int = 16) -> str:
    """
    Generate a random password similar to
    password-manager generated passwords.
    """

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    return "".join(
        random.choice(characters)
        for _ in range(length)
    )



def generate_strong_password() -> str:
    """
    Generate strong human-style passwords.

    Example:
    Silver-Tiger-482
    """

    word1 = random.choice(WORDS)

    word2 = random.choice(WORDS)

    number = random.randint(
        100,
        999
    )

    return f"{word1}-{word2}-{number}"



def generate_medium_password() -> str:
    """
    Generate medium strength passwords.

    Example:
    Coffee#72
    """

    word = random.choice(
        [
            "Coffee",
            "Summer",
            "Tiger",
            "Bhutan",
            "School",
            "Dragon",
        ]
    )


    symbol = random.choice(
        [
            "!",
            "@",
            "#",
            "$",
        ]
    )


    number = random.randint(
        10,
        99
    )


    return f"{word}{symbol}{number}"



def generate_passphrase() -> str:
    """
    Generate memorable passphrases.

    Example:
    mountain-river-cloud-star
    """

    words = random.sample(
        PASSPHRASE_WORDS,
        4
    )


    return "-".join(words)



def generate_password():
    """
    Generate password and category.
    """

    category = random.choice(
        [
            "weak",
            "medium",
            "strong",
            "passphrase",
            "random",
        ]
    )


    if category == "weak":

        password = random.choice(
            WEAK_PASSWORDS
        )


    elif category == "medium":

        password = generate_medium_password()


    elif category == "strong":

        password = generate_strong_password()


    elif category == "passphrase":

        password = generate_passphrase()


    else:

        password = generate_random_password()


    return password, category