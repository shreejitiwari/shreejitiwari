# -*- coding: utf-8 -*-
"""Logistic Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CMnVNHb_liF4ub7JXlUgvRJwV0NJdDJl

## Importing Libraries and Data Set
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

titanic_data=pd.read_csv("Titanic.csv")
titanic_data.head(10)

print("Number of Passengers in original data = "+str(len(titanic_data.index)))

"""# Analysing Data"""

# Data Information
titanic_data.info()

# No. of surviver 
sns.countplot(x="Survived",data =titanic_data)

# No. of Male and Female Surviver
sns.countplot(x="Survived",hue="Sex",data=titanic_data)

# No. of surviver as per the passanger's class
sns.countplot(x="Survived",hue="Pclass",data=titanic_data)

# Histogram on the basis of Age of Passengers
titanic_data["Age"].plot.hist()

# Histogram on the basis of Fare of Passengers
titanic_data["Fare"].plot.hist(bins=20, figsize=(10,5))

sns.countplot(x="SibSp", hue="Sex" , data=titanic_data)

"""## Data Wrangling"""

titanic_data.isnull() # True = Null

# Column wise sum of Null values
titanic_data.isnull().sum()

sns.heatmap(titanic_data.isnull(), yticklabels= False,cmap="viridis")

# Box Plot
sns.boxplot(x="Pclass",y="Age",data = titanic_data)

titanic_data.head(5)

titanic_data.drop("Cabin",axis=1,inplace=True)

titanic_data.head(5)

# Drop NaN value
titanic_data.dropna(inplace=True)

#check whether the NaN drop or not
sns.heatmap(titanic_data.isnull(),cbar=True)

# Check for the Null values
titanic_data.isnull().sum()

sex=pd.get_dummies(titanic_data["Sex"])  
sex.head(5)

sex=pd.get_dummies(titanic_data["Sex"],drop_first=True) # male =1

embark=pd.get_dummies(titanic_data["Embarked"])
embark.head(5)

embark=pd.get_dummies(titanic_data["Embarked"], drop_first=True)
embark.head(2)

pcl=pd.get_dummies(titanic_data["Pclass"],drop_first=True)
pcl.head(2)

titanic_data=pd.concat([titanic_data,sex,embark,pcl], axis=1)

titanic_data.head(5)

# Drop unnecessary column
titanic_data.drop(['PassengerId','Pclass','Name','Sex','Ticket','Embarked'],axis=1,inplace=True)

titanic_data.head(5)

"""## Train tha Data Set"""

# Independet Variables except Survuved variable
X=titanic_data.drop("Survived",axis=1)
y=titanic_data["Survived"]

!pip install sklearn

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)

"""## Logistic Regression"""

from sklearn.linear_model import LogisticRegression

logmodel=LogisticRegression()

logmodel.fit(X_train, y_train)

prediction=logmodel.predict(X_test)

from sklearn.metrics import classification_report

classification_report(y_test, prediction)

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test,prediction)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,prediction)

"""## SUV DATA ANALYSIS"""

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib as plt

# Data Readin
suv_data=pd.read_csv("SUV_Purchase.csv")

suv_data.head(10)

#Select all the rows with 2 and 3 column for X and column 4 for y
X=suv_data.iloc[:,[2,3]].values
y=suv_data.iloc[:,[4]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)*100

