
n=int(input("Enter number of students:"))
list=[]
scores=[]
secondlowest=[]
for i in range(n):
    name=(input("Enter the name of student:"))
    score=int(input("Enter the score of student:"))
    list.append(name,score)
for i in range(len(list)):
    scores=list(set(scores))
    scores.sort()
    print(scores)
    secondlowest=scores[1]
    print(secondlowest)
for i in range(len(list)):
    if(list[i][1])==secondlowest:
        secondlowest.append(list[i][1])
    

       
