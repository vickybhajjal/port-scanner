import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        if s.connect_ex((host, port)) == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"

            print(f"[OPEN] Port {port} ({service})")
        # else:
        #     print(f"[CLOSED] Port {port}")

        s.close()

    except:
        pass


# User input
target = input("Enter target IP or hostname: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

try:
    host = socket.gethostbyname(target)
    print(f"\nScanning {target} ({host})...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

except socket.gaierror:
    print("Invalid hostname or IP address.")