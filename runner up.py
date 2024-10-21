n=int(input("Enter number of elements in list:"))
num_list=[]
for i in range(n):
    x=int(input("Enter numbers to be input in list:"))
    num_list.append(x)
num_list.sort()
max_number=max(num_list)
while max_number in num_list:
    num_list.remove(max_number)
second_largest=max(num_list)
print(second_largest)

