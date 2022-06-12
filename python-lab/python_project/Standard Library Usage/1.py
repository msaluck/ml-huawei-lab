import os
# os.getpid() Obtain the current process ID.
print("ID of the current process:", os.getpid())
# os.getppid(): Obtain the ID of the current parent process.
print(" ID of the current parent process:", os.getppid())
# os.getcwd(): Obtain the current path.
cwd = os.getcwd()
print(" The current path is:",cwd)
# os.chdir(path): Change the current working directory.
os.chdir("C:\\") 
print("The modified path is:", os.getcwd())
# os.listdir(): Return all files in the directory.
print("Files in the current directory:", os.listdir(cwd))
# os.walk(): Export all files in the current path.
for root, dirs, files in os.walk(cwd, topdown=False):
    for name in files: 
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))





