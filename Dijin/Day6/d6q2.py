n=int(input("Enter length of list: "))
l=[]
for i in range(n):
    a=int(input("Enter the element of list: "))
    l.append(a)
l.sort()
print(l[1])
