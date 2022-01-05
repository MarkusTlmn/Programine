poisid = int(input("Mitu pöialpoissi tahab õunu? "))
from random import randint
if poisid == 0:
   print ("Lumivalgekesele jäänud õunte arv 14" )
summa = 1
õunad = 14
while poisid > 0:
    suvaline_arv = randint(1,2)
    print (suvaline_arv)
    poisid = poisid - 1
    õunad = õunad - suvaline_arv
    summa = õunad
    if poisid == 0:
        print ("Lumivalgekesele jäänud õunte arv " + str(summa))