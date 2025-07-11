#!/usr/bin/env python3
import socket
import argparse
import time

def scan_port(host: str, port: int, timeout: float = 0.2) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        return result == 0
    
def main():
    parser = argparse.ArgumentParser(description="portscanpy - simple TCP port scanner")
    parser.add_argument("host", help="Target host to scan")
    parser.add_argument("start_port", type=int, help="Start of port range")
    parser.add_argument("end_port", type=int, help="End of port range")
    args = parser.parse_args()

    host = args.host
    start_port = args.start_port
    end_port = args.end_port

    print(f"Scanning {host} from port {start_port} to {end_port}...")
    start_time = time.time()

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    duration = time.time() - start_time
    print("\nScan completed.")
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")
    print(f"Time taken: {duration:.2f} seconds")

if __name__ == "__main__":
    main()