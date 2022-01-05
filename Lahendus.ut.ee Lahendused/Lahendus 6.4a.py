mitu = int(input("Sisestage külaliste arv:"))
i = 1
def tervitus(arv):
    print('Võõrustaja: "Tere!"')
    print(f'Täna {arv}. kord tervitada, mõtiskleb võõrustaja.')
    print('Külaline: "Tere, suur tänu kutse eest!"')

while i <= mitu:
    tervitus(i)
    i += 1
