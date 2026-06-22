import json
import os

def evaluate_frontline_staffing_constraints(footprint_path="vulcan_live_footprint.json"):
    """
    Parses active clinical intake stress metrics and calculates localized shift 
    shortage constraints to prevent nursing and consultant burnout under peak loads.
    """
    print("==========================================================================")
    print("🏥 PROJECT VULCAN: CLINICAL STAFFING CONSTRAINT ALLOCATION ENGINE v1.0.7")
    print("==========================================================================")
    print("Clinic Node         | Intake Stress | Active Staff | Deficit Flag | Staff Buffer")
    print("--------------------------------------------------------------------------")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, footprint_path)
    
    if not os.path.exists(target_path):
        print(f" -> ERROR: Live footprint telemetry file '{footprint_path}' missing.")
        print("==========================================================================")
        return

    with open(target_path, "r") as f:
        nodes = json.load(f)
        
    # Standard baseline staffing footprints assigned across monitored clinic nodes
    staff_allocations = {
        "Warrington Central": 42,
        "Salford Frontier": 38,
        "Halton Urgent Care": 24,  # Understaffed priority node
        "Cheshire East Hub": 35
    }

    for node in nodes:
        name = node.get("clinic_node", "Unknown Node")
        stress = node.get("intake_stress_index", 1.0)
        active_staff = staff_allocations.get(name, 30)
        
        # Evaluate operational deficit threshold based on integrated stress weights
        required_staff = int(stress * 12.5)
        deficit = max(0, required_staff - active_staff)
        deficit_flag = "CRITICAL" if deficit > 0 or stress > 3.0 else "NOMINAL"
        
        # Calculate localized structural staff dispatch buffer
        staff_buffer = int(deficit + (stress * 2)) if deficit_flag == "CRITICAL" else 0
        
        print(f" {name:<18} | {stress:.4f}        | {active_staff} Active     | {deficit_flag:<12} | +{staff_buffer} Shift Units")
        
    print("--------------------------------------------------------------------------")
    print("STATUS: SHIFT CONSTRICTIONS OVERRIDDEN // FRONTLINE RESILIENCE LOCKED")
    print("==========================================================================")

if __name__ == "__main__":
    evaluate_frontline_staffing_constraints()
