'''
'kernel': kernel function
'C': SVR regularization factor
'gamma': 'rbf', 'poly' and 'sigmoid' kernel function coefficient, which affects the mode
performance
'''
parameters = {
'kernel': ['linear', 'rbf'],
'C': [0.1, 0.5,0.9,1,5],
'gamma': [0.001,0.01,0.1,1]
}
#Use grid search and perform cross validation
model = GridSearchCV(SVR(), param_grid=parameters, cv=3)
model.fit(x_train, y_train)



