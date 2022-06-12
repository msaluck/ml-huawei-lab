# extracting feature importances using RFC model
rfc = model[-1]
features=df_num.iloc[:,1:].columns
importances = rfc.feature_importances_
feat_imp = pd.DataFrame({'Feature':features, 'Importance':importances})
feat_imp = feat_imp.sort_values('Importance', ascending=FalseFalse).set_index('Feature')
feat_imp

















