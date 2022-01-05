failnimi = input("Sisestage faili nimi: ")
fail = open (failnimi, "r", encoding = "UTF-8")

for line in fail:
    line = line.replace("ä", "AE")
    line = line.replace("Ä", "AE")
    line = line.replace("Ö", "OE")
    line = line.replace("ö", "OE")
    line = line.replace("Õ", "OE")
    line = line.replace("õ", "OE")
    line = line.replace("ü", "UE")
    line = line.replace("Ü", "UE")
    print (line.upper(), end="")
    