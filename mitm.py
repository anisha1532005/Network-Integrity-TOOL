import subprocess

def get_gateway_mac():
    try:
        output = subprocess.check_output("arp -a", shell=True).decode().splitlines()

        for line in output:
            line = line.strip()

            if line.startswith("192.168.1.1"):
                parts = line.split()
                if len(parts) >= 2:
                    return parts[1]

        return None
    except:
        return None


def check_mitm(baseline_mac, current_mac):
    if baseline_mac != current_mac:
        return "POSSIBLE MITM"
    return "SAFE"
