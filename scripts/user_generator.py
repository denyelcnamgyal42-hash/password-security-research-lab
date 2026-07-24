from faker import Faker


fake = Faker()


def generate_username() -> str:
    """
    Generate a fake username.
    """

    return fake.user_name()