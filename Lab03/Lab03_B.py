import numpy as np
from random import randrange

np.set_printoptions(suppress=True)

A = np.arange(5, -5.2, -0.2)

B = (np.ones(101)*10)**np.arange(0, 1.01, 0.01)

C = np.arange(1,101).reshape(10,10,order='F')

D = np.arange(1, 13).reshape(12, 1) * np.arange(1, 13)


def E(X):
    return X[::2, ::2]

def F(X):
    return X[1:-1,1:-1]

def G(X):
    # The shape of return value will be (M, 2)
    upp_left = X[:-1,1:]
    Y1 = np.diag(upp_left)

    low_right = X[1:,:-1]
    Y2 = np.diag(low_right)
    
    return np.stack((Y1, Y2), axis=1)


# Do NOT modifiy the main function
def main():

    print('A: \n', A, '\n')
    print('B: \n', B, '\n')
    print('C: \n', C, '\n')
    print('D: \n', D, '\n')

    M = randrange(3, 8)
    X = np.random.randint(10, size=(M, M))

    print('X: \n', X, '\n')
    print('E: \n', E(X), '\n')
    print('F: \n', F(X), '\n')
    print('G: \n', G(X), '\n')


if __name__ == "__main__":
    main()