import os
for path , dirs , files in os.walk("C:/Users/User/Pictures/Screenshots"):
    print("The current folder is : " +path)
    for dir in dirs:
        print("Subfolder of : "+ " : " + path + dir)
    for file in files:
        print("folder Inside : " + " : " + path + file )
