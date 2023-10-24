import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'March', 'April', 'May', 'June']
sales = [13, 5, 7, 14, 10, 12]

plt.figure(figsize=(8,5))
plt.plot(months, sales, marker='o', color='turquoise', linestyle='-', linewidth=2, markersize=10, markerfacecolor='white', markeredgewidth=2, markeredgecolor='teal')

plt.title('Print Sales for January to June, 2022', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Monthly Sales ($1000)', fontsize=14)

plt.yticks(list(range(0, 16, 5)))
plt.ylim(0, 15)
plt.tight_layout()

plt.show()
