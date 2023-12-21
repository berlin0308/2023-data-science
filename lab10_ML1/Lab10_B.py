import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

def simple_linear_regression_fit(x_train: np.ndarray, y_train: np.ndarray) -> np.ndarray:
    """
    Inputs:
    x_train: a (num observations by 1) array holding the values of the predictor variable
    y_train: a (num observations by 1) array holding the values of the response variable

    Returns:
    beta_vals:  a (num_features by 1) array holding the intercept and slope coeficients
    """
    
    x_mean = np.mean(x_train)
    y_mean = np.mean(y_train)
    numerator = 0
    denominator = 0
    for i in range(y_train.size):
        numerator+=(x_train[i,0]-x_mean)*(y_train[i]-y_mean)
        denominator+=(x_train[i,0]-x_mean)**2
    beta_1 = numerator/denominator
    beta_0 = y_mean-beta_1*x_mean

    return np.array([beta_0, beta_1])


def main():
    X_train = np.array([1,2,3]).reshape((3,1))
    y_train = np.array([2,2,4])
    fig = plt.figure(figsize=(8,6))
    ax1 = fig.add_subplot(111)
    ax1.scatter(X_train, y_train)
    ax1.set_title('scatter')
    slope = simple_linear_regression_fit(X_train, y_train)[1]
    intercept = simple_linear_regression_fit(X_train, y_train)[0]
    print(simple_linear_regression_fit(X_train, y_train))
    x = np.array([0,4])
    f = lambda x: slope*x + intercept
    plt.plot(x,f(x),lw=7,c='r',label='simple_linear_regression_fit()')


    linear_model = LinearRegression(fit_intercept=True)
    linear_model.fit(X_train,y_train)
    g = lambda x: linear_model.coef_*x + linear_model.intercept_
    # plt.plot(x,g(x),lw=1.5,c='g',label='sklearn-LinearRegression()')

    plt.ylim(0,5)
    plt.legend()
    plt.savefig("result_B1")
    plt.show()


if __name__ == "__main__":
    main()