fil = ["\nbanana\n"
        "apple\n"
        "orange\n"]

with open("newlist.txt", "a") as file:
    file.writelines(fil)
    
   