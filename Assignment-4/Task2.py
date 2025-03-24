a = input("Enter text to write to file: ")
print("Data successfully written to output.txt")
try:
    fp = open("output.txt","+a")
    fp.write(a+"\n")
    b = input("Enter additional text to append: ")
    fp.write(b)
    print("Data successfully written to output.txt")
    fp.seek(0)
    a = fp.read()
    print("Final content of output.txt:")
    print(a)
except Exception:
    print(Exception.__name__)