from selenium import webdriver
import time

chrome_driver_path = "C:/Users/nikyadav/Downloads/100 days/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")


start_time = time.time()
end_time = start_time + 60
while time.time() < end_time:
    cookie.click()
    if time.time() > start_time + 10:
        start_time += 10
        money_element = driver.find_element_by_id("money")
        money = int(money_element.text.replace(',', ''))
        all_items = driver.find_elements_by_css_selector("#store b")
        price = [int(item.text.split(' - ')[1].replace(',', '')) for item in all_items[:8]]
        for (i, cost) in enumerate(price):
            if cost > money:
                item_no = i
                break
        if item_no >= 1:
            available_item = all_items[item_no-1]
            available_item.click()

cps = driver.find_element_by_id("cps")
print(cps.text)
driver.quit()
