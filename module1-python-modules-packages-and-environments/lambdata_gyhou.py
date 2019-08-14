import pandas as pd


def check_nulls(df_nulls):
    return df_nulls.isnull().sum()


def split_date_columns(X, column_name):
    X[column_name] = pd.to_datetime(X[column_name])
    X[column_name+'_year'] = X[column_name].dt.year
    X[column_name+'_month'] = X[column_name].dt.month
    X[column_name+'_day'] = X[column_name].dt.day
    X[column_name] = X[column_name].dt.strftime('%Y-%m-%d')
    return X
