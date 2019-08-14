name = 'lambdata_oliverash'

import pandas as pd

def to_date_format(df, column, drop_column=False):
    df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
    df['Month'] = df[column].dt.month
    df['Day'] = df[column].dt.day
    df['Year'] = df[column].dt.year
    if drop_column == True:
        df = df.drop(columns = column)
    return df

def to_time_format(df, column, drop_column=False, include_seconds=False):
    df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
    df['Hour'] = df[column].dt.hour
    df['Minute'] = df[column].dt.minute
    if include_seconds == True:
        df['Second'] = df[column].dt.second
    if drop_column == True:
        df = df.drop(columns = column)
    return df

class Complex(object):
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def __add__(self, addend):
        return Complex(self.r + addend.r, 
                       self.i + addend.i)
    def __mul__(self, multiplicand):
        return Complex(self.r * multiplicand.r - self.i * multiplicand.i, 
                       self.i * multiplicand.r + self.r * multiplicand.i)