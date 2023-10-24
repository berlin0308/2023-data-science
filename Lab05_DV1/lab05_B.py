import numpy as np
import matplotlib.pyplot as plt

f = 5e6  # 5MHz
t = np.linspace(0, 0.5e-6, 500)  # 0 to 0.5 microseconds, adjusted points

in_phase = np.sin(2 * np.pi * f * t)
quadrature = np.sin(2 * np.pi * f * t + np.pi / 2)

plt.figure(figsize=(10, 6))
plt.plot(t * 1e6, in_phase, label='In-Phase (solid)', color='cyan', linewidth=2, markersize=5, mfc='none', linestyle='dotted')
plt.plot(t * 1e6, quadrature, 'o', label='Quadrature (dotted)', color='grey', markersize=5, mfc='none', linestyle='dotted', markeredgecolor='grey')

title = r'In-Phase $\mathit{(solid)}$ and $\mathrm{Quadrature}$ $\mathit{(dotted)}$ Signals'
plt.title(title, fontsize=14)
plt.xlabel('Time (μs)', fontsize=14, fontweight='bold')

plt.ylabel(r"$\mathrm{'\mathit{Normalized}'\ Signal}$", fontsize=14, fontweight='bold')

plt.xticks(np.arange(0, 0.6, 0.1))
plt.yticks(np.arange(-1.5, 2, 0.5))
plt.ylim(-1.5, 1.5)
plt.xlim(0, 0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()
