# Defining an API -- a list of function definitions to be used by the end user

# Run a supervised learning algorithm to try to classify emails
# -- Need labelled data

# Unsupervised learning
# -- Cluster data
# -- With very few labels and clusters to classify data points

import sklearn
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.neural_network import MLPClassifier

# by default will use spacebar to seperate columns and newline character to seperate rows
data = np.loadtxt("dataset", delimiter=",")
# data is a (4600 rows x 58 columns) numpy array 2D
# 57 features that have to do with word frequency, counted the number of capital letters
# 1 label that is either spam or not spam
print("Shape of email data: ", data.shape)  # prints the shape of the numpy array
print('\n')  # '\n' is the newline character

# numpy indexing <----
v = data[0, 2]  # gets single element with first training example and 3rd attribute
v = data[0, :]  # get the entire first row with all columns
v = data[:, 0]  # get all rows for the 1st attribute
v = data[2:5, :]  # get rows 2-5 (5 not included) with all columns

# split features and labels
x = data[:, :57] # input 2d-array
y = data[:, 57] # trying to predict --- y a 1d-array of either zero or one

# put first 80% of emails into training data
num_train = int(4601 * 0.8)
train_x = x[:num_train, :] # 80% of samples into training
test_x = x[num_train:, :]  # 20% of samples left to test
train_y = y[:num_train]
test_y = y[num_train:]

#  Potential algorithms
# k-nearest-neighbor -- clustering algorithm. Finds the k centers that best group the data points.
# decision tree -- generate boundaries to split data into positive and negative instances
# random forest -- average result from group of decision trees. Each time this algorithm runs the decision trees
# that it makes are randomly selected.
# neural network -- linear regression with nonlinear activation and stacked multiple times
# regression (linear/logistic --- polynomial) -- logistic regression, similar to linear regression but predicts probabilites using the cross entropy loss.
# polynomial regression -- fits a polynomial to your training data


### Random Forest Classifier -- "Classifier" --> identifies which category an input (email) falls into
classifier = RandomForestClassifier()
classifier.fit(train_x, train_y)
# now we can use the classifier to predict on new data
print("random forest predictions: ", classifier.predict(test_x))
print("random forest score: ", classifier.score(test_x, test_y))

### Neural network algorithm
nn_classifier = MLPClassifier(hidden_layer_sizes=5)
nn_classifier.fit(train_x, train_y)
# neural network is overfitting <--
print("nn predictions: ", nn_classifier.predict(test_x))
print("nn score: ", nn_classifier.score(test_x, test_y))

### Linear Regression -- DONT USE FOR CLASSIFICATION PROBLEMS
from sklearn import linear_model
lin_model = linear_model.LinearRegression()
lin_model.fit(train_x, train_y)
print("linear predictions: ", lin_model.predict(test_x))
print("linear regression score: ", lin_model.score(test_x, test_y))

### logistic Regression
from sklearn.linear_model import LogisticRegression
log_classifier = LogisticRegression(random_state=0).fit(train_x, train_y)
print("logistic predictions: ", log_classifier.predict(test_x))
print("logistic regression score: ", log_classifier.score(test_x, test_y))

def classify(email_text):
    # Try to classify into categories (fraudulent-spam, marketing-spam, important, meeting-invitation, not-spam)
    category = -1
    return category