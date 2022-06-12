def models(X_train, y_train):
    # Logistic Regression
    from sklearn.linear_modelsklearn.linear_model importimport LogisticRegression
    lr = LogisticRegression(random_state=420
    lr.fit(X_train, y_train
    # KNN
    from sklearn.neighborssklearn.neighbors importimport KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
    knn.fit(X_train, y_train)
    # SVM (linear kernel)
    from sklearn.svmsklearn.svm importimport SVC
    svc_lin = SVC(kernel='linear', random_state=420)
    svc_lin.fit(X_train, y_train)
    #   SVM (rbf kernel)
    from sklearn.svmsklearn.svm importimport SVC
    svc_rbf = SVC(kernel='rbf', random_state=420)
    svc_rbf.fit(X_train, y_train)
    # Gaussian Naive Bayes
    from sklearn.naive_bayessklearn.naive_bayes importimport GaussianNB
    gauss = GaussianNB()
    gauss.fit(X_train, y_train)
    # Decision tree classifier
    from sklearn.treesklearn.tree importimport DecisionTreeClassifier
    dtc = DecisionTreeClassifier(criterion='entropy', random_state=420)
    dtc.fit(X_train, y_train)
    # Random Forest Classifier
    from sklearn.ensemblesklearn.ensemble importimport RandomForestClassifier
    rfc = RandomForestClassifier(n_estimators=20, criterion='entropy', random_state=420)
    rfc.fit(X_train, y_train)
    # Printing training accuracy for each model
    print('Training accuracy for logistic regression = ', lr.score(X_train, y_train))
    print('Training accuracy for KNN = ', knn.score(X_train, y_train))
    print('Training accuracy for SVC(Linear) = ', svc_lin.score(X_train, y_train))
    print('Training accuracy for SVC(rbf) = ', svc_rbf.score(X_train, y_train))
    print('Training accuracy for Gaussian Naive Bayes = ', gauss.score(X_train, y_train))
    print('Training accuracy for Decision Tree Classifier = ', dtc.score(X_train, y_train))
    print('Training accuracy for Random Forest Classifier = ', rfc.score(X_train, y_train))
    return lr, knn, svc_lin, svc_rbf, gauss, dtc, rfc































