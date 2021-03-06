#!/Users/garrettrees/opt/anaconda3/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import datetime
import time

#This script will reserve 7 days from today's date
today = datetime.datetime.now().strftime("%d")
current_month = datetime.datetime.now().strftime("%m")

driver = webdriver.Chrome("/Users/garrettrees/chromedriver")

# Set username & password, user to make reservation for
user = ''
if user == '':
    username = ""  # email address
    password = ""
    user_xpath = "/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/ul/li[2]/span/label/span"
    #username = get_parameters('epic_username_byron')
    #password = get_parameters('epic_password_byron')
else:
    username = ''
    password = ''
    user_xpath = "/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/ul/li/span/label/span"
    #username = get_parameters('epic_username_garrett')
    #password = get_parameters('epic_password_garrett')

#Set implicit wait for the life of the webdriver object
driver.implicitly_wait(30)
#Maximize browser (so all elements are visible)
driver.maximize_window()
#Go to Reservations page
driver.get("https://www.epicpass.com/info/reservation-details.aspx")
#Close cookies banner at bottom of page
close_banner = driver.find_element_by_id("onetrust-accept-btn-handler")
close_banner.click()
#Click Reserve button
reserve_button = driver.find_element_by_link_text("RESERVE YOUR DAYS")
reserve_button.send_keys(Keys.RETURN)

#Login
username_field = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/form/div/div/div[3]/input")
username_field.send_keys(username)
password_field = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/form/div/div/div[4]/input")
password_field.send_keys(password)
sign_in_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/form/div/div/div[5]/button")
sign_in_button.send_keys(Keys.RETURN)

#Select Resort
park_city = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div/select/option[24]")
park_city.click()
check_availability = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button")
check_availability.click()

#### Logic to handle reservations made less than 7 days from the end of the current month ####
go_to_next_month = driver.find_element_by_xpath(
    "/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/button[2]")
if (current_month == "01" or current_month == "03" or current_month == "05" or current_month == "07" or current_month == "08" or current_month == "10" or current_month == "12") and today >= "25":
    reservation_day = str(7 - (31 - (int(today))))
    go_to_next_month.click()
elif current_month == "02" and today >= "22":
    reservation_day = str(7 - (28 - (int(today))))
    go_to_next_month.click()
elif (current_month == "04" or current_month == "06" or current_month == "09" or current_month == "11") and today >= "24":
    reservation_day = str(7 - (30 - (int(today))))
    go_to_next_month.click()
else:
    reservation_day = str(int(today) + 7)

print("Current month: " + current_month)
print("Today is: " + today)
print("Reservation day: " + reservation_day)

#Select Date
desired_date = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/button[" + reservation_day + "]")
desired_date.click()

#Assign Pass Holders
pass_holder = driver.find_element_by_xpath(user_xpath)
pass_holder.click()
assign_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div[3]/button[2]")
assign_button.click()

#Accept Terms & Conditions
terms_conditions = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[6]/div[2]/div[2]/div[2]/label/input")
driver.execute_script("arguments[0].click();", terms_conditions)

#Complete Reservation
complete_reservation = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[6]/div[3]/button")
driver.execute_script("arguments[0].click();", complete_reservation)

#Close browser & quit
driver.close()
driver.quit()
