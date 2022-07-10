import time
import csv
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Rapport():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    def fetch_data(self):
        page = self.driver.find_element(By.CSS_SELECTOR, "div[class='d4924c9e74']")
        liste = []
        test = True
        while test:
            liste_hotels = page.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")
            page_sui = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Page suivante']")
            for hotel in liste_hotels:
                nomhotel = hotel.find_element(By.CSS_SELECTOR,"div[data-testid='title']").text.strip()
                prixhotel = hotel.find_element(By.CSS_SELECTOR,"span[class='fcab3ed991 bd73d13072']").text.strip()
                liste.append([nomhotel,prixhotel])
            test = page_sui.is_enabled()
            try:
                page_sui.click()
                time.sleep(7)
            except:
                print("Derniere page.")
                break

        return liste

    def data_to_csv(self,list,nom_fich='hotels'):
        header = ['HOTEL NAME', 'PRICE']
        with open(f'{nom_fich}.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(list)



