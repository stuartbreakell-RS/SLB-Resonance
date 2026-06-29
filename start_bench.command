#!/bin/bash

# Force terminal context path directly to the folder containing this file
cd "$(dirname "$0")"

clear
echo "=========================================================================="
echo "🚀 SLB RESONANT SYSTEMS // DEV SYSTEM LAUNCH BENCH PLATFORM v1.1.0"
echo "=========================================================================="
echo "Choose operational coordinate target node:"
echo "  * 1) PROJECT ECHO        - Run 9-Stage Diagnostics & DeepTech Sweep"
echo "  * 2) PROJECT TRISOLARIS  - Run ACSR Transmission Line Reactance Calculator"
echo "  * 3) PROJECT VULCAN      - Run Frontline Clinical Staffing Shortage Matrix"
echo "  * 4) PROJECT NEPTUNE     - Run Hydraulic Surge Overflow Ledger"
echo "  * 5) NEPTUNE FORECAST    - Run 6-Hour Time-Series Surge Predictive Engine"
echo "  * 6) GLOBAL STOREFRONT   - Launch GitHub Desktop Synchronised Panel"
echo "  * 7) EXIT BENCH          - Safe Terminal Room Shutdown"
echo "=========================================================================="

read -p "Enter operational coordinate [1-7]: " coordinate

case $coordinate in
    1)
        python3 echo_velocity_alerter.py
        ;;
    2)
        python3 trisolaris_reactance_calculator.py
        ;;
    3)
        python3 vulcan_core_mesh.py
        python3 vulcan_intake_forecaster.py
        ;;
    4)
        python3 neptune_surge_stabilizer.py
        python3 neptune_transient_solver.py
        ;;
    5)
        python3 neptune_predictive_analyzer.py
        ;;
    6)
        open -a "GitHub Desktop"
        ;;
    7)
        exit 0
        ;;
    *)
        echo "Invalid coordinate selection."
        ;;
esac

echo "=========================================================================="
echo "Process execution complete."
echo "=========================================================================="
