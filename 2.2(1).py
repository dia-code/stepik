from selenium import webdriver
import time 
import math
def calc():
   q_el = browser.find_element_by_id("num1")
   q = q_el.text
   p_el = browser.find_element_by_id("num2")
   p = p_el.text
   x = int(q) + int(p)
   return (x)
   
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    y = str(calc())
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

