kuu = input("Sisestage kuu: ")
päev = int(input("Sisestage päev: "))

from urllib.request import urlopen
vastus = urlopen("https://kodu.ut.ee/~eno/mooc/"+ str(kuu))

vastusBaitidena = vastus.read()
vastusSõnena = vastusBaitidena.decode()
järjend = vastusSõnena.splitlines()

i = 0
while i < päev:
    i += 1
    
print(järjend[i])