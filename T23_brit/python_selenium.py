"""
=====================================================
  SELENIUM BASICS  |  For Python devs, zero Selenium
=====================================================
Think of Selenium as: "Python remote control for a browser"
"""

# ── THE BIG PICTURE ───────────────────────────────
# 1. You start a browser (driver)
# 2. You tell it to open a URL
# 3. You find elements on the page
# 4. You interact with them (click, type)
# 5. You check the result
# 6. You close the browser


# ── STEP 1: START THE BROWSER ─────────────────────
from selenium import webdriver

driver = webdriver.Chrome()   # opens a Chrome window
driver.get("https://google.com")  # like typing a URL in the address bar

# Always close the browser when done:
driver.quit()   # kills the whole browser
driver.close()  # closes only the current tab (browser stays open)
# RULE: almost always use quit()


# ── STEP 2: FIND ELEMENTS ─────────────────────────
# You need to tell Selenium "which element on the page?"
# Use By to say HOW to find it

from selenium.webdriver.common.by import By

# Most common ways:
driver.find_element(By.ID, "username")         # finds <input id="username">
driver.find_element(By.NAME, "email")          # finds <input name="email">
driver.find_element(By.CLASS_NAME, "btn")      # finds first element with class="btn"
driver.find_element(By.LINK_TEXT, "Log in")    # finds <a>Log in</a> (exact text)

# ONE vs MANY:
el  = driver.find_element(By.CLASS_NAME, "item")   # ONE  — error if not found
els = driver.find_elements(By.CLASS_NAME, "item")  # LIST — empty list if not found
# find_elements (plural) never crashes, just returns []


# ── STEP 3: INTERACT WITH AN ELEMENT ──────────────
el = driver.find_element(By.ID, "username")

el.click()              # click it
el.send_keys("admin")   # type text into it  (like pressing keyboard keys)
el.clear()              # erase the text inside it

el.text                 # READ the visible text of the element  (it's a property, no ())
el.get_attribute("href")  # read any HTML attribute, e.g. the link URL
el.is_displayed()       # True/False — is it visible on screen?


# ── STEP 4: WAITS (most important concept) ────────
# Problem: pages load slowly. If you find_element too early → crash.
# Solution: tell Selenium to WAIT until the element appears.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, timeout=10)  # wait UP TO 10 seconds

# "Wait until this element exists in the page"
el = wait.until(EC.presence_of_element_located((By.ID, "result")))

# "Wait until this element is visible AND clickable"
el = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))

# There is also a simpler global wait (less precise):
driver.implicitly_wait(10)  # every find_element will wait up to 10s automatically

# RULE: explicit WebDriverWait is better than implicitly_wait
# NEVER use time.sleep(2) in real tests — it is a hard-coded delay, always bad


# ── STEP 5: USEFUL DRIVER PROPERTIES ──────────────
driver.current_url   # the URL the browser is on right now
driver.title         # the page <title> text
driver.back()        # browser back button
driver.refresh()     # refresh the page


# ── STEP 6: DROPDOWNS ─────────────────────────────
# Regular <select> elements need a special wrapper
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("Poland")  # pick by what you see
dropdown.select_by_value("pl")             # pick by the HTML value attribute
dropdown.select_by_index(0)               # pick by position (0 = first)


# ── STEP 7: ALERTS (browser pop-ups) ──────────────
# JavaScript alert() pop-ups are NOT normal elements — handle them like this:
alert = driver.switch_to.alert
alert.accept()   # click OK
alert.dismiss()  # click Cancel
alert.text       # read the message


# ── COMMON ERRORS TO RECOGNISE ────────────────────
# NoSuchElementException       → element not found at all
# TimeoutException             → WebDriverWait ran out of time
# StaleElementReferenceException → found element, page refreshed, now it's gone
#                                  fix: find the element again
# ElementClickInterceptedException → something is covering the button you want to click
