from sklearn.preprocessing import normalize
import csv
import pandas as pd
import numpy as np

data1=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/result_new_now.csv")
#data2=pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/Concat_Data/shubhi_ConcatLie.csv")

data1 = data1.transpose()
a = pd.DataFrame(normalize(data1))
b = a.transpose()


#data2 = data2.transpose() 
#x = pd.DataFrame(normalize(data2))
#y = x.transpose()
b.to_csv('result_final_modified_Norm.csv')
#y.to_csv('shubhi_Lie_Norm.csv')

"""data2 = data2.transpose() 
x = pd.DataFrame(normalize(data2))
y = x.transpose()
y.to_csv('anil_Claps_Norm.csv')
"""
