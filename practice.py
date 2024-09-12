
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




data = pd.read_csv("example.csv")
print(data.info())
print(data.describe())
print(data.describe().transpose().round(1))

data2 = pd.read_csv("example.csv", skiprows=1)
data3 = pd.read_csv("example.csv", skiprows=1, header=None)


data4 = pd.read_csv("example.csv", nrows=2)




data5 = pd.read_excel("example.xlsx")
data5.to_excel("new_example2.xlsx", index=False)



data.rename(columns={'Area':'a', 'Storey':'b', 'Bedrooms':'c', 'Garrage':'d', 'Built':'e', 'Suburbs':'f'}, inplace=True)


