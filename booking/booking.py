import time
from booking.constants import *
import booking.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from booking.BookingFiltration import BookingFiltration
from booking.Rapport import Rapport
import os


class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:/SeleniumDriver", teardown = False):
        options = Options()
        options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__(chrome_options=options)
        self.implicitly_wait(30)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.base_url)

    def change_currency(self, currency = None):
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            "button[class='bui-button bui-button--light bui-button--large'][data-modal-size='960']"
        )
        currency_element.click()
        try:
            curr = self.find_element(
                By.CSS_SELECTOR,
                f"a[data-modal-header-async-url-param='changed_currency=1&selected_currency={currency}&top_currency=1']"
            )
            curr.click()
        except:
            print("The currency doesn't exist")


    def searchplace(self, place = None):
        search_tab = self.find_element(
            By.CSS_SELECTOR,
            "input[id='ss']"
        )
        search_tab.clear()
        search_tab.send_keys(place)
        first_res = self.find_element(
            By.CSS_SELECTOR,
            "li[data-i='1']"
        )
        first_res.click()


    def choosedates(self, dep = None, arr = None):
        month_arr = arr.split("-")[1]
        month_dep = dep.split("-")[1]
        year_arr = arr.split("-")[0]
        year_dep = dep.split("-")[0]

        # On choisit la date de depart dans toutes les dates disponibles
        try:
            while int(year_dep) > int(self.find_element(By.CSS_SELECTOR, "div[class='bui-calendar__month']").text.split(" ")[1]):
                next_month = self.find_element(By.CSS_SELECTOR, "div[data-bui-ref='calendar-next']")
                next_month.click()



            while int(month_dep) > month_to_int(
                    self.find_element(By.CSS_SELECTOR, "div[class='bui-calendar__month']").text.split()[0]):
                next_month = self.find_element(By.CSS_SELECTOR, "div[data-bui-ref='calendar-next']")
                next_month.click()
            depart = self.find_element(
                By.CSS_SELECTOR,
                f"td[data-date='{dep}']"
            )
            depart.click()

            # On choisit la ate d'arrivée parmis toutes les dates
            while int(year_arr) > int(self.find_element(By.CSS_SELECTOR, "div[class='bui-calendar__month']").text.split()[1]):
                next_month = self.find_element(By.CSS_SELECTOR, "div[data-bui-ref='calendar-next']")
                next_month.click()
            while int(month_arr) > month_to_int(
                    self.find_element(By.CSS_SELECTOR, "div[class='bui-calendar__month']").text.split()[0]):
                next_month = self.find_element(By.CSS_SELECTOR, "div[data-bui-ref='calendar-next']")
                next_month.click()

            arrive = self.find_element(
                By.CSS_SELECTOR,
                f"td[data-date='{arr}']"
            )
            arrive.click()
        except:
            print("La date choisi n'est pas disponible.")


    def choose_nbr(self,adults=1,kids=0,rooms=1):
        toggle = self.find_element(By.ID, "xp__guests__toggle")
        toggle.click()
        moins_nbr_adults = self.find_element(By.CSS_SELECTOR,"button[aria-label='Supprimer des Adultes']")
        plus_nbr_adults = self.find_element(By.CSS_SELECTOR,"button[aria-label='Ajouter des Adultes']")
        moins_nbr_kids = self.find_element(By.CSS_SELECTOR, "button[aria-label='Supprimer des Enfants']")
        plus_nbr_kids = self.find_element(By.CSS_SELECTOR, "button[aria-label='Ajouter des Enfants']")
        moins_nbr_rooms = self.find_element(By.CSS_SELECTOR, "button[aria-label='Supprimer des Chambres']")
        plus_nbr_rooms = self.find_element(By.CSS_SELECTOR, "button[aria-label='Ajouter des Chambres']")

        nbr_adults = self.find_element(By.CSS_SELECTOR, "input[id='group_adults']").get_attribute('value') #Donne le nombre d'adultes selectionné maintenant        nbr_adults.get_attribute('value')
        nbr_kids = self.find_element(By.CSS_SELECTOR, "input[id='group_children']").get_attribute('value')
        nbr_rooms = self.find_element(By.CSS_SELECTOR, "input[id='no_rooms']").get_attribute('value')
        while int(nbr_adults)<adults:
            plus_nbr_adults.click()
            nbr_adults = self.find_element(By.CSS_SELECTOR, "input[id='group_adults']").get_attribute('value')

        """
        while int(nbr_kids)<kids:
            nbr_kids = self.find_element(By.CSS_SELECTOR, "input[id='group_children']").get_attribute('value')
            plus_nbr_kids.click()
        """
        """while int(nbr_rooms)<rooms:
            nbr_rooms = self.find_element(By.CSS_SELECTOR, "input[id='no_rooms']").get_attribute('value')
            plus_nbr_rooms.click()
        """
        while int(nbr_adults) > adults:
            moins_nbr_adults.click()
            nbr_adults = self.find_element(By.CSS_SELECTOR, "input[id='group_adults']").get_attribute('value')

        """
        while int(nbr_kids) > kids:
            nbr_kids = self.find_element(By.CSS_SELECTOR, "input[id='group_children']").get_attribute('value')
            moins_nbr_kids.click()
        """
        """while int(nbr_rooms) > rooms:
            nbr_rooms = self.find_element(By.CSS_SELECTOR, "input[id='no_rooms']").get_attribute('value')
            moins_nbr_rooms.click()
        """



    def search(self):
        search = self.find_element(
             By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search.click()

    def closepop(self):
        self.find_element(By.TAG_NAME,'body').send_keys(Keys.ESCAPE)


    def apply_filtre(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating( 3, 4, 5)
        time.sleep(3)
        try:
            filtration.cheapest_first()
        except:
            print('The cheapest first button is not available anymore.')

    def report_results(self,nom_fichier="HOTELS"):
        results = Rapport(driver = self)
        resultats = results.fetch_data()
        results.data_to_csv(resultats,nom_fichier)


