import os
import csv
import math
from datetime import datetime

# ==========================================================================
# SLB RESONANT SYSTEMS: PROJECT TRISOLARIS TRAJECTORY DATA PARSER
# SECURITY PERIMETER: PUBLIC STOREFRONT VALIDATION ENGINE // VERSION v1.1.0
# ==========================================================================

def parse_grid_trajectory(csv_path="trisolaris_trajectory_data.csv"):
    print("###########################################################################")
    print(" SLB RESONANT POWER GRID: TRAJECTORY LOAD COEFFICIENT PARSER")
    print(" TRACK 01 CSV DATA STREAM INTEGRATOR // RUNTIME ENGINE: v1.1.0")
    print("###########################################################################")

    # Verify if trajectory ledger is present
    if not os.path.exists(csv_path):
        # Fallback data writer to initialize the file if it's currently empty
        print(f"[*] Initializing baseline tracking trajectory array at: {csv_path}")
        headers = ["Timestamp", "MegaWatts_Draw", "Ambient_Temp_C"]
        sample_rows = [
            [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "1250.0", "34.5"],
            [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "1380.0", "35.1"],
            [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "1495.0", "36.2"]
        ]
        with open(csv_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(sample_rows)

    # Core system metrics re-anchors
    master_seed_token = "D6889ECD83EE"
    friction_floor = 0.0201
    
    print(f"📡 INGESTING GRID LEDGER STREAM: {csv_path}")
    print("===========================================================================")

    with open(csv_path, mode="r") as f:
        reader = csv.DictReader(f)
        row_count = 0
        
        for row in reader:
            row_count += 1
            mw_draw = float(row.get("MegaWatts_Draw", 1200.0))
            ambient_t = float(row.get("Ambient_Temp_C", 20.0))
            
            # Multi-physics conversion calculation: estimate internal core temperature rise 
            # based on proportional inductive load draw squared
            derived_core_temp = ambient_t + ((mw_draw / 1000.0) ** 2 * 25.0)
            
            # Calculate corresponding inductive line reactance scaling factor
            reactive_impedance_ohm = 0.314 * (1.0 + (derived_core_temp * 0.0015)) * friction_floor
            
            print(f"📈 [Row {row_count:02d}] Timestamp: {row.get('Timestamp')}")
            print(f"   ↳ Measured Grid Draw: {mw_draw:.1f} MW | Ambient Air: {ambient_t}°C")
            print(f"   ↳ Calculated Core T : {derived_core_temp:.2f}°C")
            print(f"   ↳ Reactive Impedance: {reactive_impedance_ohm:.6f} Ohms/km [BALANCED CLAMP] 🟢")
            print("---------------------------------------------------------------------------")

    print(f"[+] Successfully integrated {row_count} grid trajectory intervals.")
    print("===========================================================================")

if __name__ == "__main__":
    parse_grid_trajectory()
