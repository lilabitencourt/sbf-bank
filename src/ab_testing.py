import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

def compare_models(eval1, eval3, y_test, top_percent):

    prob1 = eval1["probabilities"]
    prob3 = eval3["probabilities"]

    df_ab = pd.DataFrame({
        "y": y_test.reset_index(drop=True),
        "score1": prob1.reset_index(drop=True),
        "score3": prob3.reset_index(drop=True)
    })

    n = int(len(df_ab) * top_percent)

    grupo_A = df_ab.sort_values("score1", ascending=False).head(n)
    grupo_B = df_ab.sort_values("score3", ascending=False).head(n)

    conv_A = grupo_A["y"].mean()
    conv_B = grupo_B["y"].mean()

    conversions = [
        grupo_A["y"].sum(),
        grupo_B["y"].sum()
    ]

    nobs = [len(grupo_A), len(grupo_B)]

    z_stat, p_value = proportions_ztest(conversions, nobs)

    uplift = conv_B - conv_A

    return {
        "AUC_model1": eval1["auc"],
        "AUC_model3": eval3["auc"],
        "ConvTop_model1": conv_A,
        "ConvTop_model3": conv_B,
        "Uplift": uplift,
        "z_stat": z_stat,
        "p_value": p_value
    }
