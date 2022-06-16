#Set the model name.
names = ['LinerRegression',
    'Ridge',
    'Lasso',
    'Random Forrest',
    'GBDT'
    'Support Vector Regression',
    'ElasticNet',
    'XgBoost']
#Define the model.
# cv is the cross-validation idea here.
models = [LinearRegression(),
    RidgeCV(alphas=(0.001,0.1,1),cv=3),
    LassoCV(alphas=(0.001,0.1,1),cv=5),
    RandomForestRegressor(n_estimators=10),
    GradientBoostingRegressor(n_estimators=30),
    SVR(),
    ElasticNet(alpha=0.001,max_iter=10000),
    XGBRegressor()]
# Output the R2 scores of all regression models.
#Define the R2 scoring function.
def R2(model,x_train, x_test, y_train, y_test):
    model_fitted = model.fit(x_train,y_train)
    y_pred = model_fitted.predict(x_test)
    score = r2_score(y_test, y_pred)
    return score
#Traverse all models to score.
for name,model in zip(names,models):
    score = R2(model,x_train, x_test, y_train, y_test)
    print("{}: {:.6f}, {:.4f}".format(name,score.mean(),score.std()))










