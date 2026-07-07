#!/usr/bin/env python3
"""
SLB RESONANT SYSTEMS - PROJECT TRITON (v1.2.0 Trajectory)
STS BERTH CRANE WIND-SHEAR STRUCTURAL JITTER SOLVER
CONFIDENTIAL // OFFLINE MOTHERSHIP LAB // NO DEPLOYMENT FOOTPRINT
"""

import numpy as np

class CraneJitterEngine:
    def __init__(self, structural_stiffness_kn_m=4500.0):
        self.k_structure = structural_stiffness_kn_m  # Structural rigidity of crane boom (kN/m)
        self.air_density = 1.225                       # kg/m^3 sea level baseline
        self.gantry_exposed_area_m2 = 145.0            # Exposed surface area of the upper crane frame
        self.drag_coefficient_steel = 1.3              # Structural drag index
        
    def compute_structural_deflection(self, wind_velocity_knots, load_mass_kg=40000.0):
        """Calculate high-frequency visual targeting alignment deviations under wind-shear spikes."""
        # Convert knots to m/s (1 knot = 0.514444 m/s)
        wind_m_s = wind_velocity_knots * 0.514444
        
        # 1. Compute Aerodynamic Drag Force: F_drag = 0.5 * rho * V^2 * Cd * A
        aerodynamic_force_n = 0.5 * self.air_density * (wind_m_s ** 2) * self.drag_coefficient_steel * self.gantry_exposed_area_m2
        aerodynamic_force_kn = aerodynamic_force_n / 1000.0
        
        # 2. Dynamic mechanical load contribution (40t container hoisting inertia)
        hoist_inertia_kn = (load_mass_kg * 9.81 * 0.05) / 1000.0
        total_structural_force_kn = aerodynamic_force_kn + hoist_inertia_kn
        
        # 3. Model multi-frequency gantry node micro-oscillations (Stochastic Wave Mesh)
        time_steps = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
        structural_modes_hz = np.array([2.4, 5.8, 12.1])
        
        print(f"📊 RUNNING CRANE STRUCTURAL JITTER MESH AT {wind_velocity_knots:.1f} KNOTS:")
        print("-" * 75)
        print(f" -> Calculated Wind Force     : {aerodynamic_force_kn:.2f} kN")
        print(f" -> Hoist Inertial Tension    : {hoist_inertia_kn:.2f} kN")
        print(f" -> Total Node Structural Load: {total_structural_force_kn:.2f} kN")
        print("-" * 75)
        
        max_displacement_mm = 0.0
        
        for step, t in enumerate(time_steps):
            # Resolve structural vibration node displacement metrics using np.sum
            oscillation_wave = np.sum(12.5 * np.sin(2 * np.pi * structural_modes_hz * t) + 
                                      6.2 * np.cos(2 * np.pi * structural_modes_hz * t))
            
            # Baseline static deflection: x = F/k (converted to mm)
            static_deflection_mm = (total_structural_force_kn / self.k_structure) * 1000.0
            instantaneous_deflection_mm = static_deflection_mm + (oscillation_wave * (wind_m_s / 15.0))
            
            if abs(instantaneous_deflection_mm) > max_displacement_mm:
                max_displacement_mm = abs(instantaneous_deflection_mm)
                
            print(f"    [Step {step+1} @ {t}s] Instantaneous Spreader Deviation: {instantaneous_deflection_mm:.2f} mm")
            
        print("-" * 75)
        print(f" -> Peak Spreader Visual Alignment Deviation: {max_displacement_mm:.2f} mm")
        
        # Automated alignment target boundary safety thresholds
        # Laser targeting sensors lose precision when tracking drift exceeds 35mm
        if max_displacement_mm > 35.0:
            print("⚠️  CRITICAL: Wind-shear induced jitter exceeds laser sensor alignment thresholds. Spreader lock delayed.")
        else:
            print("🟢 NORMAL: Gantry micro-oscillations remain inside automated positioning bounds.")
            
        return max_displacement_mm

if __name__ == "__main__":
    print("[★] INITIALISING TRITON STRUCTURAL WIND-SHEAR MODELER (v1.2.0)...")
    engine = CraneJitterEngine()
    
    # 1. Run local nominal port baseline operations (12 knot gentle sea breeze)
    engine.compute_structural_deflection(wind_velocity_knots=12.0)
    
    print("\n" + "="*75)
    print("[★] TRITON ENVIRONMENTAL INJECTION: HIGH-VELOCITY COASTAL GUST SURGE")
    print("="*75)
    
    # 2. Run severe storm profile (38 knot gale force tracking limits) to breach safety threshold
    engine.compute_structural_deflection(wind_velocity_knots=38.0)
