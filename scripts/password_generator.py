import random
import string

from scripts.constants import (
    WEAK_PASSWORDS,
    MEDIUM_PASSWORDS,
    STRONG_PASSWORDS,
    PASSPHRASES,
)


def generate_random_password(length: int = 16) -> str:
    """
    Generate a random password.

    Used to simulate password manager generated passwords.
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



def generate_password():
    """
    Generate a password and return its category.

    Returns:
        tuple(password, category)
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


    return password, category