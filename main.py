import argparse

from src.table_operation import load_data, prepare_data
from src.analysis import basic_stats, analyze_training_days, analyze_sleep


DATA_PATH = "data/fitness_data.csv"


def print_result(title, result):
    print(f"\n=== {title} ===")
    for key, value in result.items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(
        description="Анализ питания, тренировок и активности"
    )

    parser.add_argument(
        "command",
        choices=["stats", "training", "sleep"],
        help="Выбери тип анализа"
    )

    args = parser.parse_args()

    df = load_data(DATA_PATH)
    df = prepare_data(df)

    if args.command == "stats":
        result = basic_stats(df)
        print_result("Базовая статистика", result)

    elif args.command == "training":
        result = analyze_training_days(df)
        print_result("Анализ тренировочных дней", result)

    elif args.command == "sleep":
        result = analyze_sleep(df)
        print_result("Анализ сна", result)


if __name__ == "__main__":
    main()