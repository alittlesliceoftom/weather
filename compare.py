'''
This module is for comparisons to previous years data. 
'''

def time_index_with_lambda():
    df.loc[lambda df: (df.index.month ==2) & (df.index.day ==1)]

def get_matching_days(df):
    # compare current date to all of the previous similar ones: 
    index_value = df.tail(lookback_days).index[0]
    day, month = index_value.day, index_value.month

    # Get all the years with the same days
    # all_years = days.shift(-1, freq= 'Y')
    return df.loc[lambda df: (df.index.month ==month) & (df.index.day ==day)]


def compare(df, compare_column = 'tavg', lookback_days = 7):
    '''
    Given a set of data, compare the data in the compare_column for different time periods
    '''
    data = get_matching_days(df)
    tmp_series = data[compare_column]
    print(tmp_series.describe())
    

    print(f'Today is {tmp_series[compare_column]}')

    return data