# Pararecon - Passive Web Reconnaissance Tool

Pararecon is a Python-based passive reconnaissance tool that automates subdomain enumeration and endpoint parameter discovery. It leverages **Subfinder** for subdomain enumeration and **ParamSpider** for extracting endpoint parameters.

## Features
- 🕵️ Passive subdomain enumeration using **Subfinder**
- 🔍 Endpoint parameter discovery using **ParamSpider**
- 📄 Saves results in `.txt` files
- 🚀 Multi-threading support with a **custom thread limit**
- 🔧 Requires users to provide a **custom wordlist**

## Installation
Ensure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```
Install **Subfinder** and **ParamSpider** if they are not already installed:
```bash
sudo apt install subfinder  # For Linux
pip install paramspider
```

## Usage
Run Pararecon with the following command:
```bash
python pararecon.py --target example.com --wordlist subdomains.txt --threads 10
```

### Arguments:
- `--target` → The domain to scan (Required)
- `--wordlist` → Path to the wordlist file (Required)
- `--threads` → Number of threads to use (Default: 5)

## Output
- `example.com_subdomains.txt` → Contains all discovered subdomains
- `example.com_params.txt` → Contains extracted endpoint parameters

## Contribution
Feel free to fork and contribute by submitting a pull request!

## License
This project is open-source and available under the MIT License.

