number=int(input("Number of students:"))
list=[]
temp=[]
result=[]
for i in range(number):
    name=input()
    score=int(input())
    list.append([name,score])
    temp.append([score])
temp=list(set(temp))
temp.sort()
second_least_value=temp[1]
for i in range(len(list)):
    if(list[i][1]==second_least_value):
        result.append[i][0]=second_least_value
print(result)

