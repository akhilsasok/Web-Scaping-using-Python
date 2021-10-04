from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
url = 'https://www.cybo.com/US/los-angeles/all-membership-organizations/'
driver.get(url)
page = driver.page_source
soup = BeautifulSoup(page)
driver.quit()

lists = soup.find_all('div', class_="cybo result_box waiting")

with open('scrap_data.csv','w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'Address', 'Phone']
    thewriter.writerow(header)
    for list in lists:
        name = list.find('a', class_="r-e-bname ellipsis").text
        address = list.find('span', class_="e-add ellipsis").text
        phone = list.find('span', class_="phone-link hidden-dsk").text
        info = [name, address, phone]
        print(info)
        thewriter.writerow(info)
    f.close()