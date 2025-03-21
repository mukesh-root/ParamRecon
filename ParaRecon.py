import argparse
import subprocess
import threading
import os

def run_subfinder(target, wordlist, output_file):
    """Runs Subfinder for passive subdomain enumeration."""
    cmd = f"subfinder -d {target} -w {wordlist} -o {output_file}"
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[+] Subdomains saved to {output_file}")

def run_paramspider(target, output_file):
    """Runs ParamSpider to find endpoint parameters."""
    cmd = f"paramspider --domain {target} --output {output_file}"
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[+] Parameters saved to {output_file}")

def process_target(target, wordlist, threads):
    """Handles subdomain enumeration and parameter discovery for a single target."""
    subdomain_file = f"{target}_subdomains.txt"
    param_file = f"{target}_params.txt"
    
    run_subfinder(target, wordlist, subdomain_file)
    run_paramspider(target, param_file)

def main():
    parser = argparse.ArgumentParser(
        description="Pararecon - Passive Web Recon Tool",
        epilog="Example usage: python pararecon.py --target example.com --wordlist subdomains.txt --threads 10"
    )
    parser.add_argument("--target", required=True, help="Target domain to scan")
    parser.add_argument("--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("--threads", type=int, default=5, help="Number of threads to use (default: 5)")
    parser.add_argument("--help", action="help", help="Show this help message and exit")
    args = parser.parse_args()
    
    if not os.path.exists(args.wordlist):
        print("[Error] Wordlist file not found!")
        return
    
    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=process_target, args=(args.target, args.wordlist, args.threads))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("[+] Recon complete!")
    
if __name__ == "__main__":
    main()
