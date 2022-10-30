from pyexpat.errors import XML_ERROR_UNEXPECTED_STATE
from tkinter.tix import COLUMN
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv('adm_data.csv')

edu = {0:'Some high school',1:'High School',2:'Some college', 3:'assiociates degree', 4:'Bachelors degree', 5:'Masters degree'}

data = data[['CGPA', 'GRE Score', 'Chance of Admit ']]
print(data)
predict = 'Chance of Admit '
x = data.drop(columns = [predict])
#x = data[predict]
y= data[predict]

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size = 0.1)

# linear = linear_model.LinearRegression()
# linear.fit(x_train, y_train)
# acc = linear.score(x_test, y_test)
# print(acc)

modell = linear_model.LinearRegression()
modell.fit(x_train,y_train)

#modell = joblib.load('ai_testing.joblib')
predictions = modell.predict(x_test)

score = modell.score(x_test, y_test)
print(predictions)
print('r^2:',score)