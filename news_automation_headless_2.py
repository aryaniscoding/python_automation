from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options

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

df_headline = pd.DataFrame(my_dict)
df_headline.to_csv("headless_news.csv")

driver.quit()