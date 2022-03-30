def coopotsing():

    from urllib.request import urlopen
    import re
    import sqlite3
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException

    chromeDriver = 'C:/Users/markus/Downloads/chromedriver.exe'

    def startSelenium(url):
        optionss = webdriver.ChromeOptions()
        optionss.add_argument('--disable-blink-features=AutomationControlled')
        optionss.add_experimental_option("excludeSwitches", ["enable-automation"])
        optionss.add_experimental_option('useAutomationExtension', False)

        optionss.add_argument("window-size=1600,1200")
        from fake_useragent import UserAgent
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        optionss.add_argument(f'user-agent={user_agent}')

        browser = webdriver.Chrome(options=optionss, executable_path=chromeDriver)
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        browser.get(url)
        delay = 3  # seconds
        try:
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'decimal')))
            print
            "Page is ready!"
        except TimeoutException:
            print
            "Loading took too much time!"
        return browser


    url = 'https://ecoop.ee/et/toode/12858761-rollton-nuudliroog-60g-kanamaitseline'
    driver = startSelenium(url)
    source = driver.page_source

    # print(source)



    coop = re.findall('(<div _ngcontent-.*?-c21="" class="decimal">)(.*?)( €</div>)', source)

    print("Coopis on 60g Rolltoni kanaliha maitselised kiirnuudlid " + coop[0][1] + " senti")

    conn = sqlite3.connect('nuudlihinnad.db')
    c = conn.cursor()

    number = (coop[0][1])
    name = "Coop"

    c.execute("select * from hinnad where pood = 'Coop'")

    if c.fetchall():
        c.execute("UPDATE hinnad set hind = (?)  where pood = 'Coop'", [number.replace(",", ".")])
    else:
        c.execute("INSERT INTO hinnad (Hind, Pood) VALUES(?, ?)",
              (number, name))
    conn.commit()
    conn.close()

