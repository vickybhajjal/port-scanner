# 🔍 Port Scanner Tool

A lightweight Python-based port scanner for ethical security testing and learning purposes.  
This tool allows you to quickly check open ports on a target host and identify running services.

---

## ✨ Features
- Scan a range of ports (default: 1–1024)
- Supports TCP connect scans
- Banner grabbing for common services
- JSON/CSV output for easy integration
- MIT License – free to use and modify

---

## 📦 Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/vickybhajjal/port-scanner.git
cd port-scanner
pip3 install -r requirements.txt

🚀 Usage
python3 port_scanner.py -H <target_host> -p <port_range>

Examples
# Scan common ports on example.com
python3 port_scanner.py -H example.com -p 21,22,80,443

# Scan full range on localhost
python3 port_scanner.py -H 127.0.0.1 -p 1-1024



