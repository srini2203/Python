def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return f    

def spl(n):
    for i in range(1,n+1):
        k=n
        s=0
        while n!=0:
            a=n%10
            s=s+fact(a)
            n=n//10
        if(k==s):
            print(n,end='')
        
            
n=int(input())
spl(n)