import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

#driver inbuilt no manual chrome driver
driver = webdriver.Chrome()
driver.get('https://www.thesun.co.uk/sport/football/')


containers = driver.find_elements(by="xpath" , value='//div[@class="story__copy-container"]')

titles = []
subtitles = []
links =[]

# //div[@class = "story__copy-container"]/a/h3
for c in containers:
    title = c.find_element(by = "xpath" , value = './/a/p').text  #titles only
    titles.append(title)

    # .// means search inside current element only

    subtitle = c.find_element(by = "xpath" ,value= './/a/h3').text  #the content
    subtitles.append(subtitle)

    link = c.find_element(by = "xpath" , value = './/a').get_attribute("href") #the news link
    links.append(link)


my_dict = {'TITLES':titles,
       'SUBTITLES':subtitles,
       'LINKS':links
    }

df_headline = pd.DataFrame(my_dict)

df_headline.to_csv('News_Headlines.csv')

driver.quit()