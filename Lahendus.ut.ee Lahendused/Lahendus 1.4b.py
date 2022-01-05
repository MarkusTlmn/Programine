nimi = (input("Sisestage oma nimi: "))
lubatud = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik = int(input("Sisestage tegelik kiirus (km/h): "))
vastus = tegelik - lubatud
vastus = vastus * 3
vastus = min(190, vastus)
viimane_vastus = nimi + ", kiiruse ületamise eest on teile trahv " + str(vastus) + " eurot"
print (viimane_vastus)
