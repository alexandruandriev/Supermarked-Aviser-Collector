from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
site_links = ["https://rema1000.dk/om-rema-1000/avis/avis/"]

browser = webdriver.Chrome()


def rema1000(url):
    browser.get(url)
    time.sleep(0.5)

    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')

    catalog_object = soup.find('div',{'class':'eta-catalog'})
    #This is only written to avoid a dynamic-generated url
    href = catalog_object.a["href"]
    second_url = url + href
    browser.get(second_url)
    time.sleep(2)
    #Rema uses some Iframe weird thing , use this to switch to it
    iframe = browser.find_element_by_xpath('/html/body/iframe[2]')
    browser.switch_to.frame(iframe)
    #Finds the download button
    button = browser.find_element_by_xpath('/html/body/div[2]/header/div[2]/a[5]')
    button.click()
    time.sleep(2)

    #If everything goes well , the current page should be our pdf url.

    download_url = browser.current_url

    r = requests.get(download_url)
    print("It takes a while to load the pdf page")
    pdf_file = open("rema100.pdf",'wb')
    pdf_file.write(r.content)
    pdf_file.close()


def main():
    rema1000(site_links[0])

if __name__ == "__main__":
    main()


