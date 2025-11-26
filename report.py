from datetime import datetime

REPORT_FILE = "network_integrity_report.txt"

def write_report(mitm_status, suspicious_hops, score, current_mac, baseline_mac):
    content = f"""
==================== NETWORK INTEGRITY REPORT ====================

Generated : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

MITM Status      : {mitm_status}
Baseline MAC     : {baseline_mac}
Current MAC      : {current_mac}

Suspicious Hops  : {len(suspicious_hops)}

"""

    for h in suspicious_hops:
        content += f"  Hop {h['hop']} → {h['ip']} ({h['delay_ms']} ms)\n"

    content += f"""
Final Score      : {score} / 100

===================================================================
"""

    with open(REPORT_FILE, "w") as f:
        f.write(content)

    print("\n[+] Report saved to:", REPORT_FILE)
