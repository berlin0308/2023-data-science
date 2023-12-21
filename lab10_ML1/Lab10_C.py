import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

def plot_violinplot(train, test, feature):
    plt.figure(figsize=(2, 2))
    plt.violinplot([train[feature], test[feature]])
    plt.xticks([1, 2], ['Train', 'Test'])
    plt.title(f'Violin Plot of {feature}')
    plt.show()

def plot_position_cat(train, test, feature):
    plt.figure(figsize=(2, 2))
    # role_counts.plot(kind='bar')
    plt.title('Distribution of Roles')
    plt.xlabel('Role')
    plt.ylabel('Count')
    plt.violinplot([train[feature], test[feature]])
    plt.xticks([1, 2], ['Train', 'Test'])
    plt.title(f'Violin Plot of {feature}')
    plt.show()

def main():
    data = pd.read_csv('epldata_final.csv')
    age = data['age']
    page_views = data['page_views']
    data['age^2'] = age**2
    data['log_pages'] = np.log2(page_views)
    for i in range(data.shape[0]):
        if data['position_cat'][i]==1:
            data['position_cat'][i] = 'attacker'
        elif data['position_cat'][i]==2:
            data['position_cat'][i] = 'midfielders'
        elif data['position_cat'][i]==3:
            data['position_cat'][i] = 'defenders'
        elif data['position_cat'][i]==4:
            data['position_cat'][i] = 'goalkeepers'

    train_data, test_data = train_test_split(data, test_size=0.2)
    cols = ['fpl_points','age','age^2','log_pages','new_signing','big_club','position_cat']
    
    # print(train_data['position_cat'])

    X_train = train_data[cols]
    X_test = test_data[cols]
    X_train = pd.get_dummies(X_train, columns=['position_cat'])
    X_test = pd.get_dummies(X_test, columns=['position_cat'])
    y_train = train_data['market_value']
    y_test = test_data['market_value']

    print(X_train)

    polynomial_model = LinearRegression(fit_intercept=True)
    polynomial_model.fit(X_train, y_train)
    r2_train = r2_score(y_train, polynomial_model.predict(X_train))
    r2_test = r2_score(y_test, polynomial_model.predict(X_test))
    y_pred = polynomial_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print('coef: \t', polynomial_model.coef_)
    print('inter: \t', polynomial_model.intercept_)
    print('Mean squared error: \t', mse)
    print("Train R2 is {}, while test R^2 is {}".format(r2_train, r2_test))

    # plt.scatter(X_train, y_train)
    # plt.show()
    for feature in cols:
        pass
        # plot_feature_distribution(X_train, X_test, feature)
        # plot_violinplot(X_train, X_test, feature)

        # if feature == 'position_cat':
        #     plot_position_cat(train_data, test_data, feature)



if __name__ == "__main__":
    main()

