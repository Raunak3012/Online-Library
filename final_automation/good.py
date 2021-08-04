from selenium import webdriver
import creds
chromedriver = "C:/Users/sharm/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(chromedriver)
driver.get("http://127.0.0.1:8000/")
create_account=driver.find_element_by_xpath('/html/body/div[1]/div/div/form/a')
create_account.click()
register_username_input=driver.find_element_by_xpath('//*[@id="id_username"]')
register_username_input.send_keys(creds.USERNAME)
register_password_input=driver.find_element_by_xpath('//*[@id="id_password1"]')
register_password_input.send_keys(creds.PASSWORD)
register_confirm_password_input=driver.find_element_by_xpath('//*[@id="id_password2"]')
register_confirm_password_input.send_keys(creds.PASSWORD)
register_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/form/button')
register_button.click()

login_username_input=driver.find_element_by_xpath('//*[@id="id_username"]')
login_username_input.send_keys(creds.USERNAME)
login_password_input=driver.find_element_by_xpath('//*[@id="id_password"]')
login_password_input.send_keys(creds.PASSWORD)

login_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/form/button')
login_button.click()

first_detail_button=driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/span/a')
first_detail_button.click()
first_product_submit=driver.find_element_by_xpath('//*[@id="id_body"]')
first_product_submit.send_keys(creds.COMMENT)
cart_button=driver.find_element_by_xpath('//*[@id="id_body"]')
cart_button.click()
driver.get("http://127.0.0.1:8000/")
