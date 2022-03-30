def rimiotsing():

    from urllib.request import urlopen
    import re
    import sqlite3
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException

    vastus = urlopen("https://www.rimi.ee/epood/en/products/groceries/fast-food/noodles-and-pastas/kiirnuudlid-kanaliha-maitselised-rollton-60g/p/115329")
    baidid = vastus.read()
    tekst = baidid.decode()

    #print(tekst)

    rimi = re.findall('(<sup>)(.*)(</sup>)', tekst)
    #print("Rimis on Rolltoni kanaliha maitselised puljongiga kiirnuudlid " + rimi[0][1] + " senti")

    conn = sqlite3.connect('nuudlihinnad.db')
    c = conn.cursor()

    number = (rimi[0][1])
    name = "Rimi"

    c.execute("select * from hinnad where pood = 'Rimi'")
    c.execute("UPDATE hinnad set hind = (?)  where pood = 'Rimi'", [number.replace(",", ".")])

    conn.commit()
    conn.close()

