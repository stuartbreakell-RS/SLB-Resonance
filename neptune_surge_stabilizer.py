import os
import json
import math
import csv
from datetime import datetime

def run_neptune_hydraulic_audit(footprint_name="neptune_live_footprint.json", ledger_name="neptune_fidelity_ledger.csv"):
    """
    PROJECT NEPTUNE: UK Water Infrastructure Surge Calibration Matrix v1.2.0
    Dynamically ingests utility telemetry and logs execution vectors to an audited CSV ledger.
    """
    print("==========================================================================")
    print("🌊 PROJECT NEPTUNE: AUTOMATED HYDRAULIC LEDGER SYSTEM v1.2.0")
    print("==========================================================================")
    print("Utility Node        | Flow (m³/s) | Kinetic Load | Status         | Gate Phase Vector")
    print("--------------------------------------------------------------------------")

    # Establish absolute local environment paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, footprint_name)
    ledger_path = os.path.join(current_dir, ledger_name)
    
    if not os.path.exists(target_path):
        print(f" -> ERROR: Telemetry source file '{footprint_name}' missing in path.")
        print("==========================================================================")
        return

    # Ingest the active data footprint stream
    with open(target_path, "r") as f:
        nodes = json.load(f)

    friction_floor = 0.0201
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ledger_rows = []
    
    for node_data in nodes:
        node = node_data.get("utility_node", "Unknown Node")
        max_cap = float(node_data.get("capacity_max", 500.0))
        flow = float(node_data.get("live_flow", 100.0))
        chem_index = float(node_data.get("chemical_saturation_index", 1.0))
        
        # Calculate dynamic hydraulic friction ratio combined with compounding chemical density
        strain_index = (flow / max_cap) * 5.0
        
        # Apply exponential fluid back-pressure dampening if strain breaches critical threshold
        if strain_index > 4.0 or chem_index > 3.5:
            kinetic_load = max(1.0, (strain_index ** 1.9) * friction_floor * 15 * (chem_index * 0.5))
            status_flag = "SURGE WARNING"
            gate_vector = f"ADJUST PHASE BY {math.degrees(strain_index * 0.12):.2f}° // INVERSE OPEN"
        else:
            kinetic_load = strain_index * friction_floor * 5
            status_flag = "OPTIMAL SYSTEM"
            gate_vector = "HOLD BALANCED VECTOR"

        print(f" {node:<19} | {flow:<11.1f} | {kinetic_load:<12.4f} | {status_flag:<14} | {gate_vector}")
        
        # Store metadata track for spreadsheet export
        ledger_rows.append([
            timestamp, node, flow, max_cap, f"{kinetic_load:.4f}", status_flag, gate_vector
        ])

    print("--------------------------------------------------------------------------")
    
    # 📊 EXPORT TO STANDALONE CSV LEDGER
    file_exists = os.path.exists(ledger_path)
    try:
        with open(ledger_path, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            # If the ledger is brand new, write the tracking headers first
            if not file_exists:
                writer.writerow(["Timestamp", "Utility Node", "Live Flow (m3/s)", "Max Capacity", "Kinetic Load", "Status", "Gate Phase Vector"])
            writer.writerows(ledger_rows)
        print(f"💾 LEDGER SYNCED SECURELY -> {ledger_name} UPDATED SUCCESSFULLY")
    except Exception as e:
        print(f"[-] ERROR: Failed to write file ledger data. Detail: {e}")
        
    print("==========================================================================")

if __name__ == "__main__":
    run_neptune_hydraulic_audit()
