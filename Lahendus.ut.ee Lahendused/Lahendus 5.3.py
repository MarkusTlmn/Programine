fail = open("konto.txt", encoding="UTF-8")

raha = []

for rida in fail:

    if float(rida) > 0:
        print(rida)

fail.close()