aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
ab = 0
fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
while aasta > 2011:
     aasta = aasta - 1
     ab = ab + 1
fail.close()
print (vastuvõetud[ab])