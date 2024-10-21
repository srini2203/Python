with open("newfile.txt","r") as file:
    def showWords():
        lines=file.readlines()
        for line in file:
            words=line.strip().split()
        for word in words:
            if len(word)<3:
                print(word)  
            else:
                print("Not found")      
            