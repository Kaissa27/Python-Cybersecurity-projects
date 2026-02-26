import time

# Base class for all security events
class SecurityEvent:
    def __init__(self, source_ip, event_type, severity):
        self.source_ip = source_ip
        self.event_type = event_type
        self.severity = severity
        self.timestamp = time.time()

# The SIEM Engine - Demonstrates State Management and Correlation
class SIEM:
    def __init__(self):
        self.event_history = []
        self.threat_threshold = 3 # 3 related events = 1 incident

    def ingest_event(self, event):
        print(f"[*] SIEM Logged: {event.event_type} from {event.source_ip}")
        self.event_history.append(event)
        self._correlate_events(event.source_ip)

    def _correlate_events(self, ip):
        # Look for patterns (same IP doing different bad things)
        recent_activity = [e for e in self.event_history if e.source_ip == ip]
        
        if len(recent_activity) >= self.threat_threshold:
            self._trigger_incident_report(ip, recent_activity)

    def _trigger_incident_report(self, ip, activities):
        print(f"\n[!!!] INCIDENT ALERT [!!!]")
        print(f"CRITICAL: Multi-stage attack detected from {ip}")
        print(f"Attack Pattern: {' -> '.join([a.event_type for a in activities])}")
        print("ACTION: Isolating host and notifying SOC Team.\n")

def main():
    siem_engine = SIEM()

    # Simulating a "Kill Chain" attack: 
    # 1. Scanning -> 2. Password Guessing -> 3. Data Export
    malicious_activity = [
        SecurityEvent("192.168.10.50", "PORT_SCAN", "Low"),
        SecurityEvent("192.168.10.50", "FAILED_LOGIN", "Medium"),
        SecurityEvent("192.168.10.50", "DATA_EXFILTRATION", "High")
    ]

    print("--- SOC Security Lab: SIEM Correlation Engine ---")
    for attack_step in malicious_activity:
        time.sleep(1) # Simulating time passing between attack phases
        siem_engine.ingest_event(attack_step)

if __name__ == "__main__":
    main()