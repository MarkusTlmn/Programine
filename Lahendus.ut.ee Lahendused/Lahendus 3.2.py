ringid = int(input("Sisesta ringide arv: "))
summa = 0
ring = 1
while ring <= ringid:
    # testime, kas ring, kus parasjagu asume, on paaris
    if ring % 2 == 0:
        # kui oli paaris, siis sai porkse
        summa = summa + ring
    ring = ring + 1
    
print (summa)
    