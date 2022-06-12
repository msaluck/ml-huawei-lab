#dropping the Cabin column as 177 rows are empty)
df.drop(['Cabin'], axis=1, inplace=TrueTrue)
# dropping the rows containing Nan in Embarked column (2 rows)
df.dropna(subset=['Embarked'], axis=0, inplace=TrueTrue

df







