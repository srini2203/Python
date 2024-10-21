import csv

def Search(register_number,filename="File1.cv"):
    try:

        with open("File1.csv","r",newline="") as file:
            reader=csv.DictReader(file)
            for row in file:
                if row["Reg_No"]==register_number:
                    return row
                else:
                    return None
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error occured")
def main():
    # Ask the user for the register number
    register_number = input("Enter the register number to search for: ")
    
    # Search for the record in the CSV file
    record = search_record(register_number)
    
    if record:
        print("Record found:")
        print(f"Reg_no: {record['Reg_no']}")
        print(f"Name: {record['Name']}")
        print(f"Year: {record['Year']}")
        print(f"Section: {record['Section']}")
        print(f"Tot_marks: {record['Tot_marks']}")
    else:
        print("No record found with the given register number.")

if __name__ == "__main__":
    main()            

            