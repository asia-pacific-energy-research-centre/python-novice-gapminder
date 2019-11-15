import pandas as pd

df = pd.read_csv("./data/gapminder_all.csv", index_col="country")

print(df.describe())