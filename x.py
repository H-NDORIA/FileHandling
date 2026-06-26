with open("text.txt", "w+") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("It contains multiple lines of text.\n")
    file.seek(0)
    print(file.read())
    