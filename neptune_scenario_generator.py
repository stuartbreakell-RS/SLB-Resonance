import json
import random
from datetime import datetime

# ==========================================================================
# SLB RESONANT SYSTEMS: PROJECT NEPTUNE DYNAMIC SCENARIO GENERATOR
# SECURITY PERIMETER: PUBLIC STOREFRONT VALIDATION ENGINE // VERSION v1.1.0
# ==========================================================================

def generate_network_stress_scenario(output_path="neptune_live_footprint.json"):
    print("###########################################################################")
    print(" SLB RESONANT INFRASTRUCTURE: HYDRAULIC NETWORK SCENARIO GENERATOR")
    print(" TRACK 01 PIPELINE DYNAMICS STRESS MODULATOR // RUNTIME ENGINE: v1.1.0")
    print("###########################################################################")

    # Master metric envelopes
    master_seed_token = "D6889ECD83EE"
    friction_floor = 0.0201
    
    # Northwest operational nodes to dynamically fluctuate
    base_zones = {
        "MERSEY_CORE": {"base_surge": 120.0},
        "GREATER_MCR": {"base_surge": 135.0},
        "CHESHIRE_W":  {"base_surge": 110.0},
        "LANCASHIRE_S": {"base_surge": 125.0}
    }

    print(f"[*] Simulating sudden pump trips and environmental grid pressure shifts...")
    
    updated_footprint = {}
    for zone, data in base_zones.items():
        # Inject realistic hydraulic volatility factor (+/- 15% grid load fluctuation)
        volatility_multiplier = random.uniform(0.85, 1.15)
        calculated_surge = round(data["base_surge"] * volatility_multiplier, 1)
        
        updated_footprint[zone] = {
            "surge_ceiling": calculated_surge,
            "damp_constant": friction_floor,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"   ↳ Modulating {zone:<14} -> New Dynamic Surge Ceiling: {calculated_surge:>5.1f} PSI")

    # Safely overwrite the local JSON storage layer
    with open(output_path, "w") as f:
        json.dump(updated_footprint, f, indent=4)

    print("---------------------------------------------------------------------------")
    print(f"[+] Dynamic scenario successfully written to: {output_path}")
    print("===========================================================================")

if __name__ == "__main__":
    generate_network_stress_scenario()
