FILE_PATH = ""
FILE_PATH2 = ""

text = "This is my string\ndsfd"

with open(FILE_PATH, 'w') as f:
    f.write(text)
with open(FILE_PATH, 'r') as file:
     print(file.read())


a = {'Name': 'fds', 'Age': 150}

with open(FILE_PATH2, 'w') as f:
    f.write(str(a))

with open(FILE_PATH2, 'r') as file:
    collection = file.readline()
    print(collection)
    final = eval(collection)
    print(type(final))
