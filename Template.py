# User Input and Replace String Template “Hello << UserName >>, How are you?”

name = input("Enter Your Name : ")

name = str(name)
nameLength = len(name)
if nameLength >= 3:
    print("Hello", name, "How are you")
else:
    print("Name should Min 3 char it is only ",nameLength,"Char")