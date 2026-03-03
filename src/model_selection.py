def select_model(comparison):

    if (comparison["p_value"] < 0.05) and (comparison["Uplift"] > 0):
        return "model3"
    else:
        return "model1"
