from selenium import webdriver
from parser import parse_offices
from csv_utils import write_to_csv
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager


def main(output_file):
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.onlyoffice.com")

    about_menu = driver.find_element(By.ID, "navitem_about")
    contacts_link = driver.find_element(By.ID, "navitem_about_contacts")

    actions = ActionChains(driver)
    actions.move_to_element(about_menu).click(contacts_link).perform()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "companydata")))

    offices = parse_offices(driver)
    write_to_csv(output_file, offices)

    driver.quit()


if __name__ == "__main__":
    output_file = "offices.csv"
    main(output_file)