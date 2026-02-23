import random
import time

def get_system_stats():
    # In a real app, we'd use the 'psutil' library
    # Here we simulate real-time hardware flux
    cpu_usage = random.randint(5, 95)
    ram_usage = random.randint(20, 80)
    temp = random.randint(40, 85)
    return cpu_usage, ram_usage, temp

def main():
    print("--- Live Hardware Monitor ---")
    print("Press Ctrl+C to stop monitoring\n")
    
    try:
        while True:
            cpu, ram, temp = get_system_stats()
            
            # Visual progress bars
            cpu_bar = "█" * (cpu // 5) + "-" * (20 - (cpu // 5))
            ram_bar = "█" * (ram // 5) + "-" * (20 - (ram // 5))
            
            print(f"CPU Usage: [{cpu_bar}] {cpu}%")
            print(f"RAM Usage: [{ram_bar}] {ram}%")
            print(f"Core Temp: {temp}°C")
            
            # Warning Logic
            if cpu > 90 or temp > 80:
                print("STATUS: [!!] CRITICAL OVERLOAD [!!]")
            else:
                print("STATUS: [OK] Normal")
                
            print