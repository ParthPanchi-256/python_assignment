a= input("Enter the student's name: ")
dict = {}
if len(a.strip()) != 0:
    b = int(input(f"{a}'s marks: "))
    dict[a.strip()]=b
else:
    print("Student not found.")
