# WAP to enter any character and check if its in lower case or uppercase
name = input("Enter a character :")
if 'A'<name<'Z':
    print("Uppercase")
elif  'a' < name < 'z':
    print("Lowercase")
else:
    print("Not a character")    