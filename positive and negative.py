def customSum(first,last):
    sum=0
    for i in range(first,last+1):
        sum=sum+l[i]
    return sum   
def customAvg(sum,number):
    return sum/number
l=[]
pos_count,neg_count,zero_count,n=0,0,0,0
q=int(input("Enter the total number:"))
for i in range(0,q):
    num=int(input("Enter the value of number{}:".format(i+1)))
    l.append(num)
l.sort(num)
print("The sorted numbers are:",l)
while n<len(l):
    if l[n]>0:
        pos_count+=1
    elif l[n]==0:
        zero_count+=1
    else:
        neg_count+=1
        n+=1
print("No. of positive nos.",pos_count,"/n","No. of negative nos.",neg_count,"/n","No. of zero nos.",zero_count,"/n")
neg_last_posn=neg_count-1                 #neg_count stores no. of neegativenos. and subtracting one from it gives us index of last no. as index goes from 0...n
zero_last_posn=neg_last_posn+zero_count   #this gives us index of last zero after negative nos.
pos_sum=customSum(zero_last_posn+1,len(l)-1)
neg_sum=customSum(0,neg_last_posn)
pos_avg=customAvg(pos_sum,pos_count)
neg_avg=customAvg(neg_sum,neg_count)
print("Sum of positive nos.=",pos_count,"Avg. of positive nos.=",neg_count)
print("Sum of negative nos.",neg_count,"Avg. of negative nos.=",neg_avg)    
        
    




