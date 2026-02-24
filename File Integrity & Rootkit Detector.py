import hashlib
import sys

def generate_fingerprint(data):
    # SHA-256 is a cryptographic hash function used in Blockchain and SSL
    return hashlib.sha256(data.encode()).hexdigest()

def main():
    # Simulated system files and their "Last Known Good" fingerprints
    baseline = {
        "/etc/passwd": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "/bin/login": "f2ca1bb6c7e907d06dafe4687e579fce76b3776e21e7c10b1ad9441c11f5997a"
    }

    # Current "Live" state of the files
    # Note: Someone added "hacker:123" to the passwd file!
    current_files = {
        "/etc/passwd": "root:admin, hacker:123", 
        "/bin/login": "system_login_v1.0"
    }

    print("--- Security Audit: File Integrity Monitor ---")
    print("Scanning critical system files for unauthorized modifications...\n")

    for file_path, content in current_files.items():
        current_hash = generate_fingerprint(content)
        expected_hash = baseline.get(file_path)

        print(f"Checking: {file_path}")
        
        if current_hash == expected_hash:
            print(f"  [OK] Integrity Verified.")
        else:
            print(f"  [!!] ALERT: INTEGRITY BREACH DETECTED!")
            print(f"       Expected: {expected_hash[:15]}...")
            print(f"       Actual:   {current_hash[:15]}...")
            print(f"       Status:   File has been tampered with or replaced.")
        print("-" * 50)

if __name__ == "__main__":
    main()