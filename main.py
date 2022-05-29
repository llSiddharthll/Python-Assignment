from selenium import webdriver as wd
from selenium.webdriver.support.select import Select
import chromedriver_binary
import random 
import time
import csv

class extract:
    def values(self):
        file = open("sample.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()

    def purchase(self):

        wd= wd.Chrome()

        wd.get("https://edalnice.cz/en/bulk-purchase/index.html")

        random_wait_time = random.randrange(15.0, 20.0)
        print(random_wait_time)
        time.sleep(random_wait_time)

        file = open("sample.csv")
        csvreader = csv.reader(file)
        a = list(csvreader)
        for i in range(0,5):
            for j in range(0,5):
                country = a[i][j]
                date = a[i][j+1]
                licence_plate = a[i][j+2]
                powered_by = a[i][j+3]
                vignette = a[i][j+4]
                break
            break


        beginning_of_vignette_validity = wd.find_element_by_xpath('//*[@id="valid-since-input"]')
        beginning_of_vignette_validity.send_keys(date)
        random_wait_time = random.randrange(2.0, 3.0)
        print(random_wait_time)
        time.sleep(random_wait_time)

        licence_plate_no =wd.find_element_by_xpath('//*[@id="root"]/div/form/div/div[1]/div/div[3]/div/div/div[1]/input')
        licence_plate_no.send_keys(licence_plate)
        random_wait_time = random.randrange(2.0, 3.0)
        print(random_wait_time)
        time.sleep(random_wait_time)

        if (powered_by == "Natural Gas"):   

            powered_by = wd.find_element_by_xpath('//*[@id="alternative_fuel_type_checkbox_0"]')
            powered_by.click()
            random_wait_time = random.randrange(2.0,3.0)
            print(random_wait_time)
            time.sleep(random_wait_time)

            natural_gas = wd.find_element_by_xpath('//*[@id="natural_gas_radio_array_option_0"]')
            natural_gas.click()
            random_wait_time = random.randrange(2.0, 3.0)
            print(random_wait_time)
            time.sleep(random_wait_time)

        elif (powered_by == "Biomethane") :
            powered_by = wd.find_element_by_xpath('//*[@id="alternative_fuel_type_checkbox_0"]')
            powered_by.click()
            random_wait_time = random.randrange(2.0,3.0)
            print(random_wait_time)
            time.sleep(random_wait_time)  


            biomethane = wd.find_element_by_xpath('//*[@id="bio_methane_radio_array_option_0"]')
            biomethane.click()
            random_wait_time = random.randrange(2.0, 3.0)
            print(random_wait_time)
            time.sleep(random_wait_time)

        if vignette =="Annual" :

            anuual = wd.find_element_by_xpath('//*[@id="root"]/div/form/div/div[1]/div/fieldset/div/div/div/div[1]/div/div/label/div')
            anuual.click()
            random_wait_time = random.randrange(2.0, 3.0)
            print(random_wait_time)
            time.sleep(random_wait_time)

        elif(vignette=="30-day"):


            thirty_days= wd.find_element_by_xpath('//*[@id="root"]/div/form/div/div[1]/div/fieldset/div/div/div/div[2]/div/div/label/div')
            thirty_days.click()
            random_wait_time = random.randrange(2.0, 3.0)
            print(random_wait_time)
            time.sleep(random_wait_time)

        else:

            ten_days = wd.find_element_by_xpath('//*[@id="root"]/div/form/div/div[1]/div/fieldset/div/div/div/div[3]/div/div/label/div')
            ten_days.click()
            random_wait_time = random.randrange(2.0, 3.0)
            print(random_wait_time)
            time.sleep(random_wait_time)

    def Recapitulation(self):
        continue_button = wd.find_element_by_xpath('//*[@id="multiEshop"]/div/div[2]/div/div[8]/div/button')
        continue_button.click()


    def payment(self):
        pay_button = wd.find_element_by_xpath('//*[@id="multiEshop"]/div[2]/div/div[10]/div/button')
        pay_button.click()