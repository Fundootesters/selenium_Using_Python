from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class DropdownSelect():

    def test(self):
        baseUrl = "https://www.seleniumhq.org/"
        driver = webdriver.Firefox(executable_path="D:\\Soft\\Jars\\geckodriver-v0.23.0-win64\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        

        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")

        driver.quit()


ff = DropdownSelect()
ff.test()
