import datetime

def log_intruder(ip, username, password):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ALERT: Intruder from {ip} tried User: '{username}' Pwd: '{password}'"
    
    # In a real tool, this would write to a hidden security file
    with open("honeypot_log.txt", "a") as f:
        f.write(log_entry + "\n")
    return log_entry

def main():
    # This dictionary simulates a "vulnerable" system look
    fake_system_info = {
        "OS": "Ubuntu 18.04.1 LTS",
        "Kernel": "4.15.0-generic",
        "Service": "OpenSSH 7.6p1"
    }

    print("--- Cyber Deception: Honeypot Active ---")
    print(f"Service Emulation: {fake_system_info['Service']} on {fake_system_info['OS']}")
    print("Listening for incoming 'unauthorized' connections...\n")

    while True:
        print("CONNECTION REQUEST RECEIVED...")
        attacker_ip = "192.168.45.212" # Simulated dynamic IP
        
        user_input = input("login as: ")
        pass_input = input(f"{user_input}@{attacker_ip}'s password: ")

        # The Honeypot always rejects the password to keep the attacker trying
        # while we log every single attempt they make.
        alert = log_intruder(attacker_ip, user_input, pass_input)
        
        print("\n[SYSTEM] Access Denied.")
        print(f"[INTERNAL ADMIN MONITOR] {alert}")
        
        cont = input("\nContinue simulation? (y/n): ")
        if cont.lower() != 'y': break

if __name__ == "__main__":

    main()
