with open("seek.txt", "w+") as file:
    file.write("This is a test file for seek operation.\n")
    file.seek(0)
    print(file.read())
