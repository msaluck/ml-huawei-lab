#Deep Copy and Shallow Copy 
import copy
Dict1 = {'name':'lee', 'age':89, 'num':[1,2,8]} # Create a dictionary
Dict_copy = Dict1.copy() # Shallow cop
Dict_dcopy = copy.deepcopy(Dict1) # Deep copy. 
Dict1['num'][1] = 6 # Change the value of the nested list in the original data.
print('Dict1:'+str(Dict1)+"\n",' Dict_copy:'+ str(Dict_copy)+"\n",' Dict_dcopy:'+ str(Dict_dcopy))

