fail = input("Sisestage failinimi: ")
from datetime import *
fail1 = open(fail, encoding="UTF-8")

nimed = []

for rida in fail1:
    nimed.append((rida))

nimi = nimed[datetime.now().day-1]

print ("Vastama tuleb: " + (nimi))