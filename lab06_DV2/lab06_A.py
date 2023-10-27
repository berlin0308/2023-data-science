import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv("sales_data.csv")
# print(df.head(10))

# Set XKCD style
with plt.xkcd():
    fig, axs = plt.subplots(2, 1, figsize=(9, 6))

    # Plotting sales data of bathing soap
    axs[0].plot(df["month_number"], df["bathingsoap"], color='black', marker='o', linestyle='-', linewidth=4, markersize=10)
    axs[0].set_title("Sales data of a Bathingsoap", fontsize=24)
    # axs[0].set_ylabel("Sales units in number", fontsize=18)
    axs[0].set_yticks([7500, 10000, 12500])
    axs[0].set_xticks(range(1, 13))
    axs[0].set_xticklabels([])

    # Plotting sales data of facewash
    axs[1].plot(df["month_number"], df["facewash"], color='black', marker='o', linestyle='-', linewidth=4, markersize=10)
    axs[1].set_title("Sales data of a facewash", fontsize=24)
    axs[1].set_yticks([1500, 2000])
    axs[1].set_xlabel("Month Number", fontsize=18) 
    axs[1].set_xticks(range(1, 13))

    # plt.subplots_adjust(hspace=5)
    fig.text(0, 0.5, 'Sales units in number', fontsize=18, rotation='vertical', va='center')
    plt.tight_layout()
    # plt.savefig("lab06_A_result.png")
    plt.show()
