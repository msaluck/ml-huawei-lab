df['Title'] = df['Name'].str.split('.').str[0].str.split(',').str[1]
df






