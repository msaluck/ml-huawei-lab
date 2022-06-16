# Three value assignment operations on dictionaries.
# dict.copy(): Copy data.
d={'food':'Spam','quantity':4,'color':'pink'}
e=d.copy()
e["color"]="red"
print(d)
print(e)
# {'food':'Spam','quantity':4,'color':'pink'}
# {'food':'Spam','quantity':4,'color':'red'}
# Element access.
# Obtain the error information.
#e["rasa"]

# Output: None
print(e.get("rasa"))
# Output: The key value does not exist.
if e.get('rasa') is None:
    print("The key value does not exist.")
# Output: dict_keys(['food', 'quantity', 'color'])
print(e.keys())
# Output: dict_values(['Spam', 4, 'red'])
print(e.values())
# Output: dict_items([('food', 'Spam'), ('quantity', 4), ('color', 'red')])
print(e.items())
# Clear all data in the dictionary.
e.clear()
print(e)
# Output: {}
# Delete the dictionary.
# The program is abnormal, and a message is displayed, indicating that d is not defined.