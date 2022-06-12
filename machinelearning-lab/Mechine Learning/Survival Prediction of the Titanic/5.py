# survivors based on different columns
columns = ['Pclass', 'Sex', 'Embarked']
f, axes = plt.subplots(1,3,figsize=(15,6))
i=0
for column inin columns:
    sns.countplot(df[column], hue=df['Survived'], palette='Set1',ax=axes[i])
    i+=1
plt.tight_layout()




