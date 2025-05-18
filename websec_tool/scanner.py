# # Basic headers, cookies info
# # scanner.py

# import requests
# import json

# def basic_scan(url):
#     try:
#         response = requests.get(url, timeout=10)
#         headers = response.headers
#         cookies = response.cookies

#         # Print headers in structured format
#         print("\n[+] Headers:")
#         print(json.dumps(dict(headers), indent=2))

#         # Print cookies in structured format
#         print("\n[+] Cookies:")
#         if cookies:
#             cookies_dict = {cookie.name: cookie.value for cookie in cookies}
#             print(json.dumps(cookies_dict, indent=2))
#         else:
#             print("No cookies found.")

#         # Return data in a structured format
#         return {"headers": dict(headers), "cookies": {cookie.name: cookie.value for cookie in cookies}}

#     except requests.exceptions.ConnectionError:
#         print("[!] Connection error—unable to reach the target.")
#     except requests.exceptions.Timeout:
#         print("[!] Timeout error—the request took too long.")
#     except requests.exceptions.HTTPError as e:
#         print(f"[!] HTTP error: {e}")
#     except requests.exceptions.RequestException as e:
#         print(f"[!] General request error: {e}")

#     return {"headers": {}, "cookies": {}}

# if __name__ == "__main__":
#     url = input("Enter the URL: ")
#     basic_scan(url)


import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def basic_scan(url):
    """Performs a basic scan of a given URL to retrieve headers and cookies."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        headers = response.headers
        cookies = response.cookies
        
        #check if there are any headers or cookies
        if not headers:
            logging.warning("No headers found.")
        if not cookies:
            logging.warning("No cookies found.")

        # Return data in a structured format
        return {"headers": dict(headers), "cookies": {cookie.name: cookie.value for cookie in cookies}}

    except requests.exceptions.ConnectionError:
        logging.error("[!] Connection error—unable to reach the target.")
        return {"headers": {}, "cookies": {}}
    except requests.exceptions.Timeout:
        logging.error("[!] Timeout error—the request took too long.")
        return {"headers": {}, "cookies": {}}
    except requests.exceptions.HTTPError as e:
        logging.error(f"[!] HTTP error: {e}")
        return {"headers": {}, "cookies": {}}
    except requests.exceptions.RequestException as e:
        logging.error(f"[!] General request error: {e}")
        return {"headers": {}, "cookies": {}}

if __name__ == "__main__":
    url = input("Enter the URL: ")
    results = basic_scan(url)
    print(json.dumps(results, indent=2)) # Print the results