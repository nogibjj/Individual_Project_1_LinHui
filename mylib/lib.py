# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def pd_read_csv_backfill(filename):
    """read csv using pandas with method backfill"""
    return pd.read_csv(filename, index_col = 0)\
    .fillna(method = 'backfill')

def pd_summary_stats(df):
    """return summary stats of a df with min, max, mean, median, std etc."""
    return pd.concat([df.describe(include='all').drop('count').T, \
     df.median().rename('median')], axis=1).T.round(decimals=2)

def plot_open_price(df, save = False):
    """plot open price against date from a price dataframe"""
    plt.plot(df['Open'])
    plt.xticks(df.index[::40], rotation=20)
    plt.xlabel('Date')
    plt.ylabel('Open Price')
    plt.title('Open price in the past year')
    if save:
        plt.savefig('Open price figure.png')
    plt.show()
