import numpy as np
import matplotlib.pyplot as plt

def y(x):
    return np.sin(x) + np.sin(3*x)

x = np.linspace(0, 4*np.pi, 1000)

y_vals = y(x)


y_ticks = [-1, -0.3, 0.1, 1]
y_labels = ['Minimum', 'Critical', 'Collapse', 'Maximum']
plt.yticks(y_ticks, y_labels)
plt.ylim(-2,2)

plt.xticks(range(0,16,2))
plt.xlim(0,14)
plt.xlabel("x-axis", color='lightgreen')

plt.grid(True, which='both', linestyle='-', linewidth=0.5)
plt.axhline(-2, color='lightgreen', linewidth=2)
plt.axhline(2, color='lightgreen', linewidth=2)

plt.axvline(2, color='lightgreen', linewidth=1)
plt.axvline(4, color='lightgreen', linewidth=1)
plt.axvline(6, color='lightgreen', linewidth=1)
plt.axvline(8, color='lightgreen', linewidth=1)
plt.axvline(10, color='lightgreen', linewidth=1)
plt.axvline(12, color='lightgreen', linewidth=1)

plt.gca().spines['top'].set_color('lightgreen')
plt.gca().spines['bottom'].set_color('lightgreen')
plt.xticks(color='lightgreen')
plt.yticks(color='black')
plt.grid(axis='y', color='black')

plt.plot(x, y_vals, color='magenta', linewidth=2)

plt.tick_params(axis='both', which='both', top=False, bottom=False, labelbottom=True)

plt.tight_layout()
plt.show()