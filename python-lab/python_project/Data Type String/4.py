#Data Type: Tuple
T=(1,2,3) # Create a tuple.
print(T+(4,5)) #Tuples are combined. The output is (1, 2, 3, 4, 5).
t=(42,) # A tuple with only one element, which is different from a number.
tuple1 = (12,45,32,55,[1,0,3]) # Create a tuple. 
tuple1 = (12,45,32,55,[1,0,3]) # Create a tuple. 
tuple1[0] = "good" # The program is abnormal, and the tuple is unchangeable. 
tuple1[4][0] = 2 # Elements that can be changed in a tuple are changeable.
print(tuple1) # (12,45,32,55,[2,0,3])