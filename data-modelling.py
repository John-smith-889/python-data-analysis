
#=============#
# Test design #
#=============#

from sklearn.model_selection import train_test_split

# split data set into train and test sets

train_X, test_X, train_target, test_target = \
train_test_split(dataset.iloc[:,[0,1,2,3]].values, \
                 dataset['Target_variable'].values, test_size = 0.30, \
                 random_state = 10)

"""
Input:
	explanatory variables ndarray,
	target variables ndarray,
	test_size, 
	random_state


Output:
	explanatory variables training set ndarray,
	explanatory variables test set ndarray,
	target variables training set ndarray,
	target variables test set ndarray
"""


#=============================================================================#
# Classification #
#================#

#=========#
# XGBoost #
#=========#
# Good for small to medium datasets

from xgboost import XGBClassifier

# Create and fit XGBoost model
model_01 = XGBClassifier()
model_01.fit(train_X, train_target)

# Predict values on test set
Y_pred_01 = model_01.predict(test_X)


#=====#
# SVM #
#=====#
# Good for NLP datasets

from sklearn.svm import LinearSVC

# Create instance of linear support vector classifier from Sci-kit learn
model_02 = LinearSVC()

# training the model
model_02.fit(train_X, train_target)

# Predict values on test set
Y_pred_02 = model_02.predict(test_X)



#=============================================================================#
# Classification model assessment #
#=================================#

from sklearn.metrics import confusion_matrix

# Distinguish unique values of target_test variable
unique, counts = np.unique(test_target, return_counts=True)
for i in range(0,len(unique)):
    print(unique[i], ": ", counts[i])
# categories are printed in order of future confusion matrix


#=========================#
# Create confusion matrix #
#=========================#

confusion_matrix(target_test, Y_pred_01)

"""
As we may see in the matrix:
    1) row 1, column 1 - number of observations of category 1 classified as category 1
    2) row 2, column 2 - number of observations of category 2 classified as category 2
    3) row 3, column 3 - number of observations of category 3 classified as category 3
    4) etc.
    
"""








