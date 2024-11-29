x=input("enter the character")

for i in range(65,122):
    if chr(i)==x:
        print(x,"is an alphabet")
        x=1

if x!=1:
    print("not")
