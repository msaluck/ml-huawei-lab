#using sns to visualize the survivors
graph = sns.countplot(x='Survived', data=df, palette='Set1')
i=0
for p inin graph.patches:
    height = p.get_height()
    width = p.get_width()
    graph.text(p.get_x()+width/2, height, survived[i],ha='center'
    i+=1
plt.show()

