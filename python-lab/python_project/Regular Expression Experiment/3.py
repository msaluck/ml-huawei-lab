# Function syntax: 
re.compile(pattern[, flags])
# Example: 
import re 
pattern = re.compile(r'\d+') # At least one digit is matched.  
n = pattern.match('one12twothree34four') # The header is not found.
print(n)
m = pattern.search('one12twothree34four') # Match from the position of 'e'. No match is found.
print(m)
print(m.group())



















