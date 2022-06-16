f = open("text.txt", 'w') # Open the text.txt file. If the file does not exist, a new file will be
# created.
print(f.read(6)) # Read six characters and move the cursor six characters backward.
print(f.read()) # Read from the current position of the cursor to the end.
f.close() 




























