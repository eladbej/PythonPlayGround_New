import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

df_league=pd.read_csv("england-premier-league-league-2018-to-2019-stats.csv")
print(df_league.info())

df_teams=pd.read_csv("england-premier-league-teams-2018-to-2019-stats.csv")
print(df_teams.info())

df_players=pd.read_csv("england-premier-league-players-2018-to-2019-stats.csv")
print(df_players.info())

corrMat=df_players.corr(method='pearson')
print(corrMat.info())
input()

df_players=df_players[df_players.age!=0]
df_players=df_players[df_players.min_per_assist_overall!=0]
x=df_players['age']
y=df_players['min_per_assist_overall']
m, b = np.polyfit(x, y, 1)

plt.scatter(df_players['age'],df_players['min_per_assist_overall'])
plt.xticks(np.arange(min(df_players.age)-2,max(df_players.age)+2,1))
plt.plot(x, m*x+b)
plt.xlabel("גיל")
plt.ylabel("Minutes Per Assists Overall")

plt.show()

