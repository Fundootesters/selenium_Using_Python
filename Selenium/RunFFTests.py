from selenium import webdriver
from selenium.webdriver.common.by import By


class RunFfTest():

    def test(self):
        baseUrl = "https://www.seleniumhq.org/"
        driver = webdriver.Firefox(executable_path="D:\\Soft\\Jars\\geckodriver-v0.23.0-win64\\geckodriver.exe")
        driver.get(baseUrl)

        xpath = driver.find_element_by_xpath("//a[@title='Get Selenium']")

        if xpath is not None:
            print("Xpath is correct")

        xpath.click()

        driver.find_element(By.XPATH, "//a[@title='Selenium Projects']").click()

        driver.close()


ff = RunFfTest()
ff.test()

