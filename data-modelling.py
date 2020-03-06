
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