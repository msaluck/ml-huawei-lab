sample_set = {'Prince', 'Techs'}
# The output is False. in is used to check whether an element exists in the set.
print("Data" in sample_set)
# set.add(obj): Add an element to a set. If the element to be added already exists in the set, no operation is performed.
# Add element Data to the set.
sample_set.add("Data")
print(sample_set)
# Output: {'Prince', 'Techs', 'Data'}
print(len(sample_set))
# Output: 3
# set.remove(obj): Remove a specified element from a set.
# Delete element Data.
sample_set.remove("Data")
print(sample_set)
# {'Prince', 'Techs'}
list2 = [1,3,1,5,3]
# The output is [1,3,5]. The uniqueness of the set elements is used to deduplicate the list.
print(list(set(list2)))
# Invariable set.