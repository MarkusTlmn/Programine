t_arv = int(input("Täringute arv: "))
from random import randint
arv2 = 0
while t_arv > arv2:
    if arv2 >= 0:
        suvaline_arv = randint(1,6)
        print (suvaline_arv)
        arv2 = arv2 + 1