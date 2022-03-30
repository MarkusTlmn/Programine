def megaturgotsing():

    from urllib.request import urlopen
    import re
    import sqlite3
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException

    vastus = urlopen("https://www.megaturg.ee/kiirsupid-ja-pudrud/rollton-kanalihamaitselised-kiirnuudlid-60g")
    baidid = vastus.read()
    tekst = baidid.decode()

    #print(tekst)
    megaturg = re.findall('(<span class="price normal">0.)(.*?)( €</span>)', tekst)

    #print('Megaturus on  60g Rolltoni kanaliha maitselised kiirnuudlid ' + megaturg[0][1] + " senti")

    conn = sqlite3.connect('nuudlihinnad.db')
    c = conn.cursor()

    number = (megaturg[0][1])
    name = "Megaturg"

    c.execute("select * from hinnad where pood = 'Megaturg'")

    if c.fetchall():
        c.execute("UPDATE hinnad set hind = (?)  where pood = 'megaturg'", [number.replace(",", ".")])
    else:
        c.execute("INSERT INTO hinnad (Hind, Pood) VALUES(?, ?)",
                  (number, name))
    conn.commit()
    conn.close()
