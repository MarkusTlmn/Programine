ruut = int(input("Sisestage täisarv: "))
ruute = ruut
arv = 1
if ruute == 1:
     print ("nisuteri 1 " " ruudu eest: 1 ")
while ruute > 1:
    arv = arv * 2
    ruute = ruute - 1
    if ruute == 1:
     print ("nisuteri " + str(ruut) + " ruudu eest: " + str(arv))