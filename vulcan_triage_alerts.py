import json
import os
import datetime

def scan_frontline_bottlenecks(data_path="vulcan_live_footprint.json", threshold=1.15):
    """
    Scans the open-source JSON telemetry layer for operational capacity breaches.
    Simulates direct text alert routing to field units when critical friction limits are passed.
    """
    print("==========================================================================")
    print(f"🚨 PROJECT VULCAN: FRONTLINE TRIAGE INCIDENT ALERT LAYER v1.0.7")
    print("==========================================================================")
    
    if not os.path.exists(data_path):
        print(f" -> ERROR: Target telemetry file '{data_path}' not found on disk.")
        print("==========================================================================")
        return

    try:
        with open(data_path, "r") as f:
            nodes = json.load(f)
    except Exception as e:
        print(f" -> ERROR: Failed to parse telemetry matrix data layer ({str(e)})")
        return

    breaches_detected = 0
    current_time = datetime.datetime.now().strftime("%H:%M:%S BST")

    for node in nodes:
        node_name = node.get("clinic_node", "Unknown Node")
        bottleneck = node.get("bottleneck_index", 0.0)
        priority = node.get("priority_index", 0.0)
        allocated_mw = node.get("allocated_mw_equiv", 0.0)

        # Evaluate real-time structural load breach condition
        if bottleneck > threshold:
            breaches_detected += 1
            print(f"\n[ALERT TRIGGERED // TIME: {current_time}]")
            print(f" ⚠️ NODE CRITICAL: {node_name} is operating at {bottleneck * 100:.1f}% capacity.")
            print(f" -> Severity Index : PRIORITY SCORE {priority:.4f} [OVERLOAD]")
            print(f" -> Action Routing : Routing automated text alert to Regional Field Commander...")
            print(f" -> Direct Payload : Injecting emergency {allocated_mw} MW Equiv resource buffer natively.")
            
    if breaches_detected == 0:
        print(f" -> Structural Scan Complete: All clinic nodes operating within normal parameters (<{threshold}).")
    else:
        print("\n--------------------------------------------------------------------------")
        print(f"STATUS: TRIAGE LIFELINE DISPATCHED // {breaches_detected} CRITICAL BREACHES ARRESTED NATIVELY")
        
    print("==========================================================================")

if __name__ == "__main__":
    scan_frontline_bottlenecks()
