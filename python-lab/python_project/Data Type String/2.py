#Step 3Common operations on strings:
S = "python" # Assign value "python" to variable S.
# str.split(str="", num=-1): The string is split by separator. If the num parameter has a value, divide the string into num+1 substrings. The value -1 indicates that all strings are split.
print(S.split('h')) # The output is ['pyt','on']. The string is split by h.
# str.replace(old, new[, max]): A string generated after the old string is replaced with the new string is returned. If the third parameter max is specified, the number of times that the old string is replaced with the new string cannot exceed the value of max.
print(S.replace('py','PY')) # In the string, py is replaced with PY.
# str.upper(): Return the value after lowercase letters are converted to uppercase letters.
print(S.upper()) # PYTHON
# str.lower(): Return the value after uppercase letters are converted to lowercase letters.
print ('PYTHON'.lower()) # The output is python because all uppercase letters
line= 'aa,bb,ccc,dd\n' # \n is a newline character.
# str.join(sequence): sequence indicates a sequence to be joined. In the output, the new stringgenerated after the elements in the specified character join sequence is returned. 
print (' '.join([' life ',' is ',' short '])) # The output is life is short. The join function is used for concatenating strings.
hw12= '%s %s %d' % ('hello', 'world', 12) # Format the string.
print(hw12) # Output: hello world 12
