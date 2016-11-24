# coding:utf-8
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model


def get_data(file_name):
    data = pd.read_csv(file_name)
    x_parameter = []
    y_parameter = []
    for feet, price in zip(data['feet'], data['price']):
        x_parameter.append([float(feet)])
        y_parameter.append(float(price))
    return x_parameter,y_parameter


def linear_modle_main(x_parameter, y_parameter, predict_value):
     # create linear regression object
     regr = linear_model.LinearRegression()
     regr.fit(x_parameter, y_parameter)
     predict_outcome = regr.predict(predict_value)
     predictions = {}
     predictions['intercept'] = regr.intercept_
     predictions['coefficient'] = regr.coef_
     predictions['predict_price'] = predict_outcome
     return predictions


def show_linear_line(x, y):
    regr = linear_model.LinearRegression()
    regr.fit(x, y)
    plt.scatter(x, y, color='red')
    plt.xticks(())
    plt.yticks(())
    plt.show()

x,y = get_data('input_data.csv')
predict_value = 700
result = linear_modle_main(x, y, predict_value)
print "Intercept value: ", result['intercept']
print "Coefficient:", result['coefficient']
print "Predict value:", result['predict_price']


# show linear line
show_linear_line(x,y)