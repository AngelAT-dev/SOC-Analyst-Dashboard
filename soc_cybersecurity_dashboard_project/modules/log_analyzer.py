from collections import Counter

def analyze_logs(file):
    with open(file, "r") as f:
        lines = f.readlines()

    ips = []

    for line in lines:
        parts = line.split()
        if parts:
            ips.append(parts[0])

    counter = Counter(ips)

    output = "Security Log Analysis\n\n"

    for ip, count in counter.items():
        if count > 5:
            output += f"ALERT: suspicious activity from {ip} ({count} requests)\n"
        else:
            output += f"{ip} -> {count} requests\n"

    return output