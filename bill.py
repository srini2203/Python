bill_amnt=int(input("Enter the bill amount:"))
n=int(input("Enter number of friends:"))
total_tip=int(input("Enter the tip to be given:"))
tip_per_person=total_tip//n
amnt_per_person=(bill_amnt//n)+tip_per_person
print("Amount to be paid:",amnt_per_person)

