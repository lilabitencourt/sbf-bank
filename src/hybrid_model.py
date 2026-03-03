import statsmodels.api as sm
import numpy as np
import pandas as pd


class HybridModel:

    def __init__(self, model_new, model_old, cols_m1, cols_m3):
        self.model_new = model_new
        self.model_old = model_old
        self.cols_m1 = cols_m1
        self.cols_m3 = cols_m3

    def predict(self, X):

        results = []

        for _, row in X.iterrows():

            if row["previous"] == 0:
                X_input = pd.DataFrame([row[self.cols_m3]])
                X_input = sm.add_constant(X_input, has_constant="add")
                pred = self.model_new.predict(X_input)[0]
            else:
                X_input = pd.DataFrame([row[self.cols_m1]])
                X_input = sm.add_constant(X_input, has_constant="add")
                pred = self.model_old.predict(X_input)[0]

            results.append(pred)

        return np.array(results)