import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:


# Print out the plaform from sys:
for arguments in sys.argv: 
    print(arguments)

# Print out the Python version from sys:
print("python version",sys.version)



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("PROCESS ID BELOW: ")
process = os.getpid()
print(process)


# Print the current working directory (cwd):
cwd = os.getcwd()
print("cwd is..",cwd)

# Print your login name
user = os.getlogin(); 
print(user)

