def selverotsing():

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
        return browser

    url = 'https://www.selver.ee/kiirnuudlid-kanalihamaitselised-rollton-60-g'
    driver = startSelenium(url)
    source = driver.page_source


    #print(source)
    selver = re.findall('(</h1> <div data-v-0121a281="" class="row"><div data-v-0121a281="" class="col-xs-6"><div data-v-4140045b="" data-v-0121a281="" class="ProductPrices Product__prices"><!----> <!----> <!----> <div data-v-4140045b="" class="ProductPrice">)(.*?)(<span data-v-4140045b="" class="ProductPrice__unit-price">11,50 €/kg</span></div> <!----></div> <button data-v-32c468bd="" data-v-0121a281="" type="button" class="WishlistButton"><svg data-v-32c468bd="" viewBox="0 0 18 18" fill="currentColor" role="presentation" class="Icon Wishlist__icon"><use xlink:href="#heart"></use></svg> <span data-v-32c468bd="" class="visually-hidden">)', source, flags=re.DOTALL)

    #print(selver)

    #print("Selveris on  85g Rolltoni kanaliha maitselised kiirnuudlid " + selver[0][1] + " senti")

    conn = sqlite3.connect('nuudlihinnad.db')
    c = conn.cursor()

    number = selver[0][1]
    number = float(number.replace(" ", "").replace("€", "").replace(",", ".").strip())
    number *= 100
    number = round(number)
    number = int(number)
    #print("pärast asendust: ", number)

    name = "Selver"

    c.execute("select * from hinnad where pood = 'Selver'")

    if c.fetchall():
        c.execute("UPDATE hinnad set hind = (?)  where pood = 'Selver'", [number])
    else:
        c.execute("INSERT INTO hinnad (Hind, Pood) VALUES(?, ?)",
              (number, name))
    conn.commit()
    conn.close()

