import subprocess

def run_traceroute(target_ip="8.8.8.8"):
    try:
        output = subprocess.check_output(f"tracert {target_ip}", shell=True).decode().splitlines()
        hops = []

        for line in output:
            line = line.strip()
            if not line or line.startswith("Tracing") or line[0].isalpha():
                continue

            parts = line.split()

            if parts[0].isdigit():
                hop_number = int(parts[0])

                delay_ms = 0
                for p in parts:
                    if "ms" in p:
                        try:
                            delay_ms = int(p.replace("ms", "").replace("<", ""))
                            break
                        except:
                            pass

                hop_ip = parts[-1]

                hops.append({
                    "hop": hop_number,
                    "ip": hop_ip,
                    "delay_ms": delay_ms
                })

        return hops
    except:
        return []


def analyze_hops(hops):
    suspicious = []
    for h in hops:
        if h["delay_ms"] > 200:
            suspicious.append(h)
    return suspicious
