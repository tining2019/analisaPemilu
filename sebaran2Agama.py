# import libraries
from bs4 import BeautifulSoup
#import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#DATA SEBARAN AGAMA JATIM
url2 = 'https://jatim.bps.go.id/dynamictable/2017/10/09/120/jumlah-penduduk-menurut-kabupaten-kota-dan-agama-yang-dianut-di-provinsi-jawa-timur-2016.html'
# The path to where you have your chrome webdriver stored:
webdriver_path = 'D:/SOFTWARE/chromedriver_win32/chromedriver.exe'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)
# Load webpage
browser.get(url2)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse the raw into delicious soup
soup2 = BeautifulSoup(browser.page_source, 'html.parser')

def sebaran2Agama():
    tabel2 = soup2.find('table', attrs={'id':'tableRightBottom'})
    hasil2 = tabel2.find_all('tr')
    print(hasil2)

    wilJatim = []
    wilJatim.append(['Provinsi Jatim'])
    indeksAgama = []
    tIslam = []
    tProtestan = []
    tKatolik = []
    tHindu = []
    tBudha = []
    tLain = []

    # loop over hasil
    for h2 in hasil2:
        # find all columns per result
        dataTot2 = h2.find_all('td', attrs={'class':'datas'})
        # check that columns have data
        if len(dataTot2) == 0:
            continue

        agmIslam = dataTot2[0].getText()
        agmProtestan = dataTot2[1].getText()
        agmKatolik = dataTot2[2].getText()
        agmHindu = dataTot2[3].getText()
        agmBudha = dataTot2[4].getText()
        agmLain = dataTot2[5].getText()

        # Remove decimal point
        agmIslam = agmIslam.replace(' ','')
        agmProtestan = agmProtestan.replace(' ','')
        agmKatolik = agmKatolik.replace(' ','')
        agmHindu = agmHindu.replace(' ','')
        agmBudha = agmBudha.replace(' ','')
        agmLain = agmLain.replace(' ','')

        agmIslam = float(agmIslam)
        agmProtestan = float(agmProtestan)
        agmKatolik = float(agmKatolik)
        agmHindu = float(agmHindu)
        agmBudha =  float(agmBudha)
        agmLain = float(agmLain)

        tIslam.append(agmIslam)
        tProtestan.append(agmProtestan)
        tKatolik.append(agmKatolik)
        tHindu.append(agmHindu)
        tBudha.append(agmBudha)
        tLain.append(agmLain)

    indeksAgama.append((tIslam[-1]))
    indeksAgama.append((tProtestan[-1]))
    indeksAgama.append((tKatolik[-1]))
    indeksAgama.append((tHindu[-1]))
    indeksAgama.append((tBudha[-1]))
    indeksAgama.append((tLain[-1]))


    #print indexSebaranAgama
    agama = []
    agama.append('islam')
    agama.append('protestan')
    agama.append('katolik')
    agama.append('hindu')
    agama.append('budha')
    agama.append('lain')

    print (agama)
    print (indeksAgama)
    np_agama = np.array(agama)
    np_indeks = np.array(indeksAgama)

    #naming Label
    plt.xlabel('Agama')
    plt.ylabel('Jumlah Penduduk di Provinsi Jatim')

    #styling x,y value
    plt.xticks(rotation=30,ha='right')
    plt.yticks(np.arange(np_indeks.min(),np_indeks.max(),4000000))

    #plot data
    #plt.subplot(2,1,2)
    plt.plot(np_agama,np_indeks,color='red',label='AGAMA')
    plt.legend(loc='upper right')
    plt.yscale('linear')
    plt.show()


sebaran2Agama()
