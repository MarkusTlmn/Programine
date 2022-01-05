sissekanne = input("Sisesta sissekande tekst: ")
from datetime import datetime
kuupäev_kellaeg = datetime.today()
f = open("paevik.txt", "a")
f.write(str(kuupäev_kellaeg))
f.write(sissekanne)
f.close()