import json
import os
import csv
import datetime

def evaluate_frontline_staffing_constraints(footprint_path="vulcan_live_footprint.json"):
    """
    Parses active clinical intake stress metrics, generates an emergency shift rotation grid,
    and logs critical resource transfers out to a physical CSV spreadsheet asset.
    """
    print("==========================================================================")
    print("🏥 PROJECT VULCAN: CLINICAL STAFFING SHIFT ROTATION ENGINE v1.0.7")
    print("==========================================================================")
    print("Clinic Node         | Intake Stress | Active Staff | Shift Units | Rotation Path")
    print("--------------------------------------------------------------------------")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, footprint_path)
    
    if not os.path.exists(target_path):
        print(f" -> ERROR: Live footprint telemetry file '{footprint_path}' missing.")
        print("==========================================================================")
        return

    with open(target_path, "r") as f:
        nodes = json.load(f)
        
    staff_allocations = {
        "Warrington Central": 42,
        "Salford Frontier": 38,
        "Halton Urgent Care": 24,  
        "Cheshire East Hub": 35
    }

    transfer_records = []
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for node in nodes:
        name = node.get("clinic_node", "Unknown Node")
        stress = node.get("intake_stress_index", 1.0)
        active_staff = staff_allocations.get(name, 30)
        
        required_staff = int(stress * 12.5)
        deficit = max(0, required_staff - active_staff)
        deficit_flag = "CRITICAL" if deficit > 0 or stress > 3.0 else "NOMINAL"
        
        staff_buffer = int(deficit + (stress * 2)) if deficit_flag == "CRITICAL" else 0
        
        if deficit_flag == "CRITICAL":
            rotation_path = "DRAW FROM WARRINGTON POOL"
            # Append record for local CSV audit staging
            transfer_records.append([current_timestamp, name, stress, staff_buffer, rotation_path])
        else:
            rotation_path = "HOLD STEADY BASELINE"
            
        print(f" {name:<18} | {stress:.4f}        | {active_staff} Active     | +{staff_buffer} Shift     | {rotation_path}")
        
    print("--------------------------------------------------------------------------")
    
    # Write transfer records out to an automated physical CSV spreadsheet layer
    csv_file_path = os.path.join(current_dir, "vulcan_shift_transfers.csv")
    try:
        file_exists = os.path.exists(csv_file_path)
        with open(csv_file_path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(["Timestamp", "Clinic Node", "Intake Stress Index", "Allocated Shift Units", "Rotation Routing Path"])
            for record in transfer_records:
                writer.writerow(record)
        print(" -> Open-Source Spreadsheet Log: vulcan_shift_transfers.csv UPDATED SUCCESFULLY")
    except Exception as e:
        print(f" -> Spreadsheet Log Export    : WRITE ERROR ({str(e)})")
        
    print("--------------------------------------------------------------------------")
    print("STATUS: SHIFT CONSTRICTIONS OVERRIDDEN // ROTATION MATRIX LOCKS GREEN")
    print("==========================================================================")

if __name__ == "__main__":
    evaluate_frontline_staffing_constraints()
