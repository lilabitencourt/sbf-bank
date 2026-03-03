import pandas as pd

def prepare_base_data(df):

    df = df.copy()
    df["y"] = df["y"].map({"yes":1, "no":0})

    df_encoded = pd.get_dummies(df, drop_first=True)
    df_encoded = df_encoded.astype(float)

    X = df_encoded.drop("y",axis=1)
    y = df_encoded["y"]

    return X, y
