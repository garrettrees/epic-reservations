#!/Users/garrettrees/opt/anaconda3/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import datetime
import time

#This script will reserve 7 days from today's date
#Set your username, password & target reservation day (of the current month) before running script
username = "greesy@gmail.com" #email address
password = "R!d3-0r-d!3"
today = datetime.datetime.now().strftime("%d")
reservation_day = str(int(today) + 7)
driver = webdriver.Chrome("/Users/garrettrees/chromedriver")

driver.implicitly_wait(10)
#Set browser size (so all elements are visible)
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
#username_field.clear()
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

#Select Date
desired_date = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/button[" + reservation_day + "]")
#desired_date = driver.find_element_by_css_selector("#passHolderReservations__wrapper > div:nth-child(3) > div.passholder_reservations__booking_container > div.passholder_reservations__booking.row.reverse_styles > div.shared_modal.shared_modal--open > div.shared_modal__container.container.shared_modal__container--not_full_screen > div.shared_modal__content > div > div.passholder_reservations__calendar > div > div.passholder_reservations__calendar__days > button:nth-child(" + reservation_day + ")"
desired_date.click()

#Assign Pass Holders
pass_holder = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/ul/li/span/label/span")
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