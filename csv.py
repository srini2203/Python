import csv


mylist = [["ABC", 65, 70, "DEF"], ["GHI", 75, 80, "JKL"]]
with open("File1.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(mylist)


with open("File1.csv", "r") as fp:
    rp = csv.reader(fp)
    for r in rp:
        print(r)
