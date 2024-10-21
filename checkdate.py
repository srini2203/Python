def checkDate(date):
    dd,mm,yyyy=date.split("/")
    if 0<int(dd)<=31 and 0<int(mm)<=12 and 0<int(yyyy):
        print("It is a valid date")
    else:
        print("The date is not valid")    

date=str(input("Enter date in dd/mm/yyyy format:"))
checkDate(date)