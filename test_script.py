

# def test_numpy():
#     import numpy as np
#     assert np.__version__ == '1.25.1'

import mylib.lib as lib

def test_script():
    df = lib.pd_read_csv_backfill('AAPL.csv')
    assert isinstance(df, lib.pd.DataFrame), "Expected a DataFrame object"
    assert not df.isnull().any().any(), "DataFrame should not contain any NaNs"
    summary_stats = lib.pd_summary_stats(df)
    assert 'mean' in summary_stats.index
    assert 'std' in summary_stats.index
    assert 'median' in summary_stats.index
