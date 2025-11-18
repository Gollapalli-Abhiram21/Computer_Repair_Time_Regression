import pandas as pd
from sklearn.linear_model import LinearRegression

def create_manual_models(df):
    df['min_model0'] = df['Minutes'].mean()
    df['min_model1'] = 10 + 12 * df['Units']
    df['min_model2'] = 6 + 18 * df['Units']
    return df

def best_fit_linear_regression(df):
    x = df['Units']
    y = df['Minutes']
    n = len(df)
    xmean = x.mean()
    ymean = y.mean()
    numerator = (x * y).sum() - n * xmean * ymean
    denominator = (x ** 2).sum() - n * (xmean ** 2)
    m = numerator / denominator
    c = ymean - (m * xmean)
    df['min_best_fit_model'] = c + m * x
    return c, m, df

def sklearn_linear_regression(df):
    X = df[['Units']]
    y = df['Minutes']
    model = LinearRegression()
    model.fit(X, y)
    return model
