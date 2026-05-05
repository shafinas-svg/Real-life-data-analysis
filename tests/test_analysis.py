import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.table_operation import load_data, prepare_data
from src.analysis import basic_stats, analyze_nutrition, get_conclusions


DATA_PATH = "data/fitness_data.csv"


def test_load_data_not_empty():
    df = load_data(DATA_PATH)
    assert not df.empty


def test_basic_stats_has_days_count():
    df = load_data(DATA_PATH)
    df = prepare_data(df)

    result = basic_stats(df)

    assert "Количество дней" in result
    assert result["Количество дней"] > 100


def test_analyze_nutrition_returns_dict():
    df = load_data(DATA_PATH)
    df = prepare_data(df)

    result = analyze_nutrition(df)

    assert isinstance(result, dict)
    assert "Средние калории" in result
    assert "Средний белок" in result


def test_get_conclusions_returns_list():
    df = load_data(DATA_PATH)
    df = prepare_data(df)

    result = get_conclusions(df)

    assert isinstance(result, list)
    assert len(result) >= 5