# # Selenium-based form tester
# # form_fuzzer.py

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Basic test payloads (can expand later)
# FUZZ_PAYLOADS = [
#     "<script>alert('XSS')</script>",
#     "' OR '1'='1",
#     "<img src=x onerror=alert('xss')>",
# ]

# def force_dismiss_alerts(driver):
#     while True:
#         try:
#             WebDriverWait(driver, 2).until(EC.alert_is_present())  # Wait if alert exists
#             alert = Alert(driver)
#             print(f"[!] Dismissing alert: {alert.text}")
#             alert.dismiss()
#             time.sleep(1)  # Brief pause to ensure alert closes properly
#         except:
#             break  # No alert remains, continue execution

# # def handle_alert(driver):
# #     try:
# #         WebDriverWait(driver, 2).until(EC.alert_is_present())  # Wait for alert to appear
# #         alert = Alert(driver)
# #         alert_text = alert.text
# #         print(f"[+] Alert detected: {alert_text}")
# #         alert.dismiss()  # Dismiss the alert
# #     except:
# #         pass  # No alert, continue
# #     except Exception as e:
# #         print(f"[-] Error handling alert: {e}")
# #         return False
# #     return True
# # # Fuzzing forms on the target URL

# def fuzz_forms(url):
#     # Setup headless browser
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")

#     driver = webdriver.Chrome(options=chrome_options)

#     driver.get(url)
#     time.sleep(2)  # Wait for JS forms to load if any

#     results = []

#     forms = driver.find_elements(By.TAG_NAME, "form")
#     print(f"\n[+] Found {len(forms)} form(s)")

#     for index, form in enumerate(forms, start=1):
#         print(f"\n[*] Fuzzing Form #{index}")

#         for payload in FUZZ_PAYLOADS:
#             try:
#                 force_dismiss_alerts(driver)

#                 form = driver.find_elements(By.TAG_NAME, "form")[index-1]  # Re-find the form before each payload
#                 inputs = form.find_elements(By.TAG_NAME, "input")  # Refresh element list

#                 for input_field in inputs:
#                     input_type = input_field.get_attribute("type")
#                     if input_type in ['text', 'search', 'email', 'url', 'password']:
#                         input_field.clear()
#                         input_field.send_keys(payload)

#                 force_dismiss_alerts(driver)

#                 form.submit()
#                 time.sleep(1)

#                 force_dismiss_alerts(driver)

#                 results.append({
#                     "form_number": index,
#                     "payload": payload,
#                     "result_url": driver.current_url
#                 })

#                 driver.get(url)  # Reload the page for the next payload
#                 time.sleep(2)

#             except Exception as e:
#                 print(f"[-] Error while fuzzing: {e}")
#                 driver.get(url)  # Reload page if interaction fails



#     driver.quit()
#     return results
# # form_fuzzer.py

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import traceback # Import traceback for detailed error messages
# import logging  # Import the logging module

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Basic test payloads (can expand later)
# FUZZ_PAYLOADS = [
#     "<script>alert('XSS')</script>",
#     "' OR '1'='1",
#     "<img src=x onerror=alert('xss')>",
# ]

# def force_dismiss_alerts(driver):
#     """Dismisses all present alerts."""
#     while True:
#         try:
#             WebDriverWait(driver, 2).until(EC.alert_is_present())
#             alert = Alert(driver)
#             logging.warning(f"[!] Dismissing alert: {alert.text}")  # Use logging
#             alert.dismiss()
#             time.sleep(1)
#         except:
#             break

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback # Import traceback for detailed error messages
import logging  # Import the logging module

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Basic test payloads (can expand later)
FUZZ_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "' OR '1'='1",
    "<img src=x onerror=alert('xss')>",
]

def force_dismiss_alerts(driver):
    """Dismisses all present alerts."""
    while True:
        try:
            WebDriverWait(driver, 2).until(EC.alert_is_present())
            alert = Alert(driver)
            logging.warning(f"[!] Dismissing alert: {alert.text}")  # Use logging
            alert.dismiss()
            time.sleep(1)
        except:
            break
        
def fuzz_forms(url):
    """Fuzzes input fields in forms on a given URL."""
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    try:
        driver = webdriver.Chrome(options=options) # Or .Firefox(), etc.
        driver.get(url)
        time.sleep(2)  # Give the page time to load

        results = []
        forms = driver.find_elements(By.TAG_NAME, "form")
        logging.info(f"\n[+] Found {len(forms)} form(s)") # Use logging

        if not forms:
            logging.info("[-] No forms found on this page.")
            return results  # Return empty list if no forms

        for index, form in enumerate(forms, start=1):
            logging.info(f"\n[*] Fuzzing Form #{index}")
            for payload in FUZZ_PAYLOADS:
                try:
                    force_dismiss_alerts(driver)
                    # Re-find form and inputs to avoid StaleElementReferenceException
                    form = driver.find_elements(By.TAG_NAME, "form")[index-1]
                    inputs = form.find_elements(By.TAG_NAME, "input")

                    if not inputs:
                        logging.warning(f"[-] Form #{index} has no inputs.")
                        continue  # Skip to the next payload

                    for input_field in inputs:
                        input_type = input_field.get_attribute("type")
                        if input_type in ['text', 'search', 'email', 'url', 'password']:
                            input_field.clear()
                            input_field.send_keys(payload)

                    force_dismiss_alerts(driver)
                    form.submit()
                    time.sleep(1)
                    force_dismiss_alerts(driver)

                    results.append({
                        "form_number": index,
                        "payload": payload,
                        "result_url": driver.current_url
                    })
                    driver.get(url)  # Reload the page for the next payload
                    time.sleep(2)

                except Exception as e:
                    logging.error(f"[-] Error fuzzing form {index} with payload '{payload}': {e}")
                    logging.error(traceback.format_exc()) # Log the traceback
                    driver.get(url) # try to continue
                    time.sleep(2)

        return results

    except Exception as e:
        logging.error(f"[-] Exception in fuzz_forms: {e}")
        logging.error(traceback.format_exc())
        return [] # Return empty list on error
    finally:
        if 'driver' in locals(): #check if the driver was initiated
           driver.quit()

if __name__ == "__main__":
    target_url = input("Enter the URL to fuzz: ")
    fuzz_results = fuzz_forms(target_url)
    if fuzz_results:
        for result in fuzz_results:
            print(f"Form #{result['form_number']}, Payload: {result['payload']}, URL: {result['result_url']}")
    else:
        print("No forms found or error occurred.")
