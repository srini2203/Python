with open("fruit.txt","a") as file:
    L=[]
    for i in range(5):
        x=input("Enter names of five fruits")
        L.append(x)
    file.writelines(L)    
