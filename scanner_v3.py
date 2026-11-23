import socket
import ipaddress
import errno
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Common service names
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    111: "RPCbind",
    139: "NetBIOS",
    445: "SMB",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"
}

# Function to scan one port
def scan_port(target, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            service = services.get(port, "Unknown")
            return port, "OPEN", service

        elif result == errno.ECONNREFUSED:
            return port, "CLOSED", "-"

        else:
            return port, "NO RESPONSE", "-"

    except OSError:
        return port, "ERROR", "-"

    finally:
        sock.close()


print("=" * 60)
print("          PYTHON NETWORK SCANNER V3")
print("              MULTITHREADED")
print("=" * 60)

# Get target IP
target = input("Enter target IP address: ")

try:
    ipaddress.ip_address(target)
except ValueError:
    print("Invalid IP address!")
    raise SystemExit

# Get port range
try:
    start_port = int(input("Starting port: "))
    end_port = int(input("Ending port: "))

    if not (1 <= start_port <= end_port <= 65535):
        print("Invalid port range!")
        raise SystemExit

except ValueError:
    print("Enter valid port numbers!")
    raise SystemExit

# Thread configuration
MAX_WORKERS = 100

print("\nTarget:", target)
print("Ports:", start_port, "-", end_port)
print("Threads:", MAX_WORKERS)

start_time = time.time()

print("\nScan started:", datetime.now())
print("-" * 60)

results = []

# Create thread pool
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

    futures = [
        executor.submit(scan_port, target, port)
        for port in range(start_port, end_port + 1)
    ]

    # Collect completed scan results
    for future in as_completed(futures):
        results.append(future.result())

# Sort results by port number
results.sort()

# Display results
for port, status, service in results:

    if status == "OPEN":
        print(f"[+] Port {port:<7} {status:<12} {service}")

# Calculate statistics
open_count = sum(1 for r in results if r[1] == "OPEN")
closed_count = sum(1 for r in results if r[1] == "CLOSED")
other_count = len(results) - open_count - closed_count

end_time = time.time()
duration = end_time - start_time

print("-" * 60)
print("SCAN SUMMARY")
print("-" * 60)

print("Total ports scanned:", len(results))
print("Open ports:", open_count)
print("Closed ports:", closed_count)
print("No response / errors:", other_count)
print("Scan duration: {:.2f} seconds".format(duration))

print("\nScan completed:", datetime.now())
print("=" * 60)
