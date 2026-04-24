from functools import wraps
import pandas as pd


def validate_dataframe(required_columns=None):
    def decorator(func):
        @wraps(func)
        def wrapper(df, *args, **kwargs):
            if not isinstance(df, pd.DataFrame):
                raise TypeError("Ожидался объект pandas DataFrame.")

            if df.empty:
                raise ValueError("DataFrame пустой.")

            if required_columns is not None:
                missing_columns = [col for col in required_columns if col not in df.columns]
                if missing_columns:
                    raise ValueError(
                        f"В DataFrame отсутствуют столбцы: {', '.join(missing_columns)}"
                    )

            return func(df, *args, **kwargs)
        return wrapper
    return decorator


def round_numeric_results(ndigits=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, dict):
                rounded_result = {}
                for key, value in result.items():
                    if isinstance(value, (int, float)):
                        rounded_result[key] = round(value, ndigits)
                    else:
                        rounded_result[key] = value
                return rounded_result

            return result
        return wrapper
    return decorator