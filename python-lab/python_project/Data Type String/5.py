#Data Type: Dictionary
# Three value assignment operations on dictionaries.
x = {'food':'Spam','quantity':4,'color':'pink'}
X =dict(food='Spam',quantity=4, color='pink')
x = dict([("food", "Spam"),("quantity", "4"),("color","pink")])
# dict.copy(): Copy data. 
d =x.copy()
d['color'] = 'red'
print(x) # {'food':'Spam','quantity':4,'color':'pink'}
print(d) # {'food':'Spam','quantity':4,'color':'red'} 
# Element access.
print (d ['name']) # Obtain the error information.
print(d.get('name')) # Output: None 
print(d.get('name','The key value does not exist.')) # Output: The key value does not exist.
print(d.keys()) # Output: dict_keys(['food', 'quantity', 'color'])
print(d.values()) # Output: dict_values(['Spam', 4, 'red']) 
print(d.items())
# Output: dict_items([('food', 'Spam'), ('quantity', 4), ('color', 'red')]) 
d.clear() # Clear all data in the dictionary.
print(d) # Output: {}
del(d) # Delete the dictionary.
print(d) # The program is abnormal, and a message is displayed,indicating that d is not defined.
