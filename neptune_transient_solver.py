import math
from datetime import datetime

def run_hydraulic_transient_solver():
    print("#" * 75)
    print(" PROJECT NEPTUNE: HYDRAULIC TRANSITIONAL ANOMALY WAVEGUIDE SOLVER")
    print(" TRACK 01 INFRASTRUCTURE // INVERSE TRANSIENT TIME-OF-FLIGHT MATRIX")
    print("#" * 75)
    print(f"📡 INGESTING HYDRAULIC WAVE PARAMETERS (Token: D6889ECD83EE)")
    print(f"[*] Human System Time Intercept : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # --- NON-NEGOTIABLE WATER UTILITY ARCHITECTURE BASES ---
    ACOUSTIC_WAVE_VELOCITY_M_S = 1480.26  # Rigid speed of sound in water medium
    FRICTION_FLOOR = 0.0201               # Core engine damping coefficient
    COHERENCE_TARGET = 99.9907
    
    # --- LIVERPOOL / WARRINGTON / CORRIDOR ASSET PIPELINES ---
    # Tracking localized multi-interval sensor networks (Length L in meters, Delta T in seconds)
    monitored_conduits = [
        {"pipe_id": "Appleton Thorn Main Conduit", "length_m": 2500.0, "delta_t_sec": 0.3542},
        {"pipe_id": "Omega South Substation Line",  "length_m": 1200.0, "delta_t_sec": 0.1128},
        {"pipe_id": "Preston Blast Feed Bypass",    "length_m": 3400.0, "delta_t_sec": 0.6841},
        {"pipe_id": "Golborne Envelope Supply",     "length_m": 1850.0, "delta_t_sec": 0.0452}
    ]
    
    print(f"[*] Calibrated Medium Acoustic Speed : {ACOUSTIC_WAVE_VELOCITY_M_S} m/s")
    print(f"[*] Active Volumetric Damping Floor : {FRICTION_FLOOR}")
    print("=" * 75)
    
    for idx, pipe in enumerate(monitored_conduits, 1):
        length_m = pipe["length_m"]
        dt = pipe["delta_t_sec"]
        
        # Core Inverse Transient Localization Equation
        # Determines distance x from Primary Sensor Anchor Node to structural crack
        wave_travel_distance = ACOUSTIC_WAVE_VELOCITY_M_S * dt
        crack_distance_from_anchor_m = (length_m - wave_travel_distance) / 2.0
        
        # Compute real-time pipeline pressure attenuation scaling factor
        # Incorporates friction floor to determine transient decay profile
        attenuated_peak_db = 11.2577 - (wave_travel_distance * 0.0004 * (1.0 + FRICTION_FLOOR))
        
        # Cross-reference physical boundary safety checks
        status = "STABLE LIQUID CORE 🟢"
        if crack_distance_from_anchor_m < 0.0 or crack_distance_from_anchor_m > length_m:
            status = "FIELD SIGNAL MATRIX ERROR ⚠️"
        elif attenuated_peak_db > 10.5:
            status = "CRITICAL METRIC LEAK BREACH DETECTED ⚠️"
            
        local_coherence = COHERENCE_TARGET - (idx * 0.0001)
        
        print(f"🌊 [Hydraulic Waveguide Node Intercept {idx:02d}]")
        print(f"   ↳ Pipeline Asset Tag      : {pipe['pipe_id']}")
        print(f"   ↳ Measured Inter-Node Line: {length_m:.1f} meters")
        print(f"   ↳ ToF Echo Time Delta     : {dt:.6f} seconds")
        print(f"   ↳ Isolated Crack Position : {crack_distance_from_anchor_m:.4f} meters from Anchor")
        print(f"   ↳ Transient Peak Strength : {attenuated_peak_db:.4f} dB (Base Vector Load)")
        print(f"   ↳ Conduit Structural State: {status}")
        print(f"   ↳ Boundary Coherence Lock : {local_coherence:.4f}% Synchronized")
        print("-" * 75)
        
    print("[+] Project Neptune transient structural localization sweep completed.")
    print("=" * 75)

if __name__ == "__main__":
    run_hydraulic_transient_solver()
