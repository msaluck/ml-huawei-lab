import os
# os.getpid() Obtain the current process ID.
print("The absolute path of text.txt is:",os.path.abspath("text.txt")) # The text.txt file is a file in the
# current folder. (In the previous experiment, the current path is changed to C:\, and you need to switch 
# back to the original path.)
# os.path.exists(path): If the file exists, True is returned; if the file does not exist, False is returned. 
print("Whether the text.txt file exists: ",os.path.exists("text.txt"))
# os.path.isdir(path): Check whether the path is a folder.
print("Whether text.txt is a folder:",os.path.isdir("text.txt")) 






