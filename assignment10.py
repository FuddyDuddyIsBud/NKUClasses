import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
from selenium import webdriver
from seleniu.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


#task1

driver = webdriver.Chrome()
driver.get(www.google.com)
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 greatest movies of all time imdb')
button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
button.click()
time.sleep(2)
driver.save_screenshot('screenshot.png')

#task2

google_button = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3')
google_button.click()
time.sleep(2)

element = driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[3]/div[50]/div[2]/h3/a')
actions=ActionChains(driver)
actions.move_to_element(element).preform()
time.sleep(2)
driver.save_screenshot('screenshot2.png')

jaws_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img')
jaws_button.click()

time.sleep(2)
driver.save_screenshot('screenshot3.png')

#task3

username=input("input username: ")
password=input("input password: ")

driver = webdriver.Chrome()
driver.get('https://store.unionlosangeles.com/collections/outerwear')
button = driver.find_element_by_xpath('//*[@id="shopify-section-header"]/div/header/div/div[2]/a[1]/span')
button.click()
time.sleep(2)

box = driver.find_element_by_xpath('//*[@id = "customer_email"]')
box.send_keys(username)
time.sleep(2)

box = driver.find_element_by_xpath('//*[@id="customer_password"]')
box.send_keys(password)
time.sleep(2)
button = driver.find_element_by_xpath('//*[@id="customer_login"]/div[3]/input')
button.click()


while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(new_height)
    if new_height == last_height:
        break
    last_height = new_height
    
driver.save_screenshot('screenshot4.png')

print(last_height)


#task4

df = pd.DataFrame({'Link': [''], 'Vendor': [''], 'Title': [''], 'Price': ['']})

for product in product_card:
    try:
        Link = product.find('a', class_='product-card__img-link-overlay').get('href')
        Vendor = product.find('div', class_='product-card__title').text
        Title = product.find('div', class_='product-card__subtitle').text
        Price = product.find('div', class_='product-price ca__styling is--striked-out css-0').text
        df = df.append({'Link': link, 'Vendor': Vendor, 'Title': Title,'Price': Price}, ignore_index=True)
    except:
        pass

print(df)

driver.save_screenshot('screenshot4.png')
df.to_csv('A/File/Path/file_name.csv')