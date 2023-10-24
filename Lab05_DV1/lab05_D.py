import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


df = pd.read_csv('pokemon_data.csv', delimiter=',', encoding='utf-8')
print(df.head(10))

# Scatter plot for each cluster
colors = ['magenta', 'green', 'cyan']
centroids = [(49.875000, 48.075000), (79.801887, 74.386792), (112.270833, 102.479167)]

for cluster, color in enumerate(colors):
    subset = df[df['cluster'] == cluster]
    plt.scatter(subset['Attack'], subset['Defense'], c=color ,s=4, label=f'Cluster {cluster}')

# Plot centroids
for idx, (x, y) in enumerate(centroids):
    plt.scatter(x, y, c=colors[idx], s=100, marker='^', label=f'Cent. of cluster{idx}')

legend_elements_cluster = [
    Line2D([0], [0], color='magenta', marker='o', markersize=2, label='Cluster 0', linestyle='None'),
    Line2D([0], [0], color='green', marker='o', markersize=2, label='Cluster 1', linestyle='None'),
    Line2D([0], [0], color='cyan', marker='o', markersize=2, label='Cluster 2', linestyle='None'),
]

legend_elements_centroid = [
    Line2D([0], [0], color='magenta', marker='^', markersize=10, label='Cent. of cluster0', linestyle='None'),
    Line2D([0], [0], color='green', marker='^', markersize=10, label='Cent. of cluster1', linestyle='None'),
    Line2D([0], [0], color='cyan', marker='^', markersize=10, label='Cent. of cluster2', linestyle='None')
]

# Display the legends side by side
legend1 = plt.legend(handles=legend_elements_cluster, loc='upper right', bbox_to_anchor=(0.77,1))
plt.gca().add_artist(legend1)  # Add the first legend back after the second one overrides it
legend2 = plt.legend(handles=legend_elements_centroid, loc='upper right', bbox_to_anchor=(1.005,1))


plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Scatter plot of pokemons')
plt.grid(False)
plt.gcf().set_size_inches(9, 8)
plt.show()