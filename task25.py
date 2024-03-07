#common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
#Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Imdb:
    #create method to open the url
    def __init__(self, url = "https://www.imdb.com/search/name/"):
        self.url =url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=2)
        self.actionChains = ActionChains(self.driver)

    #create method to boot up the webpage
    def boot(self):
        self.driver.get(self.url)
        self.wait.until(EC.url_to_be(self.url))
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    #create method to close the pop-up by using the xpath
    def closePopup(self):
        try:
            popup_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/button[2]')))
            popup_button.click()
            print("Pop up closed!")
        except TimeoutException:
            print("Pop up not found or clickable")

    #create a method that uses the name of the search box("q") to search for the query(movie name) and print it
    def searchBox(self, query):
        search_box = self.driver.find_element(by=By.NAME, value="q")
        search_box.send_keys(query)
        self.clickSearch()
        print(f"The movie searched for is {query}")

    #method to select the search button
    def clickSearch(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.ID,"suggestion-search-button")))
        search_button.click()

    #method to select ALL from the drop down list using the xpath
    def dropDownSelect(self):
        dropdown_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="nav-search-form"]/div[1]/div/label/span')
        dropdown_menu.click()
        self.wait.until(EC.element_to_be_selected(dropdown_menu))


if __name__ == "__main__":
   obj = Imdb()
   obj.boot()
   obj.closePopup()
   obj.searchBox("Oppenheimer")
   obj.quit()


