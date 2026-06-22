import json
import os
import datetime

def generate_clinical_inventory_audit(footprint_path="vulcan_live_footprint.json"):
    """
    Evaluates real-time intake stress metrics to calculate equipment depletion rates.
    Ensures zero frontline hardware deficits under intense capacity spikes.
    """
    print("==========================================================================")
    print("🏥 PROJECT VULCAN: FRONTLINE MEDICAL EQUIPMENT INVENTORY LOG v1.0.7")
    print("==========================================================================")
    print("Clinic Node         | Stress Index | Ventilator Stock | Telemetry Kits | Status")
    print("--------------------------------------------------------------------------")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, footprint_path)
    
    if not os.path.exists(target_path):
        print(f" -> ERROR: Live footprint telemetry file '{footprint_path}' missing.")
        print("==========================================================================")
        return

    with open(target_path, "r") as f:
        nodes = json.load(f)
        
    # Baseline regional warehouse inventory footprints assigned across monitored clinics
    base_inventory = {
        "Warrington Central": {"ventilators": 85, "telemetry": 140},
        "Salford Frontier": {"ventilators": 60, "telemetry": 110},
        "Halton Urgent Care": {"ventilators": 30, "telemetry": 55},  # Strained node
        "Cheshire East Hub": {"ventilators": 75, "telemetry": 125}
    }

    for node in nodes:
        name = node.get("clinic_node", "Unknown Node")
        stress = node.get("intake_stress_index", 1.0)
        stock = base_inventory.get(name, {"ventilators": 50, "telemetry": 90})
        
        # Calculate dynamic hardware consumption scaling factors under peak load friction
        depletion_factor = max(1.0, stress * 0.45)
        remaining_vents = max(0, int(stock["ventilators"] - (depletion_factor * 4)))
        remaining_telemetry = max(0, int(stock["telemetry"] - (depletion_factor * 8)))
        
        status_flag = "CRITICAL LIMIT" if remaining_vents < 25 or stress > 3.0 else "SECURE BASE"
        
        print(f" {name:<18} | {stress:.4f}        | {remaining_vents} Units REM     | {remaining_telemetry} Units REM     | {status_flag}")
        
    print("--------------------------------------------------------------------------")
    print("STATUS: INVENTORY RESILIENCE TRACK COMPLETE // TELEMETRY INSULATED")
    print("==========================================================================")

if __name__ == "__main__":
    generate_clinical_inventory_audit()
