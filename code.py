from selenium import webdriver
from bs4 import BeautifulSoup


start_url = "https://meet.google.com/dkd-zwgb-uaz"
browser = webdriver.Chrome()
browser.get(start_url)

def join():
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/span/span').click()
    
join()
