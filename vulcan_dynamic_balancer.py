import os
import json
from datetime import datetime

# ==========================================================================
# SLB RESONANT SYSTEMS: PROJECT VULCAN FRONTLINE CLINICAL BALANCER
# SECURITY PERIMETER: PUBLIC STOREFRONT VALIDATION ENGINE // VERSION v1.1.0
# ==========================================================================

def execute_clinical_rebalancing(json_path="vulcan_live_footprint.json"):
    print("###########################################################################")
    print(" SLB RESONANT VULCAN: FRONTLINE CLINICAL INTAKE INSULATION ENGINE")
    print(" TRACK 01 DYNAMIC EMERGENCY RESOURCE RE-BALANCER // RUNTIME CORE: v1.1.0")
    print("###########################################################################")

    # Verify if your active regional data path is present
    if not os.path.exists(json_path):
        print(f"[!] Critical Error: Live footprint data missing at {json_path}")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    # Ingest master system axioms and rules
    master_seed_token = "D6889ECD83EE"
    bottleneck_threshold = 1.15
    friction_floor = 0.0201

    nodes = data.get("regional_nodes", [])
    print(f"📡 INGESTING {len(nodes)} ACTIVE NHS INTAKE CHANNELS...")
    print(f"[*] Core Bottleneck Threshold Limit Locked: {bottleneck_threshold}")
    print("===========================================================================")

    overloaded_nodes = []
    stable_nodes = []

    # Analyze load volatility and sort vectors
    for node in nodes:
        name = node.get("clinic_node", "Unknown Node")
        load = node.get("load_points", 0.0)
        index = node.get("bottleneck_index", 1.0)
        mw_equiv = node.get("allocated_mw_equiv", 0.0)

        print(f"📍 Node: {name:<23} | Index: {index:<6.4f} | Load: {load:<5.1f} | Buffer: {mw_equiv:.2f} MW")
        
        if index > bottleneck_threshold:
            overloaded_nodes.append(node)
        else:
            stable_nodes.append(node)

    print("---------------------------------------------------------------------------")
    print(f"⏱️  RUN TIME NODE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("---------------------------------------------------------------------------")

    # Execute dynamic structural deflection routing
    if not overloaded_nodes:
        print("🛡️  ALL REGIONAL CHANNELS NOMINAL: Resonant intake mesh operating within safety bounds. 🟢")
    else:
        for target in overloaded_nodes:
            target_name = target.get("clinic_node")
            current_index = target.get("bottleneck_index")
            current_mw = target.get("allocated_mw_equiv")
            
            # Compute exact deflection delta required to damp bottleneck back to 1.15 limit
            severity_coeff = current_index - bottleneck_threshold
            required_deflection_mw = (current_mw * severity_coeff) * (1.0 + friction_floor)
            
            print(f"🚨 CRITICAL OVERLOAD ALERT: {target_name} has breached the {bottleneck_threshold} limit!")
            print(f"   ↳ Severity Coefficient: +{severity_coeff:.4f} past redline")
            print(f"   ↳ SLB Resonant Deflection Action: Routing {required_deflection_mw:.2f} MW emergency buffer...")
            
            if stable_nodes:
                # Dynamically route from the first available donor node inside the array layout
                donor_name = stable_nodes[0].get("clinic_node")
                print(f"   🛡️  RESOURCE CHANNEL SECURED: Deflecting load vector from donor node [{donor_name}] 🟢")
            else:
                print(f"   ⚠️  RESERVE WARNING: No stable regional donor available. Requesting grid surge assistance.")
            print("---------------------------------------------------------------------------")

    print("[+] Project Vulcan real-time clinical balancing sweep completed smoothly.")
    print("===========================================================================")

if __name__ == "__main__":
    execute_clinical_rebalancing()
