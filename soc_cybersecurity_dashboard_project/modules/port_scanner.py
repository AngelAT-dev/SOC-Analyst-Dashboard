import socket

def scan_ports(target):
    result_text = "Scanning ports...\n"
    open_ports = []

    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

        s.close()

    if open_ports:
        for p in open_ports:
            result_text += f"Port {p} OPEN\n"
    else:
        result_text += "No open ports found\n"

    return result_text