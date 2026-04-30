import numpy as np
from src.decorators import validate_dataframe, round_numeric_results


@validate_dataframe(required_columns=["калории_ккал", "белок_г", "вода_л", "шаги", "сон_часы"])
@round_numeric_results(ndigits=2)
def basic_stats(df):
    return {
        "Количество дней": len(df),
        "Средние калории": np.mean(df["калории_ккал"]),
        "Средний белок": np.mean(df["белок_г"]),
        "Средняя вода": np.mean(df["вода_л"]),
        "Средние шаги": np.mean(df["шаги"]),
        "Средний сон": np.mean(df["сон_часы"])
    }


@validate_dataframe(required_columns=["зал", "шаги", "белок_г", "энергия_балл"])
@round_numeric_results(ndigits=2)
def analyze_training_days(df):
    training_days = df[df["зал"] == "да"]
    rest_days = df[df["зал"] == "нет"]

    return {
        "Средние шаги в дни с залом": training_days["шаги"].mean(),
        "Средние шаги в дни без зала": rest_days["шаги"].mean(),
        "Средний белок в дни с залом": training_days["белок_г"].mean(),
        "Средний белок в дни без зала": rest_days["белок_г"].mean(),
        "Средняя энергия в дни с залом": training_days["энергия_балл"].mean(),
        "Средняя энергия в дни без зала": rest_days["энергия_балл"].mean()
    }


@validate_dataframe(required_columns=["сон_часы", "энергия_балл", "настроение_балл"])
@round_numeric_results(ndigits=2)
def analyze_sleep(df):
    good_sleep = df[df["сон_часы"] >= 7]
    bad_sleep = df[df["сон_часы"] < 7]

    return {
        "Энергия при сне 7+ часов": good_sleep["энергия_балл"].mean(),
        "Энергия при сне меньше 7 часов": bad_sleep["энергия_балл"].mean(),
        "Настроение при сне 7+ часов": good_sleep["настроение_балл"].mean(),
        "Настроение при сне меньше 7 часов": bad_sleep["настроение_балл"].mean()
    }