import csv


with open("input.csv", "w", newline="") as file:
    csw = csv.writer(file)
    
    csw.writerow(["Reg_no", "Name", "Year", "Section", "Total"])
    
    Reg_no = int(input("Enter your register number: "))
    Name = input("Enter your name: ")
    Year = int(input("Enter the year you were born: "))
    Section = input("Enter your section: ")
    total = int(input("Enter total marks: "))
    csw.writerow([Reg_no, Name, Year, Section, total])


with open("input.csv", "r") as file:
    csr = csv.reader(file)
    header = next(csr) 
    found = False
    for row in csr:
        if int(row[0]) == Reg_no:  
            print(f"Name: {row[1]}")
            print(f"Year: {row[2]}")
            print(f"Section: {row[3]}")
            print(f"Total Marks: {row[4]}")
            found = True
            break
    if not found:
        print("Not in list")
