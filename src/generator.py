def iter_all_days(df):
    for _, row in df.iterrows():
        yield row


def iter_training_days(df):
    for _, row in df.iterrows():
        if row["зал"] == "да":
            yield row


def iter_high_protein_days(df):
    for _, row in df.iterrows():
        if row["белок_г"] >= 100:
            yield row