import statsmodels.api as sm

def train_model(X_train, y_train):

    #split foi feito externamente

    X_train = sm.add_constant(X_train, has_constant="add")

    model = sm.Logit(y_train, X_train).fit(disp=0)

    return model