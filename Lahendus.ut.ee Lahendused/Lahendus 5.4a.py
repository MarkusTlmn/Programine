laul = input("Palun sisestage failinimi: ")

fail = open(laul, encoding="UTF-8")

laulud = []
i = 1

print ("Muusikapalade valik: ")
for rida in fail:
    print (str(i) + ". " + rida)
    laulud.append(rida)
    i+=1


fail.close()
laul2 = int(input(" Valige laulu järjekorranumber: "))
print ("Mängitav muusikapala on " + laulud[laul2 -1])