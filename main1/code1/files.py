with open("/home/nishank/notebooks/code/file.txt", "r") as files:
    line1 = files.readlines()
    line2 = files.readlines()
    print(line1)
    '''
    Files cannot be read after reading.
    '''
    print(line2)

'''
File writing
'''
with open("/home/nishank/notebooks/code/file.txt","w") as files:
    files.write("I am good!")

'''
File appending. It appends at the last of file.
'''
with open("/home/nishank/notebooks/code/file.txt","a") as files:
    files.write("\nHow about you!")

'''
R plus mode
'''
