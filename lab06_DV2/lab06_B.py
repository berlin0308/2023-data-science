import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

df = pd.read_excel("Scatter.xlsx")

colors = {0: 'pink', 1: 'yellow', 2: 'lightblue'}
markers = {0: '^', 1: 'o', 2: 's'}
labels = {0: 'c/c', 1: 'C/c', 2: 'C/C'}

# Set font sizes
plt.rcParams.update({
    'font.size': 10,              # Default font size
    'legend.fontsize': 'large',  # Legend font size
    'xtick.labelsize': 10,       # X-axis tick label size
    'ytick.labelsize': 10,       # Y-axis tick label size
})

fig, axs = plt.subplots(2, 2, figsize=(6, 4), gridspec_kw={'width_ratios': [1, 3], 'height_ratios': [3,1]})

# PC2-histogram
data_to_stack = [group['PC2'] for genotype, group in df.groupby('Genotype')]

axs[0,0].hist(data_to_stack, bins=10, orientation='horizontal', color=[colors[i] for i in range(3)], label=[labels[i] for i in range(3)], 
               stacked=True, alpha=0.6, edgecolor='black', rwidth=0.8)

axs[0,0].set_xlabel('Frequency')
axs[0,0].set_xticks([0, 5, 10])
axs[0,0].set_ylim([-400, 400])
axs[0,0].set_yticks(range(-400,600,200))
axs[0,0].set_ylabel('PC2')

# Legend
legend_elements = [Line2D([0], [0], color=colors[0], marker=markers[0], markersize=10, label='c/c', linestyle='None', markeredgecolor='black'),
                   Line2D([0], [0], color=colors[1], marker=markers[1], markersize=10, label='C/c', linestyle='None', markeredgecolor='black'),
                   Line2D([0], [0], color=colors[2], marker=markers[2], markersize=10, label='C/C', linestyle='None', markeredgecolor='black')]

axs[1,0].legend(handles=legend_elements, fontsize='small', loc='center', handlelength=0, handletextpad=2, bbox_to_anchor=(0.5, 0))
axs[1,0].axis('off')

# PC1-histogram
data_to_stack = [group['PC1'] for genotype, group in df.groupby('Genotype')]
axs[1,1].hist(data_to_stack, bins=10, orientation='vertical', color=[colors[i] for i in range(3)], label=[labels[i] for i in range(3)], 
               stacked=True, alpha=0.6, edgecolor='black', rwidth=0.8)

axs[1,1].set_ylabel('Frequency')
axs[1,1].set_xlabel('PC1')
axs[1,1].set_yticks([0, 5, 10])
axs[1,1].set_xticks(range(-400, 600, 200))
axs[1,1].set_xlim([-400, 400])

# PC1-PC2 Scatter Plot
for genotype, group in df.groupby('Genotype'):
    axs[0,1].scatter(group['PC1'], group['PC2'], color=colors[genotype], marker=markers[genotype], label=labels[genotype], edgecolor='black')

axs[0,1].set_xlabel('PC1')
axs[0,1].set_ylabel('PC2')
axs[0,1].set_xticks(range(-400, 600, 200))
axs[0,1].set_yticks(range(-400, 600, 200))
axs[0,1].set_title('Scatter Plot', fontsize=12)

plt.tight_layout()
# plt.savefig("lab06_B_result.png")
plt.show()
