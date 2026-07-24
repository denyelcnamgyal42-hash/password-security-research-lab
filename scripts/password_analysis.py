from zxcvbn import zxcvbn


def calculate_entropy(password: str) -> float:
    """
    Estimate password strength using zxcvbn.

    Returns:
        log10 of the estimated number of guesses.
    """
    analysis = zxcvbn(password)
    return analysis["guesses_log10"]