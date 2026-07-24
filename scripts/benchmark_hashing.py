import time

from scripts.hash_generator import (
    hash_md5,
    hash_sha256,
    hash_bcrypt,
    hash_argon2id,
)

PASSWORD = "password123"

ITERATIONS = 100


def benchmark(name, func):
    """
    Measure total and average hashing time.
    """

    start = time.perf_counter()

    for _ in range(ITERATIONS):
        func(PASSWORD)

    end = time.perf_counter()

    total = end - start
    average = total / ITERATIONS

    return {
        "Algorithm": name,
        "Iterations": ITERATIONS,
        "Total (s)": total,
        "Average (ms)": average * 1000,
    }


def main():

    results = []

    results.append(
        benchmark("MD5", hash_md5)
    )

    results.append(
        benchmark("SHA-256", hash_sha256)
    )

    results.append(
        benchmark("bcrypt", hash_bcrypt)
    )

    results.append(
        benchmark("Argon2id", hash_argon2id)
    )

    print()

    print("=" * 70)

    print(
        f'{"Algorithm":<15}'
        f'{"Iterations":<15}'
        f'{"Total(s)":<15}'
        f'{"Average(ms)"}'
    )

    print("=" * 70)

    for row in results:

        print(
            f'{row["Algorithm"]:<15}'
            f'{row["Iterations"]:<15}'
            f'{row["Total (s)"]:<15.4f}'
            f'{row["Average (ms)"]:.4f}'
        )


if __name__ == "__main__":
    main()