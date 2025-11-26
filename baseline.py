import json
from datetime import datetime
from mitm import get_gateway_mac
from traceroute import run_traceroute

BASELINE_FILE = "baseline_network.json"

def create_baseline():
    gateway_mac = get_gateway_mac()
    hops = run_traceroute()

    baseline = {
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "gateway_mac": gateway_mac,
        "target_ip": "8.8.8.8",
        "traceroute": hops
    }

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    print("[+] Baseline saved.")
    print("[+] Gateway MAC:", gateway_mac)


def load_baseline():
    try:
        with open(BASELINE_FILE, "r") as f:
            return json.load(f)
    except:
        print("Baseline not found. Please create it first.")
        return None
