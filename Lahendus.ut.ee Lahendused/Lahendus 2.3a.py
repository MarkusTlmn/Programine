vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ")
treening = int(input("Sisestage treening tüüp: "))
if treening == 1 and (sugu == "m" or sugu == "M"):
    vastus_1 = vanus 
    vastus_1 = 220 - vastus_1
    vastus_1 = vastus_1 * 0.50
    vastus_1 = round(vastus_1)
    vastus_2 = vanus 
    vastus_2 = 220 - vastus_2
    vastus_2 = vastus_2 * 0.70
    vastus_2 = round(vastus_2)
    print (str(vastus_1) + " kuni " + str(vastus_2))
elif treening == 2 and (sugu == "m" or sugu == "M"):
    vastus_1 = vanus 
    vastus_1 = 220 - vastus_1
    vastus_1 = vastus_1 * 0.70
    vastus_1 = round(vastus_1)
    vastus_2 = vanus 
    vastus_2 = 220 - vastus_2
    vastus_2 = vastus_2 * 0.80
    vastus_2 = round(vastus_2)
    print (str(vastus_1) + " kuni " + str(vastus_2))
elif treening == 3 and (sugu == "m" or sugu == "M"):
    vastus_1 = vanus 
    vastus_1 = 220 - vastus_1
    vastus_1 = vastus_1 * 0.80
    vastus_1 = round(vastus_1)
    vastus_2 = vanus 
    vastus_2 = 220 - vastus_2
    vastus_2 = vastus_2 * 0.87
    vastus_2 = round(vastus_2)
    print (str(vastus_1) + " kuni " + str(vastus_2))
elif treening == 1 and (sugu == "n" or sugu == "N"):
    vastus_1 = vanus * 0.88
    vastus_1 = 206 - vastus_1
    vastus_1 = vastus_1 * 0.50
    vastus_1 = round(vastus_1)
    vastus_2 = vanus * 0.88
    vastus_2 = 206 - vastus_2
    vastus_2 = vastus_2 * 0.70
    vastus_2 = round(vastus_2)
    print (str(vastus_1) + " kuni " + str(vastus_2))
elif treening == 2 and (sugu == "n" or sugu == "N"):
    vastus_1 = vanus * 0.88 
    vastus_1 = 206 - vastus_1
    vastus_1 = vastus_1 * 0.70
    vastus_1 = round(vastus_1)
    vastus_2 = vanus * 0.88
    vastus_2 = 206 - vastus_2
    vastus_2 = vastus_2 * 0.80
    vastus_2 = round(vastus_2)
    print (str(vastus_1) + " kuni " + str(vastus_2))
elif treening == 3 and (sugu == "n" or sugu == "N"):
    vastus_1 = vanus * 0.88 
    vastus_1 = 206 - vastus_1
    vastus_1 = vastus_1 * 0.80
    vastus_1 = round(vastus_1)
    vastus_2 = vanus * 0.88
    vastus_2 = 206 - vastus_2
    vastus_2 = vastus_2 * 0.87
    vastus_2 = round(vastus_2)
    print (str(vastus_1) + " kuni " + str(vastus_2))
if sugu == "m" or "M" or "N" or "n":
    print
else:
    print ("See sisend ei sobi")
if treening == "1" or "2" or "3":
    print
else:
    print ("See sisend ei sobi")