#Load the Boston house price data set.
boston = load_boston()
#x features, and y labels.
x = boston.data
y = boston.target
#Display related attributes.
print('Feature column name')
print(boston.feature_names)
print("Sample data volume: %d, number of features: %d"% x.shape)
print("Target sample data volume: %d"% y.shape[0])










