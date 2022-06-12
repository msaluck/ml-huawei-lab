# Calculating mean age for different titles
mean_ages = df['Age'].groupby(df['Title']).mean()
mean_ages.to_dict()




