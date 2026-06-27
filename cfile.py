import csv
with open("cfile.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["John", 25, "Electrical Engineer"])
    writer.writerow(["Mary", 30, "Financial Analyst"])
    writer.writerow(["David", 22, "Accountant"])
    writer.writerow(["Electrical Engineer", "Financial Analyst", "Accountant"])