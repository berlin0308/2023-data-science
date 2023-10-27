import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mpl_colors

df = pd.read_csv("Score.csv")
df = df.sort_values(by=['Round', 'Team'], ascending=[False, True])

teams = df['Team'].unique()
colors = {'D': 'green', 'K': 'blue', 'P': 'orange'}
colors = {team: mpl_colors.to_rgba(colors[team], alpha=0.65) for team in teams}

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_title('Points', fontsize=16)
ax.xaxis.tick_top()  # Move x-labels to top
ax.set_xlim([0, 160])
ax.tick_params(axis='x', colors='grey')
ax.set_xticks(range(0, 161, 20))
ax.grid(axis='x', linestyle='-', linewidth=0.5, color='grey')


teamnames = ['Team D', 'Team K', 'Team P']
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

handles = [plt.Rectangle((0, 0), 1, 1, color=colors[team]) for team in teams]
ax.legend(handles, teamnames, loc='lower right')

bottoms = {round: 0 for round in df['Round'].unique()}
for team in teams:
    team_data = df[df['Team'] == team]
    ax.barh(team_data['Round'], team_data['Score'], color=colors[team], left=[bottoms[row['Round']] for _, row in team_data.iterrows()])

    for _, row in team_data.iterrows():
        bottoms[row['Round']] += row['Score']

rounds_unique = df['Round'].unique()
for row in rounds_unique:
    teamD_score = df[(df["Round"] == row) & (df["Team"] == "D")]["Score"].values[0]
    teamD_leader = df[(df["Round"] == row) & (df["Team"] == "D")]["Leader"].values[0]

    teamK_score = df[(df["Round"] == row) & (df["Team"] == "K")]["Score"].values[0]
    teamK_leader = df[(df["Round"] == row) & (df["Team"] == "K")]["Leader"].values[0]

    try:
        teamP_score = df[(df["Round"] == row) & (df["Team"] == "P")]["Score"].values[0]
        teamP_leader = df[(df["Round"] == row) & (df["Team"] == "P")]["Leader"].values[0]
        ax.text(teamD_score + teamK_score + teamP_score/2 , row, teamP_leader, ha='center', va='center', color='black', fontsize=14)
    except:
        pass

    ax.text(teamD_score/2, row, teamD_leader, ha='center', va='center', color='black', fontsize=14)
    ax.text(teamD_score + teamK_score/2 , row, teamK_leader, ha='center', va='center', color='black', fontsize=14)

plt.tight_layout()
plt.savefig("lab06_C_results.png")
plt.show()
