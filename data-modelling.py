
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

from xgboost import XGBClassifier

# Create and fit XGBoost model
model_01 = XGBClassifier()
model_01.fit(train_X, train_target)

# Predict values on test set
Y_pred_01 = model_01.predict(test_X)



#=============================================================================#
# Classification model assessment #
#=================================#

from sklearn.metrics import confusion_matrix

# Distinguish unique values of target_test variable
unique, counts = np.unique(test_target, return_counts=True)
for i in range(0,len(unique)):
    print(unique[i], ": ", counts[i])
# categories are printed in order of future confusion matrix











