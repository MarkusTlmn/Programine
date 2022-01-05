fail1 = input("Sisestage faili nimi: ")

fail = open(fail1, encoding = "UTF-8")

nimed = []

for line in fail:
    nimed.append(str(line.strip()))
   
fail.close()
i = 0
tuleb = 0
kutsutud = 0
while i < len(nimed):
    if "+" in nimed[i].strip():
        tuleb = tuleb + 1
        kutsutud = kutsutud + 1
        i = i + 1
    else:
        kutsutud = kutsutud + 1
        i = i + 1
print( str(tuleb) + " Inimest tuleb")
print("Kutsutud on " + str(kutsutud) + " inimest")

def eelarve(kogus):
    hind = kogus * 10 + 55
    return hind
print("Maksimaalne eelvarve: " + str(eelarve(kutsutud)))
print("Minimaalne eelarve: " + str(eelarve(tuleb)))
        
