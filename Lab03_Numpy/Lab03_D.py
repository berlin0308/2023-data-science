import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=False)

def transition_matrix(n):

    # TODO_D1
    if n == 2:
        return np.array([[0.4, 0.6],[0.5, 0.5]])

    P = np.zeros((n, n))
    
    P[np.arange(n-1), np.arange(1, n)] = np.where(np.arange(n-1) < n/2, 0.60, 0.50)
    P[np.arange(1, n), np.arange(n-1)] = np.where(np.arange(n-1) < n/2-1, 0.35, 0.40)
    P[np.arange(1, n), 0] = np.where(np.arange(1, n) < n/2, 0.05, 0.10)

    # special cases
    P[0, 0] = 0.40
    P[1, 0] = 0.40
    P[-1, -1] = 0.50

    return P

def propagate(x0, P, k):

    # TODO_D2
    from numpy.linalg import matrix_power

    xk = x0 @ (matrix_power(P, k))

    assert abs(np.sum(xk)-1.0) < 1e-6

    return xk

def create_sample(s0, P, k):
    trajectories = [s0]
    current_state = s0
    next_states = P[current_state]
    # print(P[current_state])

    # TODO_D6
    import random
    for i in range(k):
        next_state = random.choices(range(len(next_states)), P[current_state])[0]
        # print(next_state)
        trajectories.append(next_state)
        current_state = next_state

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
    plt.clf()
    plt.hist(x, bins=max(x)+1, range=(-0.5, max(x)+0.5))
    plt.xticks(np.arange(0, max(x)+1, step=1))
    plt.xlabel('State (i)')
    plt.ylabel('Number of smaple')
    plt.title('State Histogram')
    plt.savefig('Lab04_D7.png', dpi=150)
    
def main():
    
    P = transition_matrix(n=10)
    # print(P)


    # TODO_D3, D4, D5,and D7
    # D3
    x0 = np.zeros(10, dtype=int)
    x0[0] = 1
    # print(x0)
    x8 = propagate(x0, P, k=8)
    print(x8)
    print("Highest: {} with prob {}".format(np.argmax(x8),np.max(x8)))
    print("Final state prob: {}".format(format(x8[-1],'.20f')))
    # Highest: 0 with prob 0.20327944000000003
    # Final state prob: 0.00000000000000000000
    plot_distribution(x8)

    # D4
    n = 0
    while True:
        xn = propagate(x0, P, k=n)
        # print(xn)
        # print("Final state prob: {}".format(format(xn[-1],'.20f')))
        n += 1

        if xn[-1] > 0.01:
            print("Step:",n)
            print("Final state prob: {}".format(format(xn[-1],'.10f')))
            # Step: 12
            # Final state prob: 0.0122472000
            break

    # D5
    random_x0 = np.random.random(10)
    norm_x0 = random_x0 / np.sum(random_x0)
    print(norm_x0)
    x8 = propagate(norm_x0, P, k=8)
    print(x8)
    print("Highest: {} with prob {}".format(np.argmax(x8),np.max(x8)))
    print("Final state prob: {}".format(format(x8[-1],'.20f')))
    plot_distribution(x8)

    # D6
    samples = create_sample(s0=0, P=P, k=20)
    print(samples)

    # D7
    last_state = []
    for _ in range(1000):
        sample = create_sample(s0=0, P=P, k=8)[-1]
        last_state.append(sample)

    # print(last_state)
    plot_histogram(last_state)
    

    # import matplotlib.pyplot as plt
    # import matplotlib.image as mpimg
    # import cv2

    # image1 = mpimg.imread('Lab04_D3.png')
    # image2 = mpimg.imread('Lab04_D7.png')

    # if image1.shape[1] != image2.shape[1]:
    #     image1 = cv2.resize(image1, (image2.shape[1], image1.shape[0]))

    # # Concatenate the images vertically
    # new_image = np.vstack((image1, image2))

    # plt.imshow(new_image)
    # plt.axis('off')
    # # plt.show()
    # plt.savefig('Lab04_D.png', dpi=150)




if __name__ == "__main__":
    main()