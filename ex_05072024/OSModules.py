#Interact with the Operating Systems
import os
import time

#Get the current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

#posix --> For unix based systems --> MAC
#nt ---> windows based system
print(os.name)

#Changing the directory path from one folder to another
os.chdir("D:\\Evening6To7\\Python_Learning\\pythonProject\\ex_01072024")

print(os.getcwd())

#Listing the directories in the given folder
print(os.listdir("D:\\Evening6To7\\Python_Learning\\pythonProject"))

#Creating the missing directories
try:
    os.mkdir("test")
except FileExistsError:
    print("Directory already exists")

#Prints the size of the file in the form of bytes
size=os.path.getsize('AbstractMethods.py')
print(size)

if size>0:
    print("File is not empty and has content")

else:
    print("File is empty, so no content is there")

#Prints the last modified time ---> UTC Date time format
print(os.path.getmtime('AbstractMethods.py'))

#Prints the last modified date time in a readable manner
print(time.gmtime(os.path.getmtime('AbstractMethods.py')))