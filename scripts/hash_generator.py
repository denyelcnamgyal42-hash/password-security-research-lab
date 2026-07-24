import hashlib

import bcrypt

from argon2 import PasswordHasher


ph = PasswordHasher()


def hash_md5(password: str) -> str:
    """Generate an MD5 hash."""

    return hashlib.md5(
        password.encode("utf-8")
    ).hexdigest()


def hash_sha256(password: str) -> str:
    """Generate a SHA-256 hash."""

    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def hash_bcrypt(password: str) -> str:
    """Generate a bcrypt hash with a random salt."""

    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def hash_argon2id(password: str) -> str:
    """Generate an Argon2id hash."""

    return ph.hash(password)