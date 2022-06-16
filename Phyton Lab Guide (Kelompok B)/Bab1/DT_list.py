animals = ['cat', 'dog', 'monkey']
# list.append(obj): Add a new object to the end of the list.
# Append an element.
animals.append("fish")
print(animals)
# Output: ['cat', 'dog', 'monkey', ‘fish’]
# list.remove(obj): Remove the first match for a value in the list.
# Delete element fish.
animals.remove("fish")
print(animals)
# Output: ['cat', 'dog', 'monkey']
# list.insert(index, obj): Insert a specified object to a specified position in the list. The index indicates
#the position.
# Insert element fish at subscript 1.
animals.insert(1,"fish")
print(animals)
# Output: ['cat', ‘fish’, 'dog', 'monkey']
# list.pop([index=-1]): Remove the element (the last element by default) corresponding to the
#subscript in the list. The index indicates the subscript.
# Delete the element whose subscript is 1.
animals.pop(1)
print(animals)
# Output: ['cat', 'dog', 'monkey']
# Traverse and obtain the elements and indexes.
# enumerate(sequence): Return an index sequence consisting of a data object that can be traversed
#and list the data and subscripts. This function is usually used in the for loop.
# Index consisting of the element subscript and element
h=enumerate(animals)
print(list(h))
#Output: (0, cat)
# (1, dog)
# (2, monkey)
# List derivation.
# Generate a list of elements that comply with rules in batches.
H=[]
for i in range(len(animals)):
    H.append(animals[i]*2)
print(H)
#['catcat ', 'dogdog ', 'monkeymonkey ']
# list.sort(cmp=None, key=None, reverse=False): The cmp parameter is an optional parameter. If this
#parameter is specified, the method uses this parameter is used for sorting. Key is an element used for
#comparison. reverse indicates the sorting rule, and False indicates the ascending order.
# Sort the list.
N=["31", "12", "55", "45"]
N.sort()
print(N)
# Output: [12,32,45,55]
# list.reverse(): Element in the reverse list.
# Reverse the list.
N.sort(reverse=True)
print(N)
# Output: [55,45,32,12]