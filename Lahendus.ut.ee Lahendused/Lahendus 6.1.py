tekst = int(input("Mitu korda soovite reklaamlauset kuvada?"))
tekst2 = input("Sisestage reklaamlause: ")

def banner(tekst2):
    return tekst2.upper()
  
loendur = tekst
while loendur > 0:
    print (banner(tekst2))
    loendur -= 1
    