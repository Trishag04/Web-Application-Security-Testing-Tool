# Web-Application-Security-Testing-Tool

A Python-based web application security testing tool that integrates with **OWASP ZAP** and **Selenium** to scan websites for common vulnerabilities.

## 🛡️ Overview

This tool is designed for security professionals, developers, and testers to automate the process of scanning web applications for vulnerabilities like XSS, SQL Injection, and more. It uses OWASP ZAP in headless (daemon) mode and provides a simple CLI for testing any target URL.

## 🚀 Features

- Launches OWASP ZAP in daemon mode.
- Automatically crawls and scans the target web application.
- Uses Selenium to simulate realistic user interactions.
- Extracts and reports vulnerabilities via the ZAP API.
- Generates simple output for analysis or reporting.
- Cross-platform compatible (Windows, Linux, macOS).

## 🛠️ Technologies Used

- **Python 3.12+**
- **OWASP ZAP (Zed Attack Proxy)**
- **Selenium**
- **Requests**
- **ZAP Python API (python-owasp-zap-v2.4)**

## 📁 Project Structure

websec_tool/
│
├── main.py
├── scanner.py           # Basic headers, cookies info
├── form_fuzzer.py       # Selenium-based form tester
├── zap_scan.py          # OWASP ZAP API Integration
├── report.py            # Output results to file
├── requirements.txt




## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/websec_tool.git
cd websec_tool
```


### 2. nstall Python Dependencies
pip install -r requirements.txt


### 3. Download and Install OWASP ZAP
Download ZAP
Install it, and note the install path (e.g., C:\Program Files\ZAP\Zed Attack Proxy).


### 4. Start ZAP in Daemon Mode
Open PowerShell or terminal:

    cd "C:\Program Files\ZAP\Zed Attack Proxy"
    .\zap.bat -daemon -port 8090 -config api.key=changeme


▶️ **Usage:**
Once ZAP is running:
       
        python main.py


Then enter the target URL when prompted (e.g., http://testphp.vulnweb.com).
The tool will:
      Connect to the ZAP API.
      Crawl the site.
      Perform an active scan.
      Print results to the terminal


🙋‍♀️ **Contributing:**
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
