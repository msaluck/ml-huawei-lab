# Assign value "python" to variable S.
S='python'
# str.split(str="", num=-1): The string is split by separator. If the num parameter has a value, divide the string into num+1 substrings. The value -1 indicates that all strings are split.
Ss= S.split("h",-1)
# The output is ['pyt','on']. The string is split by h.
print(Ss)
# str.replace(old, new[, max]): A string generated after the old string is replaced with the new string is returned. If the third parameter max is specified, the number of times that the old string is replaced with the new string cannot exceed the value of max.
Us=S.replace("python","PYthon")
print(Us)
# In the string, py is replaced with PY.
# str.upper(): Return the value after lowercase letters are converted to uppercase letters.
print(S.upper())
# PYTHON
# str.lower(): Return the value after uppercase letters are converted to lowercase letters.
print(S.lower())
# The output is python because all uppercase letters are converted to lowercase letters.
# \n is a newline character.
# str.join(sequence): sequence indicates a sequence to be joined. In the output, the new string generated after the elements in the specified character join sequence is returned.
# The output is life is short. The join function is used for concatenating strings.
# Format the string.
T=("hello","world","12")
text=" ".join(T)
print(text)
# Output: hello world 12
