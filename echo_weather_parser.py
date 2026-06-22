import urllib.request
import json
import ssl

def fetch_environmental_matrix():
    print("==========================================================================")
    print("PROJECT ECHO: LOCAL GROUND METADATA ENVIRONMENTAL PARSER")
    print("==========================================================================")
    
    lat, lon = "53.3719", "-2.5517"
    url = f"https://open-meteo.com{lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,surface_pressure"
    
    print("[*] Pinging open public weather telemetry nodes for Grappenhall grid...")
    
    try:
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=context, timeout=5) as response:
            raw_bytes = response.read()
            decoded_str = raw_bytes.decode('utf-8', errors='ignore')
            data = json.loads(decoded_str)
            
        current_data = data['current']
        temp = float(current_data['temperature_2m'])
        humidity = float(current_data['relative_humidity_2m'])
        pressure = float(current_data['surface_pressure'])
        status_msg = "[+] Integration Successful: Live data active."
        
    except Exception:
        temp = 15.00
        humidity = 60.00
        pressure = 1013.25
        status_msg = "[-] Network Offline: Baseline parameters loaded."
        
    env_density_scalar = (pressure / 1013.25) * (1.0 + (temp / 100.0))
    
    print("")
    print("INTERCEPT AREA TROPOSPHERIC PROFILE")
    print("==========================================================================")
    print(f"-> Regional Surface Pressure:      {pressure:.2f} hPa")
    print(f"-> Local Thermal Baseline:         {temp:.2f} deg C")
    print(f"-> Relative Humidity Vector:       {humidity:.2f}%")
    print(f"-> Calculated Matrix Density:      {env_density_scalar:.6f}")
    print("==========================================================================")
    print(status_msg)
    print("==========================================================================")

if __name__ == "__main__":
    fetch_environmental_matrix()
