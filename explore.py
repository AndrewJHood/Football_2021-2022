import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("2021-2022 Football Team Stats.csv", encoding="latin1", delimiter=';')
epl = df[df.Country == 'ENG']

print(epl)
print(epl.describe())
print(epl.info())

epl_goals_top5 = epl[['Squad', 'GF', 'LgRk']]
epl_goals_top5 = epl_goals_top5[epl_goals_top5.LgRk < 6]


plt.bar(data=epl_goals_top5, x='Squad', height='GF', color=['lightblue', 'red', 'blue', 'gray', 'red'])
plt.title('Top 5 Premier League Teams\' Goals')
plt.xlabel("Team")
plt.ylabel("Goals")
plt.show()
plt.close()
