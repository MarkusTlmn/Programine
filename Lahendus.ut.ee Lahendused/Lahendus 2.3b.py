isevmitte = input("Kas soovite istekohta ise valida (ise) või loosida (loos): ")

from random import randint
arv_1 = randint(1, 3)
if isevmitte == "loos" and (arv_1 == 1):
    print ("Istekoht loositi. Aknakoht")
elif isevmitte == "loos" and (arv_1 == 2 or arv_1 == 3):
    print ("Istekoht loositi. Vahekäigukoht")
elif isevmitte == "ise" :
    istekoht = input("Kas soovite istuda akna ääres (aken) või mitte (muu): ")
    print ("Valisite ise. Aknakoht, Vahekäigukoht")
elif istekoht == "muu":
    print ("Valisite ise. Vahekäigukoht")

