class Person:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
    
    def display(self):
        print(f"ID: {self.id}, NAME: {self.name}, ADDRESS: {self.address}")

class Employee(Person):
    def __init__(self, salary, job, deptID, deptName, id, name, address):
        
        super().__init__(id, name, address)
    
        self.salary = salary
        self.job = job
        self.deptID = deptID
        self.deptName = deptName
    
    def display(self):
        
        super().display()
        
        print(f"SALARY: {self.salary}, JOB: {self.job}, DEPT ID: {self.deptID}, DEPT NAME: {self.deptName}")


def main():
    n = int(input("Enter the number of employees: "))
    employees = []

    for i in range(n):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        salary = float(input("Enter Salary: "))
        job = input("Enter Job: ")
        deptID = int(input("Enter Department ID: "))
        deptName = input("Enter Department Name: ")

        
        employees.append(Employee(salary, job, deptID, deptName, id, name, address))     ##Employee object is created using constructor
    
    
    for emp in employees:
        emp.display()


if __name__ == "__main__":
    main()
