# Function syntax: 
re.sub(pattern, repl, string, count=0, flags=0)
# Example: 
import re 
phone = "2019-0101-000 # This is a phone number." 
# Delete the Python comment in the string.
num = re.sub(r'#.*$', "", phone)
print("The phone number is: ", num)
# Delete the hyphens from the phone number.
num = re.sub(r'\D', "", phone) 
print("The phone number is: ", num)



















