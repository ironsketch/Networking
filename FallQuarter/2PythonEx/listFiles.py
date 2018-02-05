import os

# Getting user input
repeating = False
while not repeating:
    dir = raw_input("(For current directory just hit ENTER)\nIf unsure of where you are just type pwd to get location.\nType the directory to list files in it then hit ENTER: ")
    # Editing input
    if dir == "pwd":
        print("")
        print os.getcwd()
        print("")
    elif len(dir) > 0 and dir != ".":
        if dir[0] != "/":
            dir = "/" + dir
    else:
        dir = "."

    if os.path.isdir(dir):
        repeating = True
    elif dir != "pwd":
        print("")
        print("Not a valid address. Try the FULL path.")

# Iterate through files etc. and print them
pathList = os.listdir(dir)
for file in pathList:
    if os.path.isfile(file):
        print file
print ("")
