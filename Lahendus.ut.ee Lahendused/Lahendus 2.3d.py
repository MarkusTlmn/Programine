kirja_suurus = float(input("Sisestage kirja suurus: "))
kirja_teema = (input("Sisestahe kirja teema pealkiri: "))
fail = input("Kas kirjaga on kaasas fail? ")
if kirja_suurus > 1.01 and fail == "jah":
    print ("Kiri on spämm")
elif kirja_teema == "":
    print ("Kiri on spämm")
elif kirja_suurus < 1 and fail == "ei":
    print ("Kiri ei ole spämm")
else:
    print ("Kiri ei ole spämm")
