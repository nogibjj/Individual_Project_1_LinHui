import mylib.lib as lib

df = lib.pd_read_csv_backfill('AAPL.csv')

summary_stats = lib.pd_summary_stats(df)

lib.plot_open_price(df)
