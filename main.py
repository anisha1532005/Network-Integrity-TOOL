from baseline import create_baseline, load_baseline
from mitm import get_gateway_mac, check_mitm
from traceroute import run_traceroute, analyze_hops
from report import write_report

def run_integrity_check():
    baseline = load_baseline()
    if baseline is None:
        return

    baseline_mac = baseline["gateway_mac"]

    current_mac = get_gateway_mac()

    mitm_status = check_mitm(baseline_mac, current_mac)

    current_hops = run_traceroute()
    suspicious = analyze_hops(current_hops)

    score = 100
    if mitm_status != "SAFE":
        score -= 40
    score -= len(suspicious) * 10
    if score < 0:
        score = 0

    write_report(mitm_status, suspicious, score, current_mac, baseline_mac)

    print("\n=== INTEGRITY CHECK RESULT ===")
    print("MITM Status:", mitm_status)
    print("Suspicious Hops:", len(suspicious))
    print("Final Score:", score)


print("""
===========================================
        NETWORK INTEGRITY CLI TOOL
===========================================
1. Create Baseline
2. Run Integrity Check
3. Exit
""")

choice = input("Choose option: ")

if choice == "1":
    create_baseline()
elif choice == "2":
    run_integrity_check()
else:
    print("Goodbye!")
