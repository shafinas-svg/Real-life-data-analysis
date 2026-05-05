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


@validate_dataframe(required_columns=["калории_ккал", "белок_г", "питание_вне_дома", "сладкое"])
@round_numeric_results(ndigits=2)
def analyze_nutrition(df):
    protein_goal_days = df[df["белок_г"] >= 100]
    calorie_goal_days = df[df["калории_ккал"] <= 1500]

    return {
        "Дней с белком 100 г и выше": len(protein_goal_days),
        "Дней с калориями 1500 и ниже": len(calorie_goal_days),
        "Процент дней с нормой белка": len(protein_goal_days) / len(df) * 100,
        "Процент дней в пределах калорий": len(calorie_goal_days) / len(df) * 100,
        "Средние калории": df["калории_ккал"].mean(),
        "Средний белок": df["белок_г"].mean(),
        "Дней с питанием вне дома": len(df[df["питание_вне_дома"] == "да"]),
        "Дней без сладкого": len(df[df["сладкое"] == "Нет"])
    }



@validate_dataframe(
    required_columns=[
        "зал",
        "шаги",
        "белок_г",
        "сон_часы",
        "энергия_балл",
        "настроение_балл",
        "калории_ккал",
        "питание_вне_дома"
    ]
)
def get_conclusions(df):
    training_days = df[df["зал"] == "да"]
    rest_days = df[df["зал"] == "нет"]

    good_sleep = df[df["сон_часы"] >= 7]
    bad_sleep = df[df["сон_часы"] < 7]

    high_protein_days = df[df["белок_г"] >= 100]
    calorie_goal_days = df[df["калории_ккал"] <= 1500]

    dining_out_days = df[df["питание_вне_дома"] == "да"]

    conclusions = [
        f"В дни с залом среднее количество шагов составляет {training_days['шаги'].mean():.0f}, "
        f"а в дни без зала — {rest_days['шаги'].mean():.0f}.",

        f"В тренировочные дни среднее потребление белка равно {training_days['белок_г'].mean():.1f} г, "
        f"а в дни без тренировок — {rest_days['белок_г'].mean():.1f} г.",

        f"При сне 7 часов и больше средняя энергия составляет {good_sleep['энергия_балл'].mean():.1f}, "
        f"а при сне меньше 7 часов — {bad_sleep['энергия_балл'].mean():.1f}.",

        f"При сне 7 часов и больше среднее настроение равно {good_sleep['настроение_балл'].mean():.1f}, "
        f"а при сне меньше 7 часов — {bad_sleep['настроение_балл'].mean():.1f}.",

        f"Белок 100 г и выше был достигнут в {len(high_protein_days)} днях из {len(df)}.",

        f"Калории были не выше 1500 ккал в {len(calorie_goal_days)} днях из {len(df)}.",

        f"Питание вне дома встречалось в {len(dining_out_days)} днях, чаще всего это связано с днями после физической активности."
    ]

    return conclusions