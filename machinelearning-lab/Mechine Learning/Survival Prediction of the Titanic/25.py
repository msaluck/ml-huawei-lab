from sklearn.preprocessingsklearn.preprocessing importimport LabelEncoder
lab_enc = LabelEncoder()
# df.iloc[:,4] = lab_enc.fit_transform(df.iloc[:,4])
# or
df['Sex'] = lab_enc.fit_transform(df['Sex'])
df['Embarked'] = lab_enc.fit_transform(df['Embarked'])








