def pronksikarva_summa(jr):
    kokku  =0
    for rida in jr:
        if rida <6:
            kokku += rida
    return(kokku)



failn = input("Sisestage faili nimi: ")
fail = open(failn)
j = []
for r in fail:
    j.append(int(r))
fail.close()

print (pronksikarva_summa(j))


