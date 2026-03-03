from src.decision_analysis import build_analysis
from sklearn.model_selection import train_test_split

from src.config import (
    TOP_PERCENT,
    TEST_SIZE,
    RANDOM_STATE,
    REMOVE_MODEL1,
    REMOVE_MODEL3
)

from src.data_preparation import prepare_base_data
from src.model_training import train_model
from src.evaluation import evaluate_model
from src.ab_testing import compare_models
from src.model_selection import select_model
from src.hybrid_model import HybridModel


def drop_by_prefix(df, prefixes):
    cols_to_drop = []

    for col in df.columns:
        for prefix in prefixes:
            if col.startswith(prefix):
                cols_to_drop.append(col)

    return df.drop(columns=cols_to_drop, errors="ignore")


def run_pipeline(df):

    X, y = prepare_base_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    # Modelo 1
    X_train_m1 = X_train.drop(columns=REMOVE_MODEL1, errors="ignore")
    X_test_m1 = X_test.drop(columns=REMOVE_MODEL1, errors="ignore")

    model1 = train_model(X_train_m1, y_train)

    # Modelo 3
    prefixes_to_remove = ["month_", "contact_", "poutcome_"]

    X_train_m3 = drop_by_prefix(X_train_m1, prefixes_to_remove)
    X_test_m3 = drop_by_prefix(X_test_m1, prefixes_to_remove)

    model3 = train_model(X_train_m3, y_train)

    # Avaliação
    eval1 = evaluate_model(model1, X_test_m1, y_test, TOP_PERCENT)
    eval3 = evaluate_model(model3, X_test_m3, y_test, TOP_PERCENT)

    comparison = compare_models(eval1, eval3, y_test, TOP_PERCENT)

    analysis = build_analysis(comparison)

    #Modelo Híbrido

    hybrid = HybridModel(
        model_new=model3,
        model_old=model1,
        cols_m1=X_train_m1.columns,
        cols_m3=X_train_m3.columns
    )

    return {
        "comparison": comparison,
        "analysis": analysis,
        "hybrid_model": hybrid
    }