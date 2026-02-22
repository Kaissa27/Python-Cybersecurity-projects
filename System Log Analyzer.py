import sys

def analyze_logs(log_data):
    report = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "IP_COUNTS": {}
    }
    
    for entry in log_data:
        # Split log format: "TIMESTAMP | LEVEL | IP | MESSAGE"
        parts = entry.split(" | ")
        if len(parts) < 4: continue
        
        level = parts[1]
        ip = parts[2]
        
        # Count Log Levels
        if level in report:
            report[level] += 1
            
        # Track IP Frequency
        report["IP_COUNTS"][ip] = report["IP_COUNTS"].get(ip, 0) + 1
            
    return report

def main():
    # Simulated log file content
    raw_logs = [
        "2026-02-22 10:00 | INFO | 192.168.1.1 | User login successful",
        "2026-02-22 10:05 | ERROR | 10.0.0.5 | Database connection failed",
        "2026-02-22 10:10 | WARNING | 192.168.1.1 | Disk space at 90%",
        "2026-02-22 10:15 | ERROR | 10.0.0.5 | Unauthorized access attempt",
        "2026-02-22 10:20 | INFO | 172.16.0.4 | Update check completed",
        "2026-02-22 10:25 | ERROR | 10.0.0.5 | Failed password attempt"
    ]

    print("--- Log Analysis Report ---")
    results = analyze_logs(raw_logs)
    
    print(f"Total Errors Found: {results['ERROR']}")
    print(f"Total Warnings:    {results['WARNING']}")
    print(f"Total Info Logs:   {results['INFO']}")
    
    print("\nTraffic by IP Address:")
    for ip, count in results["IP_COUNTS"].items():
        alert = " [!] HIGH ACTIVITY" if count > 2 else ""
        print(f"- {ip}: {count} hits{alert}")

if __name__ == "__main__":
    main()