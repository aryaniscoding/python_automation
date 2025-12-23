from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable) #get the path of executable which we are going to create

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

#headless mode
options = Options()
# options.headless = True (older way)
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get('https://www.thesun.co.uk/sport/football/')

containers = driver.find_elements(by='xpath' , value ='//div[@class="story__copy-container"]')
titles = []
subtitles = []
links = []

for c in containers:
    headline = c.find_element(by = 'xpath' , value = './/a/p').text
    titles.append(headline)

    subtitle = c.find_element(by = 'xpath' , value = './/a/h3').text
    subtitles.append(subtitle)

    link = c.find_element(by='xpath' , value='.//a').get_attribute('href')
    links.append(link)

my_dict = {
    'TITLES':titles,
    'SUBTITLES':subtitles,
    'LINKS':links
}

# os.path.join(,)

df_headline = pd.DataFrame(my_dict)
print("Saving file to:", application_path)

curent_month = month_day_year[:2]
curent_day = month_day_year[2:4]
curent_year = month_day_year[4:]

df_headline.to_csv(f'{application_path}/headless_news_{curent_month}_{curent_day}_{curent_year}.csv')

driver.quit()

#pyinstaller converts .py into exe file

