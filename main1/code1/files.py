import os
print(os.getcwd())
with open("file.txt", "r") as files:
   for line in files.readlines():
    print(line)

'''
File writing
'''
with open("file.txt","w") as files:
    files.write("I am good!\n")

'''
File appending. It appends at the last of file.
'''
with open("file.txt","a") as files:
    files.write("How about you!")

'''
R plus mode
'''
