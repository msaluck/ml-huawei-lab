# survival rate by sex
df['Survived'].groupby(df['Sex']).mean()
# it shows the proportion of passengers survived based on gender


