# read file
tekstBestand = open("addresslist.txt", "r")
# opens the file to copy to
kopieBestand = open("copy_addresslist.txt", "w")

# loop checks if line is empty
empty = False
while (not empty):
    tabelRegel = tekstBestand.readline()
    # if line is empty, stop loop
    if (tabelRegel == ""):
        empty = True
    # if line is not empty, write to copy file
    else:
        kopieBestand.write(tabelRegel)

kopieBestand.close()
