import http.client
import sys

def check_path(domain, path):
    try:
        # Create a connection to the server
        conn = http.client.HTTPSConnection(domain, timeout=2)
        # Send a HEAD request (faster than GET as it doesn't download the page content)
        conn.request("HEAD", path)
        response = conn.getresponse()
        conn.close()
        return response.status
    except Exception:
        return None

def main():
    # TARGET: Using a common public domain for demonstration 
    # In a real scenario, you'd use your own test server
    target_domain = "www.google.com" 
    
    # "Wordlist" of common sensitive directories
    wordlist = [
        "/admin", "/login", "/config", "/api", "/backup", 
        "/.env", "/robots.txt", "/server-status", "/dashboard"
    ]

    print(f"--- Web Reconnaissance: Directory Fuzzer ---")
    print(f"Target Domain: {target_domain}\n")

    for path in wordlist:
        status = check_path(target_domain, path)
        
        if status == 200:
            print(f"[+] FOUND: {path:<15} | Status: 200 (OK)")
        elif status == 301 or status == 302:
            print(f"[*] REDIRECT: {path:<12} | Status: {status}")
        elif status == 403:
            print(f"[!] FORBIDDEN: {path:<11} | Status: 403 (Protected)")
        # We ignore 404 (Not Found) to keep the output clean

    print("\nScan complete. Finding forbidden or hidden paths is key to web pentesting.")

if __name__ == "__main__":
    main()