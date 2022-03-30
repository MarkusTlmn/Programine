def barboraotsing():

    from urllib.request import urlopen
    import re
    import sqlite3
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException

    vastus = urlopen("https://www.barbora.ee/toode/kiirnuudlid-kanalihamaits-rollton-85-g")
    baidid = vastus.read()
    tekst = baidid.decode()



    barbora = re.findall('(content=")(.*?)(">)', tekst)
    #print(barbora)
    #print("Barboras on  85g Rolltoni kanaliha maitselised kiirnuudlid " + barbora[3][1] + " senti")

    conn = sqlite3.connect('nuudlihinnad.db')
    c = conn.cursor()

    number = barbora[3][1]
    number = float(number.replace(" ", "").replace("€", "").replace(",", ".").strip())
    number *= 100
    number = round(number)
    number = int(number)


    name = "Barbora"

    c.execute("select * from hinnad where pood = 'Barbora'")

    if c.fetchall():
        c.execute("UPDATE hinnad set hind = (?)  where pood = 'Barbora'", [number])
    else:
        c.execute("INSERT INTO hinnad (Hind, Pood) VALUES(?, ?)",
                  (number, name))
    conn.commit()
    conn.close()