vastus = 0
from easygui import *
esimene = integerbox("Sisestage esimene täisarv lõigus 1-10:", lowerbound = 1, upperbound = 10)
teine = integerbox("Sisestage teine täisarv lõigus 1-10", lowerbound = 1, upperbound = 10)
nupud = ["+","-","*"]
tehe = buttonbox("Valige tehe:", choices = nupud)
vastus = eval(str(esimene) + tehe + str(teine))
msgbox("tehte tulemus on " + str22(vastus) + ".")