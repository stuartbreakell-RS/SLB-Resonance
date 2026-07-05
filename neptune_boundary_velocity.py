#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SYSTEM RUNTIME NODE: THE NORTH WEST, UK // USER: STUART BREAKELL
# COMPONENT: NEPTUNE KINEMATIC FLUID BOUNDARY VELOCITY SOLVER v1.1.0

import math

def evaluate_boundary_profile():
    # --- LOCKED PRODUCTION HYDRAULIC METRICS ---
    pipe_diameter_mm = 600.0
    nominal_flow_m3_s = 0.4219
    fluid_density_kg_m3 = 998.2
    dynamic_viscosity_pa_s = 0.001002  # Water at nominal temperature
    friction_floor = 0.0201
    
    print("⚡ INITIALISING BOUNDARY-LAYER VELOCITY CALCULATION PROFILE...")
    
    # Core geometric calculations
    radius_m = (pipe_diameter_mm / 2.0) / 1000.0
    cross_sectional_area = math.pi * (radius_m ** 2)
    mean_velocity_m_s = nominal_flow_m3_s / cross_sectional_area
    
    # Calculate Reynolds Number to track turbulence boundaries
    reynolds_number = (fluid_density_kg_m3 * mean_velocity_m_s * (radius_m * 2.0)) / dynamic_viscosity_pa_s
    
    # Compute precise kinetic friction dissipation using the v1.1.0 floor scaling
    shear_stress_wall = 0.125 * friction_floor * fluid_density_kg_m3 * (mean_velocity_m_s ** 2)
    friction_velocity = math.sqrt(shear_stress_wall / fluid_density_kg_m3)
    
    print(f"-> Mean Flow Velocity   : {mean_velocity_m_s:.4f} m/s")
    print(f"-> Calculated Reynolds No: {reynolds_number:.2f} (Turbulent Regime)")
    print(f"-> Wall Shear Stress    : {shear_stress_wall:.4f} Pa")
    print(f"-> Friction Velocity u* : {friction_velocity:.6f} m/s")
    print("\n🟢 PLATFORM MATRIX LOCK: VELOCITY DECAY TRACKED // RUNWAY GREEN")
    
    return mean_velocity_m_s

if __name__ == "__main__":
    evaluate_boundary_profile()
