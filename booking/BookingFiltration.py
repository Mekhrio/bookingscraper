#This file includes a class that apply filtrations to the result of our research
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By



class BookingFiltration():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(30)
    
    def apply_star_rating(self, *rating):
        etoiles = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        listeetoiles = etoiles.find_elements(By.TAG_NAME, "div")
        for rat in rating:
            for element in listeetoiles:
                if str(element.get_attribute("data-filters-item")) == f"class:class={rat}":
                    element.click()


    def cheapest_first(self):
        button =  self.driver.find_element(By.CSS_SELECTOR,'li[data-id="price"]')
        button.click()
    
    
    