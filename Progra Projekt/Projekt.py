from urllib.request import urlopen
import re
import sqlite3

import cffi.setuptools_ext
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from Desktop.project.barbora import barboraotsing
from Desktop.project.megaturg import megaturgotsing
from Desktop.project.project import coopotsing
from Desktop.project.rimikood import rimiotsing
from Desktop.project.test import selverotsing

rimiotsing()
coopotsing()
selverotsing()
barboraotsing()
megaturgotsing()

conn = sqlite3.connect('nuudlihinnad.db')
c = conn.cursor()

c.execute("select pood, hind from hinnad where hind = (select min(hind) from hinnad)")
odavaim = c.fetchall()
#print(odavaim)

if odavaim[0][0] == "Coop" or "Selver":
    print("Täna on nuudlid kõige odavamad " + str(odavaim[0][0]) + "is ja hinnaga " + str(odavaim[0][1]) + " senti")
elif odavaim[0][0] == "Rimi":
    print("Täna on nuudlid kõige odavamad " + str(odavaim[0][0]) + "s ja hinnaga " + str(odavaim[0][1]) + " senti")
elif odavaim[0][0] == "Barbora":
    print("Täna on nuudlid kõige odavamad " + str(odavaim[0][0]) + "as ja hinnaga " + str(odavaim[0][1]) + " senti")
elif odavaim[0][0] == "Megaturg":
    print("Täna on nuudlid kõige odavamad Megaturus ja hinnaga " + str(odavaim[0][1]) + " senti")

conn.close()
