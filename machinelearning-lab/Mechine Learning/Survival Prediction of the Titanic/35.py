from sklearn.metricssklearn.metrics importimport confusion_matrix
for mod inin model:
    cm = confusion_matrix(y_test, mod.predict(X_test))
    tn, fp, fn, tp = cm.ravel()
    test_score = (tp+tn)/(tn+tp+fn+fp)
    print(cm)
    print('{}{} \n\n Testing Accuracy = {}{}'.format(mod,test_score))
    print()























