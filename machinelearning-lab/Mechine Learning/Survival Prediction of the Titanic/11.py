plt.figure(figsize=(15,4))
plt.scatter(df['Fare'], df['Pclass'], color='yellow', edgecolors='k', label='Price Paid by Passenger')
plt.xlabel('Price')
plt.ylabel('Passenger Class')
plt.title('Price for Each Class')
plt.legend()
plt.show()













