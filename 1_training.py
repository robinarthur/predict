"""
https://github.com/llSourcell/Predicting_Winning_Teams
works on my machine only under linux
the goal is to predict full time result - FTR
"""
# data preprocessing
import pandas as pd
# produces a prediction model in the form of an ensemble of weak prediction
# models, typically decision tree
import xgboost as xgb
# the outcome (dependent variable) has only a limited number of possible values.
# Logistic Regression is used when response variable is categorical in nature.
from sklearn.linear_model import LogisticRegression
# Arandom forest is a meta estimator that fits a number of decision tree
# classifiers on various sub-samples of the dataset and use averaging to improve
# the predictive accuracy and control over-fitting.
from sklearn.ensemble import RandomForestClassifier
# a discriminative classifier formally defined by a separating hyperplane.
from sklearn.svm import SVC
# displayed data
from IPYTHON.display import display
%matplotlib inline

# Read data anddrop redundant column.
data = pd.read_csv('final_dataset.csv')

# Preview data.
display(data.head())
