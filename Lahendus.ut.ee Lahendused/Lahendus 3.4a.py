ringid = int(input("Sisesta ringide arv: "))
summa = 0
ring = 0
rings = 1
while rings <= ringid:
    ring = rings * (rings + 1)/2
    rings = rings + 1
    summa = summa + ring
    summa = round(summa)
print (summa)