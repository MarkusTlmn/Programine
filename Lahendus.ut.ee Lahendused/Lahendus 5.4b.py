fail = open("sisseränne.txt", encoding="UTF-8")

sisse = []

for rida in fail:

    sisse.append(int(rida))

fail.close()
fail = open("väljaränne.txt", encoding="UTF-8")

valja = []

for rida in fail:

    valja.append(int(rida))

fail.close()

saldod = []

for i in range(len(sisse)):
    saldod.append(sisse[i]-valja[i])

print(saldod)
sal = max(saldod)
if sal > 0:
    print ("Suurim postiivne rändesaldo oli " + str(saldod.index(sal)+1) + (". aastal"))
else:
    print ("Positiivse rändesaldoga aastaid ei ole.")

    