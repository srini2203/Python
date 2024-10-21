n=int(input("Enter number of elements:"))
list=[]
for i in range(n):
    e=int(input("Enter the element:"))
    list.append(e)
i=int(input("Enter the index:"))
e=int(input("Enter the integer:"))
list.insert(i,e)
print(list)
e=int(input("Enter element to remove:"))
list.remove(e)
print("After removing element:",list)
e=int(input("Enter elemen to be inserted:"))
list.append(e)
print("After inserting:",list)
list.sort()


