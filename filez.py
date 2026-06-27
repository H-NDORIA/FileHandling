import csv

with open("filex.csv", "r", newline = "") as file:
          reader = csv.reader(file)
          for row in reader:
                print(row)