# # main.py

# from scanner import basic_scan
# from form_fuzzer import fuzz_forms
# from zap_scan import run_zap_scan
# from report import generate_report

# def main():
#     target_url = input("Enter target URL (with http/https): ").strip()
    
#     print("\n[+] Starting Basic Recon...")
#     headers, cookies = basic_scan(target_url)

#     print("\n[+] Scanning Forms & Fuzzing Inputs...")
#     fuzz_results = fuzz_forms(target_url)

#     print("\n[+] Running OWASP ZAP Scan...")
#     zap_results = run_zap_scan(target_url)

#     print("\n[+] Generating Report...")
#     generate_report(target_url, headers, cookies, fuzz_results, zap_results)


# if __name__ == "__main__":
#     main()

# # if __name__ == "__main__":
# #     url = input("Enter the URL: ")
# #     results = run_zap_scan(url)
# #     for alert in results:
# #         print(f"{alert['risk']}: {alert['alert']} - {alert['url']}")


from scanner import basic_scan
from form_fuzzer import fuzz_forms
from zap_scan import run_zap_scan
from report import generate_report
import logging
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    target_url = input("Enter target URL (with http/https): ").strip()
    
    logging.info("\n[+] Starting Basic Recon...")
    try:
        scan_results = basic_scan(target_url) # Change here
        headers = scan_results.get("headers", {})
        cookies = scan_results.get("cookies", {})
    except Exception as e:
        logging.error(f"Basic scan failed: {e}")
        logging.error(traceback.format_exc())
        headers = {}
        cookies = {}

    logging.info("\n[+] Scanning Forms & Fuzzing Inputs...")
    try:
        fuzz_results = fuzz_forms(target_url)
    except Exception as e:
        logging.error(f"Form fuzzing failed: {e}")
        logging.error(traceback.format_exc())
        fuzz_results = []

    logging.info("\n[+] Running OWASP ZAP Scan...")
    try:
        zap_results = run_zap_scan(target_url)
    except Exception as e:
        logging.error(f"ZAP scan failed: {e}")
        logging.error(traceback.format_exc())
        zap_results = []

    logging.info("\n[+] Generating Report...")
    try:
        generate_report(target_url, headers, cookies, fuzz_results, zap_results)
    except Exception as e:
        logging.error(f"Report generation failed: {e}")
        logging.error(traceback.format_exc())
        

if __name__ == "__main__":
    main()