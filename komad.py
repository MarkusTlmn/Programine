fail = open("vigane.txt", "r", encoding="UTF-8")
def vigane(vigad):
    lause = vigad.replace(" et" , ", et")
    return(lause)
with open("parandatud.txt", "a") as f2:
    for rida in fail:
        f2.write(vigane(rida))
    f2.close()
    