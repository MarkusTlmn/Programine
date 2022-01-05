def kuu_nimi(kuunr):
    nimed = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    return(nimed[kuunr-1])
lõpp = 0
def kuupäev_sõnena(kuup):
    tükid = kuup.split(".")
    #lõpp = tükid[0] + ". ", kuu_nimi(int(tükid[1])), tükid[2] + ". a"
    nimi = kuu_nimi(int(tükid[1]))
    lõpp = f'{tükid[0]}. {nimi} {tükid[2]}. a'
    return(lõpp)
    
kuuup = str(input("Siseta kuupäev kujul DD.MM.YYYY: "))

print (kuupäev_sõnena(kuuup))