# ⚡ portscanpy

A minimal TCP port scanner written in Python using raw sockets. Inspired by hacker-style learning: no frameworks, no dependencies — just sockets and logic.

## 🎯 What It Does

- Takes an IP and port range as input
- Checks each TCP port to see if it's open
- Prints all open ports with timing
- CLI-only

## 🚀 Example

```bash
python3 scanner.py 192.168.0.1 20 100
