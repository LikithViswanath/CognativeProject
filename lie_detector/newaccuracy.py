import csv

from sklearn import linear_model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

sns.set()

# fieldnames = ['attention', 'delta', 'meditation', 'rawValue', 'theta','lowAlpha',
# 'highAlpha', 'lowBeta', 'highBeta', 'lowGamma', 'midGamma', 'poorSignal', 'blinkStrength' ,'label']

def lie_dector():
      dataset = pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/result_new_now.csv")
      labels='label'

      data_labels=dataset[labels]
      data_features=dataset.drop(columns=['label'])
      X=data_features
      Y=data_labels

      X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
      logreg = LogisticRegression()
      Y_pred=logreg.fit(X_train,Y_train).predict(X_test)
      print('Accuracy of logistic regression classifier on train set :{:.2f}'.format(logreg.score(X_test,Y_test)))
      Y_pred=logreg.predict(X_train)
      print('Accuracy of logistic regression classifier on test set :{:.2f}'.format(logreg.score(X_train,Y_train)))

      from sklearn.linear_model import LinearRegression
      lr = LinearRegression()

      lr.fit(X_train, Y_train)

      plt.scatter(lr.predict(X_train), Y_train,color="green", s=10, label='Train data')
      plt.title("TRAINING DATA SET")
      plt.xlabel("Predict->X_TRAIN")
      plt.ylabel("Y_TRAIN")
      plt.show()

      plt.scatter(lr.predict(X_test), Y_test,color="blue", s=10,label='Test data')
      plt.title("TESTING DATA SET")
      plt.xlabel("Predict->X_TEST")
      plt.ylabel("Y_TEST")
      plt.show()

      dataTruth = pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/merged_truth.csv")

      dataTruth.drop(columns=['attention', 'meditation', 'rawValue', 'lowAlpha',
                               'lowBeta', 'lowGamma', 'poorSignal', 'blinkStrength', 'label'])

      dataLie = pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/merged_lie.csv")

      dataLie.drop(columns=['attention', 'meditation', 'rawValue', 'lowAlpha',
                              'lowBeta', 'lowGamma', 'poorSignal', 'blinkStrength', 'label'])

      lst_keys = [
            'delta',
            'theta',
            'highAlpha',
            'highBeta',
            'midGamma']


      lst = []

      for i in range(0,200):
        lst.append(i)

      # Horizontal Bar Plot
      for k in lst_keys:
            plt.bar(lst, dataTruth[k][1000:1200], color='green',width=1)

            plt.bar(lst, dataLie[k][1000:1200], color='red',width=1)

            plt.xlabel(k)

            plt.ylabel('value')

            plt.title('Plot of comparision between Truth and Lie ' + k)
            # Show Plot
            plt.show()

if __name__ == '__main__':
    lie_dector()
