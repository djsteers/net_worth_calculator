import unittest
import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint



class NetWorthCalculation(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        #Remove ChromeDriver warnings (ChromeDriver specific issue, can't fix this)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        #Use below if ChromeDriver will not be on PATH
        #self.driver = webdriver.Chrome(options=options, executable_path="YOUR PATH HERE")
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.harnesswealth.com/net-worth-calculator-legacy/")

    def test_happy_path(self):
        driver = self.driver
        asset_value = 100
        liability_value = 150
        asset_total = 800
        liability_total = 300

        #Loop through form fields and input asset values
        for field_id in locators.net_worth_form_fields.values():
            driver.find_element(By.ID, field_id).send_keys(asset_value)

        #Find asset value
        element = driver.find_element(By.CLASS_NAME, f'{locators.net_worth_page_elements["TOTAL_ASSETS"]}')

        #Confirm asset total matches what is displayed
        assert element.text == f"TOTAL ASSETS: ${asset_total}"

        driver.find_element(By.ID, f'{locators.net_worth_page_elements["NEXT_BUTTON"]}').click()

        #Loop through form fields and input liability values
        for field_id in locators.additional_details_form_fields.values():
            if field_id == "age":
                driver.find_element(By.ID, field_id).send_keys(30)
            else:
                driver.find_element(By.ID, field_id).send_keys(liability_value)
        
        #Find liability value
        element = driver.find_element(By.CLASS_NAME, f'{locators.additional_details_page_elements["TOTAL_LIABILITIES"]}')

        #Confirm liability total matches what is displayed
        assert element.text == f"TOTAL LIABILITIES: ${liability_total}"

        driver.find_element(By.ID, f'{locators.additional_details_page_elements["NEXT_BUTTON"]}').click()

        #Confirm values on net worth page match form inputs and totals
        element = driver.find_element(By.CLASS_NAME, f'{locators.net_worth_results_elements["NET_WORTH"]}')

        assert element.text == f"Your Net Worth: ${asset_total - liability_total}"

    def test_min_value(self):
        driver = self.driver
        asset_value = 0
        liability_value = 0
        asset_total = 0
        liability_total = 0

        #Loop through form fields and input asset values
        for field_id in locators.net_worth_form_fields.values():
            driver.find_element(By.ID, field_id).send_keys(asset_value)

        #Find asset value
        element = driver.find_element(By.CLASS_NAME, f'{locators.net_worth_page_elements["TOTAL_ASSETS"]}')

        #Confirm asset total matches what is displayed
        assert element.text == f"TOTAL ASSETS: ${asset_total}"

        driver.find_element(By.ID, f'{locators.net_worth_page_elements["NEXT_BUTTON"]}').click()

        #Loop through form fields and input liability values
        for field_id in locators.additional_details_form_fields.values():
            if field_id == "age":
                driver.find_element(By.ID, field_id).send_keys(18)
            else:
                driver.find_element(By.ID, field_id).send_keys(liability_value)
        
        #Find liability value
        element = driver.find_element(By.CLASS_NAME, f'{locators.additional_details_page_elements["TOTAL_LIABILITIES"]}')

        #Confirm liability total matches what is displayed
        assert element.text == f"TOTAL LIABILITIES: ${liability_total}"

        driver.find_element(By.ID, f'{locators.additional_details_page_elements["NEXT_BUTTON"]}').click()

        #Confirm values on net worth page match form inputs and totals
        element = driver.find_element(By.CLASS_NAME, f'{locators.net_worth_results_elements["NET_WORTH"]}')

        assert element.text == f"Your Net Worth: ${asset_total - liability_total}"

    def test_high_value(self):
        driver = self.driver
        asset_value = 1000000
        liability_value = 1000000
        asset_total = 8000000
        liability_total = 2000000

        #Loop through form fields and input asset values
        for field_id in locators.net_worth_form_fields.values():
            driver.find_element(By.ID, field_id).send_keys(asset_value)

        #Find asset value
        element = driver.find_element(By.CLASS_NAME, f'{locators.net_worth_page_elements["TOTAL_ASSETS"]}')

        #Confirm asset total matches what is displayed
        assert element.text.replace(",", "") == f"TOTAL ASSETS: ${asset_total}"

        driver.find_element(By.ID, f'{locators.net_worth_page_elements["NEXT_BUTTON"]}').click()

        #Loop through form fields and input liability values
        for field_id in locators.additional_details_form_fields.values():
            if field_id == "age":
                driver.find_element(By.ID, field_id).send_keys(99)
            else:
                driver.find_element(By.ID, field_id).send_keys(liability_value)
        
        #Find liability value
        element = driver.find_element(By.CLASS_NAME, f'{locators.additional_details_page_elements["TOTAL_LIABILITIES"]}')

        #Confirm liability total matches what is displayed
        assert element.text.replace(",", "") == f"TOTAL LIABILITIES: ${liability_total}"

        driver.find_element(By.ID, f'{locators.additional_details_page_elements["NEXT_BUTTON"]}').click()

        #Confirm values on net worth page match form inputs and totals
        element = driver.find_element(By.CLASS_NAME, f'{locators.net_worth_results_elements["NET_WORTH"]}')

        assert element.text.replace(",", "") == f"Your Net Worth: ${asset_total - liability_total}"

    def test_random_values(self):
        driver = self.driver
        asset_value = randint(1, 5000)
        liability_value = randint(1, 5000)
        asset_total = asset_value * 8
        liability_total = liability_value * 2

        #Loop through form fields and input asset values
        for field_id in locators.net_worth_form_fields.values():
            driver.find_element(By.ID, field_id).send_keys(asset_value)

        #Find asset value
        element = driver.find_element(By.CLASS_NAME, f'{locators.net_worth_page_elements["TOTAL_ASSETS"]}')

        #Confirm asset total matches what is displayed
        assert element.text.replace(",", "") == f"TOTAL ASSETS: ${asset_total}"

        driver.find_element(By.ID, f'{locators.net_worth_page_elements["NEXT_BUTTON"]}').click()

        #Loop through form fields and input liability values
        for field_id in locators.additional_details_form_fields.values():
            if field_id == "age":
                driver.find_element(By.ID, field_id).send_keys(randint(18, 99))
            else:
                driver.find_element(By.ID, field_id).send_keys(liability_value)
        
        #Find liability value
        element = driver.find_element(By.CLASS_NAME, f'{locators.additional_details_page_elements["TOTAL_LIABILITIES"]}')

        #Confirm liability total matches what is displayed
        assert element.text.replace(",", "") == f"TOTAL LIABILITIES: ${liability_total}"

        driver.find_element(By.ID, f'{locators.additional_details_page_elements["NEXT_BUTTON"]}').click()

        #Confirm values on net worth page match form inputs and totals
        element = driver.find_element(By.CLASS_NAME, f'{locators.net_worth_results_elements["NET_WORTH"]}')

        assert element.text.replace(",", "") == f"Your Net Worth: ${asset_total - liability_total}"

    #Example of a test that should pass, but currently fails through automation testing
    def test_disabled_buttons(self):
        driver = self.driver

        #Loop through form fields and input asset values
        for field_id in locators.net_worth_form_fields.values():
            driver.find_element(By.ID, field_id).send_keys("")
            
        button = driver.find_element(By.ID, f'{locators.net_worth_page_elements["NEXT_BUTTON"]}')

        assert button.is_enabled() == False


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()




