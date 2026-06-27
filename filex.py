import csv
with open("cfile.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Alice", 28, "Software Engineer"])
    writer.writerow(["Bob", 32, "Financial Economist\n"])
    writer.writerow(["Haylee", 29, "Financial Engineer"])