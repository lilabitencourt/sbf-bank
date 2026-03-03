def build_analysis(comparison):

    analysis = {}

    analysis["auc_difference"] = comparison["AUC_model3"] - comparison["AUC_model1"]
    analysis["uplift"] = comparison["Uplift"]
    analysis["statistically_significant"] = comparison["p_value"] < 0.05

    if comparison["Uplift"] > 0:
        analysis["better_in_top20"] = "Model 3"
    else:
        analysis["better_in_top20"] = "Model 1"

    return analysis
