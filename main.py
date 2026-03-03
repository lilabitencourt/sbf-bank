import pandas as pd
from src.pipeline import run_pipeline
from src.config import PATH_CSV

def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


if __name__ == "__main__":

    df = pd.read_csv(PATH_CSV)

    results = run_pipeline(df)

    comparison = results["comparison"]
    analysis = results["analysis"]

    #  Avaliação
    print_section("Avaliação")

    for key, value in comparison.items():
        print(f"{key}: {value}")

    #Interpretação Estatística

    print_section("ANÁLISE ESTATÍSTICA")

    print(f"Uplift no Top 20%: {analysis['uplift']}")
    print(f"Diferença estatisticamente significativa: {analysis['statistically_significant']}")
    print(f"Melhor desempenho no Top 20%: {analysis['better_in_top20']}")

