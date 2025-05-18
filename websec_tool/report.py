# # Output results to file

# # report.py

# import json
# from datetime import datetime

# def generate_report(target_url, headers, cookies, fuzz_results, zap_results, output_file="scan_report.txt"):

#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write(f"===== Web Application Security Scan Report =====\n")
#         f.write(f"Target URL: {target_url}\n")
#         f.write(f"Scan Time: {timestamp}\n\n")

#         # FORM FUZZING RESULTS
#         f.write("---- Form Fuzzing Results ----\n")
#         if not fuzz_results:
#             f.write("No forms or vulnerabilities detected during fuzzing.\n\n")
#         else:
#             for result in fuzz_results:
#                 f.write(f"Form #{result['form_number']}:\n")
#                 f.write(f"  Payload: {result['payload']}\n")
#                 f.write(f"  Result URL: {result['result_url']}\n")
#                 f.write("\n")

#         # ZAP RESULTS
#         f.write("---- ZAP Vulnerability Scan ----\n")
#         if not zap_results:
#             f.write("No alerts reported by ZAP.\n")
#         else:
#             for alert in zap_results:
#                 f.write(f"Alert: {alert.get('alert', 'Unknown')}\n")
#                 f.write(f"Risk Level: {alert.get('risk', 'N/A')}\n")
#                 f.write(f"URL: {alert.get('url', 'N/A')}\n")
#                 f.write(f"Description: {alert.get('description', '')}\n")
#                 f.write(f"Solution: {alert.get('solution', '')}\n")
#                 f.write("-" * 50 + "\n")

#     print(f"\n[+] Report saved to: {output_file}")


import json
from datetime import datetime
import logging
import traceback # Import traceback

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_report(target_url, headers, cookies, fuzz_results, zap_results, output_file="scan_report.txt"):
    """Generates a report of the scan results."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"===== Web Application Security Scan Report =====\n")
            f.write(f"Target URL: {target_url}\n")
            f.write(f"Scan Time: {timestamp}\n\n")

            # BASIC SCAN RESULTS
            f.write("---- Basic Scan Results ----\n")
            f.write(f"Headers:\n{json.dumps(headers, indent=2)}\n")
            f.write(f"Cookies:\n{json.dumps(cookies, indent=2)}\n\n")

            # FORM FUZZING RESULTS
            f.write("---- Form Fuzzing Results ----\n")
            if not fuzz_results:
                f.write("No forms or vulnerabilities detected during fuzzing.\n\n")
            else:
                for result in fuzz_results:
                    f.write(f"Form #{result['form_number']}:\n")
                    f.write(f"  Payload: {result['payload']}\n")
                    f.write(f"  Result URL: {result['result_url']}\n")
                    f.write("\n")

            # ZAP RESULTS
            f.write("---- ZAP Vulnerability Scan ----\n")
            if not zap_results:
                f.write("No alerts reported by ZAP.\n")
            else:
                for alert in zap_results:
                    f.write(f"Alert: {alert.get('alert', 'Unknown')}\n")
                    f.write(f"Risk Level: {alert.get('risk', 'Unknown')}\n")
                    f.write(f"Confidence: {alert.get('confidence', 'Unknown')}\n")
                    f.write(f"URL: {alert.get('url', 'N/A')}\n")
                    f.write("\n")
        logging.info(f"[+] Report generated successfully at {output_file}")

    except Exception as e:
        logging.error(f"[-] Error generating report: {e}")
        logging.error(traceback.format_exc())