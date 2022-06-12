# creating a new list by replacing nan by mean age for the corresponding title
Age_new=[]
for age, title inin zip(df.Age, df.Title):
    if str(age)=='nan':
        Age_new.append(round(mean_ages[title]))
    else:
        Age_new.append(age)


