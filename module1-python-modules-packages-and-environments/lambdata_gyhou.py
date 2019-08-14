import pandas as pd


def check_nulls(df_nulls):
    '''
    Return number of nulls in a dataframe.

    df_nulls -- the dataframe to be checked for null values
    '''
    return df_nulls.isnull().sum()


def split_date_columns(X, column_name):
    '''
    Return columns with year, month, and day.
    Converts original column back to string from datetime.

    Keyword arguments:
    X -- the dataframe to be adjusted with new date columns
    column_name -- the name of the column that is to be used to infer datetime,
                   will also be used in naming of new columns
    '''

    X[column_name] = pd.to_datetime(X[column_name])
    X[column_name+'_year'] = X[column_name].dt.year
    X[column_name+'_month'] = X[column_name].dt.month
    X[column_name+'_day'] = X[column_name].dt.day
    X[column_name] = X[column_name].dt.strftime('%Y-%m-%d')
    return X
