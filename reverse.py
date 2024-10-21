def reverseList(l):
    l=l[::-1]
    print(l)

l=[]
n=int(input("Enter no. of elements:"))
for i in range(n):
    num=int(input("Enter number{}:".format(i+1)))
    l.append(num)
reverseList(l)    


    

