import bcrypt

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from scripts.hash_generator import (
    hash_md5,
    hash_sha256,
)

import hashlib


ph = PasswordHasher()


PASSWORD = "password123"


def verify_md5():

    hashed = hash_md5(PASSWORD)

    return (
        hashlib.md5(
            PASSWORD.encode()
        ).hexdigest()
        == hashed
    )


def verify_sha256():

    hashed = hash_sha256(PASSWORD)

    return (
        hashlib.sha256(
            PASSWORD.encode()
        ).hexdigest()
        == hashed
    )


def verify_bcrypt():

    hashed = bcrypt.hashpw(
        PASSWORD.encode(),
        bcrypt.gensalt()
    )

    return bcrypt.checkpw(
        PASSWORD.encode(),
        hashed
    )


def verify_argon2():

    hashed = ph.hash(PASSWORD)

    try:

        return ph.verify(
            hashed,
            PASSWORD
        )

    except VerifyMismatchError:

        return False


def main():

    print()

    print("=" * 50)

    print("Hash Verification")

    print("=" * 50)

    print(
        f"MD5      : {verify_md5()}"
    )

    print(
        f"SHA256   : {verify_sha256()}"
    )

    print(
        f"bcrypt   : {verify_bcrypt()}"
    )

    print(
        f"Argon2id : {verify_argon2()}"
    )


if __name__ == "__main__":

    main()