import mylib.lib as lib
import pandas as pd


def test_pd_read_csv_backfill():
    # Create a test CSV file
    test_data = "index,A,B\n0,1,\n1,,3\n2,4,5"
    with open('test.csv', 'w') as f:
        f.write(test_data)

    df = lib.pd_read_csv_backfill('test.csv')
    assert df['A'].isnull().sum() == 0, \
    f"Expected 0 NaN in column A, got {df['A'].isnull().sum()}"
    assert df['B'].isnull().sum() == 0, \
    f"Expected 0 NaN in column B, got {df['B'].isnull().sum()}"

def test_pd_summary_stats():
    data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]}
    df = pd.DataFrame(data)
    result = lib.pd_summary_stats(df)
    assert 'mean' in result.index
    assert 'std' in result.index
    assert 'median' in result.index

def test_plot_open_price():
    data = {'Open': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    lib.plot_open_price(df, save=True)
    assert os.path.exists('Open price figure.png')
