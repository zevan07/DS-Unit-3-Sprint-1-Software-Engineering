import pandas as pd

name = 'lambdata_oliverash'


def to_date_format(df, column, drop_column=False):
    """Change columns to datatime format and feature engineer
    month, day, year columns into dataframe.
    Drop original column if needed."""
    df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
    df['Month'] = df[column].dt.month
    df['Day'] = df[column].dt.day
    df['Year'] = df[column].dt.year
    if drop_column is True:
        df = df.drop(columns=column)
    return df


def to_time_format(df, column, drop_column=False, include_seconds=False):
    """Change columns to datatime format and feature engineer
    hour, minute, and second columns into dataframe.
    Drop original column if needed."""
    df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
    df['Hour'] = df[column].dt.hour
    df['Minute'] = df[column].dt.minute
    if include_seconds is True:
        df['Second'] = df[column].dt.second
    if drop_column is True:
        df = df.drop(columns=column)
    return df


class Complex(object):
    """Add or multiply complex numbers"""
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def __add__(self, addend):
        return Complex(self.r + addend.r,
                       self.i + addend.i)

    def __mul__(self, multiplicand):
        return Complex(self.r * multiplicand.r - self.i * multiplicand.i,
                       self.i * multiplicand.r + self.r * multiplicand.i)
