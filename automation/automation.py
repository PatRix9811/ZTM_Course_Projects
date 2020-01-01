from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert "Selenium Easy Demo" in driver.title
button_text = driver.find_element_by_class_name('btn-default')
input_box =  driver.find_element_by_id('user-message')
input_box.clear()
input_box.send_keys('My message')
button_text.click()
my_message = driver.find_element_by_id('display')
assert 'My message' in my_message.text



driver.close()
