#@Author Prathamesh More

openFile = open("Sample.txt","r+")

print(openFile.name)

openFile.write("This is new text")

string = openFile.read()

print(string)

position = openFile.tell()

print("Current position of pointer : ",position)