import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import roc_auc_score


def evaluate_model(model, X_test, y_test, top_percent):

    X_test = sm.add_constant(X_test, has_constant="add")

    probs = model.predict(X_test)
    auc = roc_auc_score(y_test, probs)

    df_eval = pd.DataFrame({
        "y": y_test.values,
        "score": probs.values
    })

    n = int(len(df_eval) * top_percent)
    top = df_eval.sort_values("score", ascending=False).head(n)

    conversion_top = top["y"].mean()

    return {
        "probabilities": probs,
        "auc": auc,
        "conversion_top": conversion_top
    }