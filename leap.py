year=float(input())
def isleap(year):
    if(year%4==0 and year%400==0):
        print("Leap year")
    elif(year%100==0):
        print("Not a leap year")


isleap(year)  
