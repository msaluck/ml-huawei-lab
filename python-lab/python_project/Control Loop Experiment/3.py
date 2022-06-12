def fibs(num): # Position parameter. 
    result = [0,1]# Create a list to store the sequence value. 
    for i in range(2,num): # Cycle num-2 times.
        a = result[i-1] + result[i-2]
        result.append(a) # Append the value to the list. 

    return result # Return the list.
fibs(5)


