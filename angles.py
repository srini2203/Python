def checkAngles(a1,a2,a3):
    if a1!=0 and a2!=0 and a3!=0 and a1+a2+a3==180:
        print("triangle is valid")
    else:
        print("triangle is not valid")    

a1=int(input("Enter degree of angle1:"))
a2=int(input("Enter of degree of angle2:"))
a3=int(input("Enter degree of angle3:"))
checkAngles(a1,a2,a3)