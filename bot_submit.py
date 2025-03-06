from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

start_time = time.time()  


driver.get("http://127.0.0.1:5500/form-submission/ticket_booking.html")


wait = WebDriverWait(driver, 10)


wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Test User")
wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("test@example.com")


match_dropdown = wait.until(EC.presence_of_element_located((By.NAME, "match")))
try:
    select = Select(match_dropdown)
    select.select_by_visible_text("Mumbai Indians vs Chennai Super Kings")
except:
    match_dropdown.send_keys("Mumbai Indians vs Chennai Super Kings")  # If not a <select>

wait.until(EC.presence_of_element_located((By.NAME, "tickets"))).send_keys("2")


wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()

end_time = time.time() 


print("\n\n⏳ Automated form submission time:", round(end_time - start_time, 4), "seconds\n\n")


driver.quit()
