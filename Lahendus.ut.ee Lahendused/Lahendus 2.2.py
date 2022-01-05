punkti_summa = float(input("Palun sisesta punktisumma: "))
if punkti_summa < 0:
    print ("Vigane punktisumma")
elif punkti_summa > 100:
    print ("Vigane punktisumma")
elif punkti_summa < 66:
    print ("Vähem kui kandideerimiseks vajalik")
elif punkti_summa < 85:
    print ("Kandideerimine vastuvõtule")
elif punkti_summa > 84.9:
    print ("Vastuvõtt tagatud")