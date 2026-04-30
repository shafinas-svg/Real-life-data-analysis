import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def prepare_data(df):
    df["дата"] = pd.to_datetime(df["дата"], errors="coerce")
    numeric_columns = [
        "длительность_тренировки_мин",

        "длительность_степ_аэробики_мин",

        "сон_часы",

        "вода_л",

        "калории_ккал",

        "белок_г",

        "шаги",

        "овощи_порции",

        "приемы_пищи_дома",

        "настроение_балл",

        "энергия_балл"

    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        return df
