# from zapv2 import ZAPv2
# import time

# ZAP_API_KEY = 'changeme'  # Replace with your actual key if needed
# ZAP_ADDRESS = 'localhost'
# ZAP_PORT = '8090'
# ZAP_API_URL = f'http://{ZAP_ADDRESS}:{ZAP_PORT}'

# # Connect to ZAP API endpoint
# zap = ZAPv2(apikey="changeme", proxies={"http": "http://localhost:8090", "https": "http://localhost:8090"})


# def run_zap_scan(target_url):
#     print(f"[*] Starting ZAP scan for {target_url}")

#     # Ensure ZAP is running
#     try:
#         version = zap.core.version
#         print(f"[+] Connected to ZAP v{version}")
#     except Exception as e:
#         print(f"[-] Connection error: {e}")
#         return []

#     # Open the target URL
#     try:
#         print("[*] Accessing target URL...")
#         zap.urlopen(target_url)
#         time.sleep(2)
#     except Exception as e:
#         print(f"[-] Error accessing {target_url}: {e}")
#         return []

#     # Spider the site
#     try:
#         print("[*] Spidering target...")
#         scan_id = zap.spider.scan(target_url)
#         if not scan_id.isdigit():
#             print("[-] Invalid spider scan ID received")
#             return []

#         while int(zap.spider.status(scan_id)) < 100:
#             print(f"[*] Spider progress: {zap.spider.status(scan_id)}%")
#             time.sleep(2)
#         print("[+] Spider completed")
#     except Exception as e:
#         print(f"[-] Spider scan failed: {e}")
#         return []

#     # Wait for passive scan to finish
#     try:
#         while int(zap.pscan.records_to_scan) > 0:
#             print(f"[*] Passive scanning... {zap.pscan.records_to_scan} records left")
#             time.sleep(2)
#     except Exception as e:
#         print(f"[-] Passive scan error: {e}")

#     # Active scan
#     try:
#         print("[*] Starting active scan...")
#         active_scan_id = zap.ascan.scan(target_url)
#         if not active_scan_id.isdigit():
#             print("[-] Invalid active scan ID received")
#             return []

#         while int(zap.ascan.status(active_scan_id)) < 100:
#             print(f"[*] Active scan progress: {zap.ascan.status(active_scan_id)}%")
#             time.sleep(5)
#         print("[+] Active scan completed")
#     except Exception as e:
#         print(f"[-] Active scan failed: {e}")
#         return []

#     # Get alerts
#     try:
#         print("[*] Fetching alerts...")
#         alerts = zap.core.alerts(baseurl=target_url)
#         print(f"[+] Found {len(alerts)} alerts")
#         return alerts
#     except Exception as e:
#         print(f"[-] Failed to fetch alerts: {e}")
#         return []



from zapv2 import ZAPv2
import time
import logging
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ZAP_API_KEY = 'hnferinlgukslbdag0vusaiqkh'  # Replace with your actual ZAP API key!
ZAP_ADDRESS = 'localhost'
ZAP_PORT = 8090
ZAP_API_URL = f'http://{ZAP_ADDRESS}:{ZAP_PORT}'

def run_zap_scan(target_url):
    """Performs a security scan of the target URL using OWASP ZAP."""
    logging.info(f"[*] Starting ZAP scan for {target_url}")
    
    try:
        # Connect to ZAP API
        zap = ZAPv2(
            apikey=ZAP_API_KEY,
            proxies={"http": f"http://{ZAP_ADDRESS}:{ZAP_PORT}", "https": f"http://{ZAP_ADDRESS}:{ZAP_PORT}"}
        )
        
        # Check if ZAP is running and the API is accessible
        try:
            version = zap.core.version
            logging.info(f"[+] Connected to ZAP version: {version}")
        except Exception as e:
            logging.error(f"[-] Error connecting to ZAP API: {e}")
            logging.error(traceback.format_exc())
            return []  # Return an empty list to indicate failure

        # Open the target URL
        try:
            logging.info("[*] Accessing target URL...")
            zap.urlopen(target_url)
            time.sleep(2)  # Allow time for the page to load
        except Exception as e:
            logging.error(f"[-] Error accessing target URL: {e}")
            logging.error(traceback.format_exc())
            return []

        # Spider the site
        try:
            logging.info("[*] Spidering target...")
            scan_id = zap.spider.scan(target_url)
            if not scan_id.isdigit():
                logging.error("[-] Invalid spider scan ID received from ZAP")
                return []

            while int(zap.spider.status(scan_id)) < 100:
                logging.info(f"[*] Spider progress: {zap.spider.status(scan_id)}%")
                time.sleep(5)
            logging.info("[+] Spider completed")
        except Exception as e:
            logging.error(f"[-] Spider scan failed: {e}")
            logging.error(traceback.format_exc())
            return []

        # Passive Scan
        try:
            while int(zap.pscan.records_to_scan) > 0:
                logging.info(f"[*] Passive scanning... Records left: {zap.pscan.records_to_scan}")
                time.sleep(5)
            logging.info("[+] Passive scan completed.")
        except Exception as e:
            logging.error(f"[-] Error during passive scan: {e}")
            logging.error(traceback.format_exc())

        # Active scan
        try:
            logging.info("[*] Starting active scan...")
            active_scan_id = zap.ascan.scan(target_url)
            if not active_scan_id.isdigit():
                logging.error("[-] Invalid active scan ID from ZAP")
                return []

            while int(zap.ascan.status(active_scan_id)) < 100:
                logging.info(f"[*] Active scan progress: {zap.ascan.status(active_scan_id)}%")
                time.sleep(10)
            logging.info("[+] Active scan completed")
        except Exception as e:
            logging.error(f"[-] Active scan failed: {e}")
            logging.error(traceback.format_exc())
            return []

        # Get the alerts
        try:
            logging.info("[*] Fetching alerts...")
            alerts = zap.core.alerts(baseurl=target_url)
            return alerts
        except Exception as e:
            logging.error(f"[-] Error retrieving alerts: {e}")
            logging.error(traceback.format_exc())
            return []
    
    except Exception as e:
        logging.critical(f"[-] Exception in run_zap_scan: {e}")
        logging.critical(traceback.format_exc())
        return []
    
    finally:
        try:
            zap.core.shutdown()
        except Exception as e:
            logging.warning(f"[-] Error during ZAP shutdown: {e}")



