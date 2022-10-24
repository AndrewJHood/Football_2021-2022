import pandas as pd
import numpy as np

df = pd.read_csv("2021-2022 Football Team Stats.csv", encoding="latin1", delimiter=';')
epl = df[df.Country == 'ENG']

print(epl)
print(epl.describe())
print(epl.info())