f, axes = plt.subplots(1,2, figsize=(12,5))
sns.barplot(x='Pclass', y='Survived', data=df, palette='summer', ax=axes[0])
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df, palette='summer', ax=axes[1])
plt.tight_layout()




















