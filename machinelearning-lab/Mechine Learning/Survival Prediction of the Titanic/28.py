# creating a new data set
df_num = df.drop(['PassengerId','Name', 'Ticket', 'Title'], axis=1)
df_num.head(10)


