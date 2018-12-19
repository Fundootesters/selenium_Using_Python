from selenium import webdriver
import time



class take_screenshot():

    def screenshot(self):
        baseUrl = "https://www.seleniumhq.org/"
        driver = webdriver.Firefox(executable_path="D:\\Soft\\Jars\\geckodriver-v0.23.0-win64\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        self.met(driver)
        driver.quit()


    def met(self, driver):

        filename = "D:\\PythonAutomation\\" + str(time.time()*1000) + ".png"
        try:

            driver.save_screenshot(filename)
            print("Screenshot saved to directory --> :: " + filename)
        except NotADirectoryError:
            print("Not a directory issue")


ff = take_screenshot()
ff.screenshot()

