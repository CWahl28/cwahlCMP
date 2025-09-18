thing = input("Enter a string: ")
char = input("Enter a letter to remove: ")
new_thi = ""

for i in thing:
    if(i != char):
        new_thi += i 

print(str(new_thi))

