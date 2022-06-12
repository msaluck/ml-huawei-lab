#1.1.4 Data Type: List
animals = ['cat', 'dog', 'monkey']
# list.append(obj): Add a new object to the end of the list.
animals.append ('fish') # Append an element.
print(animals) # Output: ['cat', 'dog', 'monkey', 'fish']
# list.remove(obj): Remove the first match for a value in the list. 
animals.remove ('fish') # Delete element fish.
print(animals) # Output: ['cat', 'dog', 'monkey']
# list.insert(index, obj): Insert a specified object to a specified position in the list. The index indicates the position. 
animals.insert (1, 'fish') # Insert element fish at subscript 1. 
print(animals) # Output: ['cat', 'fish', 'dog', 'monkey']
# list.pop([index=-1]): Remove the element (the last element by default) corresponding to the subscript in the list. The index indicates the subscript.
animals.pop(1) # Delete the element whose subscript is 1.
print(animals) # Output: ['cat', 'dog', 'monkey']
# Traverse and obtain the elements and indexes.
# enumerate(sequence): Return an index sequence consisting of a data object that can be traversed and list the data and subscripts. This function is usually used in the for loop.
for i in enumerate(animals):
print(i) # Index consisting of the element subscript and element
Output: (0, cat) 
(1, dog)
(2, monkey)
# List derivation.
squares = [x*2 for x in animals] # Generate a list of elements that comply with rules in batches.
print(squares) #['catcat ', 'dogdog ', 'monkeymonkey ']
list1 = [12,45,32,55] 
# list.sort(cmp=None, key=None, reverse=False): The cmp parameter is an optional parameter. If this parameter is specified, the method uses this parameter is used for sorting. Key is an element used for comparison. reverse indicates the sorting rule, and False indicates the ascending order.
list1.sort() # Sort the list. 
print(list1) # Output: [12,32,45,55]
# list.reverse(): Element in the reverse list.
list1.reverse() # Reverse the list.
print(list1) # Output: [55,45,32,12]