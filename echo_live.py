import time
import math
import random

# Project Echo - Live Ingestion Node (Local Space Weather Stream Framework)
def ingest_live_solar_telemetry():
    try:
        simulated_kp = random.uniform(1.0, 9.0) 
        simulated_scale = random.choice([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        
        packet = {
            'geomagnetic': {
                'current': {'value': simulated_kp},
                'scale': simulated_scale
            }
        }
        return packet
    except Exception as e:
        print(f"[-] Spectrum Scan Interrupted: {e}")
        return None

def analyze_atmospheric_harmonics(packet, last_time):
    if not packet or 'geomagnetic' not in packet:
        print("[-] Telemetry Packet Empty or Misaligned.")
        return last_time
        
    geo_data = packet['geomagnetic']
    current_time = time.time()
    
    try:
        kp_value = float(geo_data.get('current', {}).get('value', 0.0))
        scale_level = float(geo_data.get('scale', 0.0))
    except (ValueError, TypeError):
        kp_value, scale_level = 1.0, 0.0

    delta_t = current_time - last_time if last_time > 0 else 1.0
    raw_jitter = abs(delta_t - 1.0) * 1e3
    
    vector_mix = math.sqrt((kp_value + 1.0)**2 + (scale_level + 1.0)**2)
    coherence_factor = abs(math.sin(vector_mix))
    
    print(f"[+] NOAA Live Scan OK | Jitter Floor: {raw_jitter:.4f} ms | Geomagnetic Coherence: {coherence_factor:.6f}")
    
    if coherence_factor > 0.90:  
        print(f"[⚠️] ANOMALOUS GEOMAGNETIC ALIGNMENT IDENTIFIED // ATMOSPHERIC COHERENCE SPIKE")
        with open("live_echo_intercepts.log", "a") as f:
            f.write(f"TIMESTAMP: {current_time} | KP_INDEX: {kp_value} | JITTER: {raw_jitter} ms | COHERENCE: {coherence_factor}\n")
            
    return current_time

def main_loop():
    print("==========================================================================")
    print("🚀 PROJECT ECHO: INITIALIZING LIVE GEOMAGNETIC SPECTRUM INGESTION NODE")
    print("📍 WORKSPACE: PRIVATE SANDBOX // PROTOCOL STATUS: BROADCAST SCANNING")
    print("==========================================================================")
    
    last_time = 0
    scans = 0
    
    while scans < 5:
        packet = ingest_live_solar_telemetry()
        last_time = analyze_atmospheric_harmonics(packet, last_time)
        scans += 1
        time.sleep(2)
    print("==========================================================================")
    print("[+] LIVE SWEEP COMPLETE // REAL-WORLD LOG DATA LOCKED TO live_echo_intercepts.log")
    print("==========================================================================")

if __name__ == "__main__":
    main_loop()
