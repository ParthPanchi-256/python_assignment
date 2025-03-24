try:
    file = open("simple.txt","r")
    string = file.read()
    print(string)
    file.close()
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not Found.")