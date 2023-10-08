import numpy as np

def swap_rows(x, r1, r2):
    # no return values needed
    # no loops allowed
    # do not declare new variables, manipulate x directly
    x[r1], x[r2] = x[r2].copy(), x[r1].copy()
    # print(x)

def most_value(x):
    # no loops allowed
    return np.argmax(np.bincount(x))

def top_n(x, n):
    # no loops allowed
    return x[np.argpartition(x, -n)[-n:]]
    
def pythagorean(x):
    # print(x.shape)
    # print(x.ndim)

    if x.ndim == 1:
        x = np.array([x])
        # print(x.shape)
        # print(x.ndim)

    if x.shape[1] != 2:
        raise ValueError("Input matrix must have exactly two columns")

    a = x.copy()[:,0]
    b = x.copy()[:,1]
    # print(a, b)

    c = np.sqrt(a**2 + b**2)

    return c

def replace_me(v, a, b=0, c=None):
    if c is None:
        c = b
    
    # print(v==a)
    mask_a = (v==a)
    # print(np.where(mask_a))

    new_v = v.copy()
    new_v[np.where(mask_a)[0]] = b
    new_v = np.insert(new_v, np.where(mask_a)[0]+1, c)
    return new_v


# You may test your function here
def main():

    # Lab04_C1 Swap rows
    print('Lab04_C1 Swap rows:')
    x1 = np.arange(9).reshape(3, 3)
    swap_rows(x1, 0, 1)
    print(x1, '\n')

    # Lab04_C2 Find most frequent value
    print('Lab04_C2 Find most frequent value:')
    x2 = np.array([1, 2, 2, 1, 3, 2, 4, 1, 2])
    print('The most frequent value is: ', most_value(x2), '\n')

    # Lab04_C3 top n
    print('Lab04_C3 Top n:')
    x3 = np.array([1, 0, 3, 5, 7, 3, 2, 8, 9, 2, 8])
    print('The 3 largest values are: ', top_n(x3, n=3), '\n')

    # Lab04_C4 pythagorean
    print('Lab04_C4 pythagorean:')
    x4 = np.array([[3, 4], [5, 12]])
    # x4 = np.array([3, 3])
    print(pythagorean(x4))

    try:
        pythagorean(np.array([12]))
        print('If you see this line, you may not check the input array', '\n')
    except:
        print('\n')

    # Lab04_C5 replace_me
    print('Lab04_C5 replace_me:')
    x5 = np.array([1, 2, 3])
    # x5 = np.array([1, 2, 3, 2])
    print(replace_me(x5, 2, 4, 5), '\n')
    # print(replace_me(x5, 2, 99999), '\n')
    # print(replace_me(x5, 2), '\n')


if __name__ == "__main__":
    main()