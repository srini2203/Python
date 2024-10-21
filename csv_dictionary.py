import csv
with open ("dan.csv","w") as file:
    fieldnames={"player_name","rating"}
    writer=csv.DictWriter(file,filednames=fieldnames)
    writer.header()
    writer.writerow({"player_name":"James","rating":92})
    
