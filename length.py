with open("words.txt","r") as file:
    k=file.read()
    w=k.split()
    for i in w:
        if len(i)>=3:
            print("The words:",i)