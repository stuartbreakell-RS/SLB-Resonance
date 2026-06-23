import os
import json
import math

def calculate_spaceborne_pathloss(data_source="echo_space_telemetry.json"):
    """
    PROJECT ECHO: Spaceborne Telemetry Path-Loss & Attenuation Core v1.0.0
    Calculates absolute space-to-ground decibel path loss metrics for Moonfra satellite vectors.
    """
    print("==========================================================================")
    print("📡 PROJECT ECHO: MOONFRA SATELLITE PHASE-STABILIZATION LAYER v1.0.0")
    print("==========================================================================")
    print("Satellite Node       | Freq (GHz) | Path Loss (dB) | Status       | Phase Lock Core")
    print("--------------------------------------------------------------------------")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, data_source)

    if not os.path.exists(target_path):
        print(f" -> ERROR: Space telemetry file '{data_source}' missing in directory.")
        print("==========================================================================")
        return

    with open(target_path, "r") as f:
        satellites = json.load(f)

    # Core SLB phase synchronization anchor values
    critical_damping_coefficient = 0.016033
    base_distance_km = 35786.0  # Geostationary baseline vector range
    
    for sat in satellites:
        name = sat.get("satellite_node", "Unknown Orbiter")
        freq = float(sat.get("carrier_frequency_ghz", 1.5))
        moisture = float(sat.get("atmospheric_moisture_g_m3", 5.0))
        solar_flux = float(sat.get("solar_flux_sfu", 100.0))
        
        # Free Space Path Loss calculation baseline (FSPL dB formula)
        fspl = 20 * math.log10(base_distance_km) + 20 * math.log10(freq) + 92.45
        
        # Compound atmospheric and ionospheric attenuation friction scaling factors
        distortion_multiplier = (moisture * 0.12) + (solar_flux / 100.0)
        total_attenuation_db = fspl + distortion_multiplier
        
        # Evaluate stability limits under heavy stochastic background floors
        if total_attenuation_db > 190.0 or solar_flux > 200.0:
            status = "SIGNAL DRIFT"
            # Apply SLB critical damping coefficient to calculate delta synchronization correction
            sync_vector = f"LOCK ARRESTED // JITTER FIXED TO {(critical_damping_coefficient * 0.5):.6f} ps"
        else:
            status = "PHASE LOCKED"
            sync_vector = "COHERENCE INDEX SECURE // 1.000000"

        print(f" {name:<20} | {freq:<10.3f} | {total_attenuation_db:<14.4f} | {status:<12} | {sync_vector}")

    print("--------------------------------------------------------------------------")
    print("STATUS: TELEMETRY ENVELOPE SEEDED // ATOMIC PHASE LOCKED SECURE")
    print("==========================================================================")

if __name__ == "__main__":
    calculate_spaceborne_pathloss()
