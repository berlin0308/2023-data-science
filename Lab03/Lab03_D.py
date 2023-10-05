import numpy as np
import matplotlib.pyplot as plt


def transition_matrix(n):
    P = []

    # TODO_D1

    return P

def propagate(x0, P, k):
    xk = None

    # TODO_D2

    return xk

def create_sample(s0, P, k):
    trajectories = []

    # TODO_D6

    return trajectories

def plot_distribution(x):
    plt.plot(x)
    plt.xticks(np.arange(0, len(x), step=1))
    plt.ylim(0, max(x)+0.1)
    plt.xlabel('State (i)')
    plt.ylabel('Probability')
    plt.title('Probability Distribution')
    plt.savefig('Lab04_D3.png', dpi=150)

def plot_histogram(x):
    plt.hist(x, bins=max(x)+1, range=(-0.5, max(x)+0.5))
    plt.xticks(np.arange(0, max(x)+1, step=1))
    plt.xlabel('State (i)')
    plt.ylabel('Number of smaple')
    plt.title('State Histogram')
    plt.savefig('Lab04_D7.png', dpi=150)
    
def main():
    
    P = transition_matrix(n=10)

    # TODO_D3, D4, D5,and D7

if __name__ == "__main__":
    main()