import names
from selenium import  webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
my_driver = webdriver.Chrome()


my_driver.get("https://buyme.co.il/")
my_driver.get("https://buyme.co.il/?modal=login")



reg_page=my_driver.find_element(by="xpath",value='//*[@id="ember961"]/div/div[1]/div/div/div[3]/div[1]/span').click()

usr_name=my_driver.find_element(by="xpath", value='//html/body/div[6]/div/div[1]/div/div/div[3]/div[2]/div[3]/form/div[1]/label/input').send_keys("terantulae")
usr_mail=my_driver.find_element(by="xpath",value='/html/body/div[6]/div/div[1]/div/div/div[3]/div[2]/div[3]/form/div[2]/label/input').send_keys("emailtest@com.org")
usr_passw1=my_driver.find_element(by="id",value="valPass").send_keys("1234567 ")
usr_passw2=my_driver.find_element(by="id",value="ember1826").send_keys("1234567 ")


agreemment_one=my_driver.find_element(by="xpath",value='//html/body/div[6]/div/div[1]/div/div/div[3]/div[2]/div[3]/form/div[5]').click()

agreement_two=my_driver.find_element(by="xpath",value='//html/body/div[6]/div/div[1]/div/div/div[3]/div[2]/div[3]/form/div[6]/div').click()

my_driver.get("https://buyme.co.il/")
price_test=my_driver.find_element(by="xpath",value='//*[@id="ember1044"]/div/div[1]/span').click()

find_gift=my_driver.find_element(by="xpath",value='//html/body/div[6]/div/header/div[3]/div/div/form/a').click()

select_buton=my_driver.get("https://buyme.co.il/supplier/15579925?query=")
put2_cost=my_driver.find_element(by="xpath",value='//html/body/div[4]/div/div[2]/div[1]/div/div/div[2]/div/ul/li/div[1]/div/div[2]/form/div[1]/label/input').send_keys("300")
enter_cost=my_driver.find_element(by="xpath",value='//html/body/div[4]/div/div[2]/div[1]/div/div/div[2]/div/ul/li/div[1]/div/div[2]/form/div[2]/button').click()
nick_sent=my_driver.find_element(by="id",value="ember1674").send_keys("Aviel")
press_events=my_driver.find_element(by="xpath",value='//html/body/div[3]/div/div/div[3]/div/div/div[1]/form/div[2]/div[2]/label/div/div[1]/span').click()

thank_line=my_driver.find_element(by="xpath",value='//html/body/div[3]/div/div/div[3]/div/div/div[1]/form/div[2]/div[2]/label/div/div[2]/ul/li[5]/span').click()
greetings_row_clear=my_driver.find_element(by="xpath",value='//html/body/div[3]/div/div/div[3]/div/div/div[1]/form/div[2]/div[4]/label/textarea').clear()
greetings_row=my_driver.find_element(by="xpath",value='//html/body/div[3]/div/div/div[3]/div/div/div[1]/form/div[2]/div[4]/label/textarea').send_keys("You are an excellent lecturer")


upload_photo=my_driver.find_element(by="xpath",value='.//html/body/div[3]/div/div/div[3]/div/div/div[1]/form/div[2]/div[5]/div[2]/div[1]/label/input')
upload_photo.send_keys("C:\\Users\\yoav_\\Desktop\\JENKINS\\logo-jenkins.jpg")



#TESTING

expected="80.10"
actual=my_driver.find_element(by="id",value="tip").text1
actual1=my_driver.find_element(by="xpath",value="top").text2
assert expected!= actual
my_driver.quit()
