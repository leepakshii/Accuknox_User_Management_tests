"""
System Health Monitoring Script
--------------------------------
This script checks basic system health metrics:
- CPU usage
- Memory usage
- Disk usage

If any metric crosses a safe limit, it prints a warning message.

Libraries Used:
- psutil: For system information (CPU, memory, disk)
"""

import psutil
from datetime import datetime

# Define safe threshold limits
CPU_LIMIT = 80      # in percentage
MEMORY_LIMIT = 80   # in percentage
DISK_LIMIT = 80     # in percentage

def check_system_health():
    # Fetch system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Print system status with timestamp
    print("\n----------------------------------------")
    print(" System Health Report -", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("----------------------------------------")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")
    print("----------------------------------------")

    # Check if any threshold is exceeded
    if cpu_usage > CPU_LIMIT:
        print("⚠️  Warning: High CPU Usage Detected!")
    if memory_usage > MEMORY_LIMIT:
        print("⚠️  Warning: Memory Usage Exceeded Limit!")
    if disk_usage > DISK_LIMIT:
        print("⚠️  Warning: Low Disk Space!")

    # If everything is fine
    if cpu_usage <= CPU_LIMIT and memory_usage <= MEMORY_LIMIT and disk_usage <= DISK_LIMIT:
        print("✅ All system parameters are within safe limits.")

if __name__ == "__main__":
    check_system_health()
