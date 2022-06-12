# Function syntax: 
re.match(pattern, string, flags=0)
# Example: 
import re
print(re.match('www', 'www.huawei.com').span())  # Match at the start position.
print(re.match('com', 'www.huawei.com')) # Not match at the start position.





























