def isTriangle(a,b,c):
    if (a+b<=c) or (b+c<=a) or (c+a<=b):
        return False
    else:
        return True
    
def checkTriangle(a,b,c):
    if isTriangle(a,b,c):
        if(a==b):
            if(b==c):
                print("Equilateral triangle")
            else:
                print("Isoceles triangle")
        else:
            print("Scalene triangle")
    else:
        print("Not a triangle")                    


a=int(input("Enter side A:"))
b=int(input("Enter side B:"))
c=int(input("Enter side C:"))
checkTriangle(a,b,c)