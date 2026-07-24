import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

RESULT_FILE = (
    BASE_DIR /
    "results" /
    "cracking_results.csv"
)

OUTPUT_DIR = (
    BASE_DIR /
    "results" /
    "reports"
)


def main():

    OUTPUT_DIR.mkdir(
        exist_ok=True
    )

    df = pd.read_csv(
        RESULT_FILE
    )


    print(df)


    # Recovery chart

    plt.figure(figsize=(8,5))

    plt.bar(
        df["algorithm"],
        df["recovered"]
    )

    plt.xlabel(
        "Hash Algorithm"
    )

    plt.ylabel(
        "Recovered Passwords"
    )

    plt.title(
        "Password Recovery Comparison"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()


    plt.savefig(
        OUTPUT_DIR /
        "recovery_comparison.png"
    )


    # Success rate chart

    plt.figure(figsize=(8,5))

    plt.bar(
        df["algorithm"],
        df["success_rate"]
    )

    plt.xlabel(
        "Hash Algorithm"
    )

    plt.ylabel(
        "Recovery Percentage"
    )

    plt.title(
        "Password Cracking Success Rate"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()


    plt.savefig(
        OUTPUT_DIR /
        "success_rate.png"
    )


    print(
        "Reports generated!"
    )


if __name__ == "__main__":
    main()
