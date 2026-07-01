#!/bin/bash
# ==============================================================================
# SLB RESONANT SYSTEMS - INTEGRATED COORDINATE RUNTIME
# Version: 1.1.0 (Production Lock) // Node: D6889ECD83EE
# ==============================================================================

# Force terminal context path directly to the folder containing this file
cd "$(dirname "$0")"

clear
echo "======================================================================"
echo "          SLB RESONANT SYSTEMS - INTEGRATED RUNTIME PLATFORM          "
echo "  NODE: THE NORTH WEST, UK // USER: STUART BREAKELL // VERSION: 1.1.0  "
echo "======================================================================"
echo "🟢 RUNWAY SECURE // THE SPOON IS LOCKED GREEN"
echo ""
echo "Select Target Coordinate Vector:"
echo "----------------------------------------------------------------------"
echo "1) Skunkworks Core Array     [echo_velocity_alerter.py]"
echo "2) Project Trisolaris Base   [trisolaris_reactance_calculator.py]"
echo "3) Project Trisolaris Weather[trisolaris_weather_mesh.py] 🔥 NEW"
echo "4) Project Vulcan Core       [vulcan_core_mesh.py / vulcan_intake_forecaster.py]"
echo "5) Project Neptune Storage   [neptune_surge_stabilizer.py / neptune_transient_solver.py]"
echo "6) Project Neptune Predict   [neptune_predictive_analyzer.py]"
echo "7) Dev Deployment Environment [Open GitHub Desktop]"
echo "8) Terminate Console Session [Exit]"
echo "----------------------------------------------------------------------"
echo "----------------------------------------------------------------------"
echo -n "Enter Target Coordinate Selection [1-8]: "
read coordinate

case $coordinate in
    1)
        python3 echo_velocity_alerter.py
        ;;
    2)
        python3 trisolaris_reactance_calculator.py
        ;;
    3)
        python3 trisolaris_weather_mesh.py
        ;;
    4)
        python3 vulcan_core_mesh.py
        python3 vulcan_intake_forecaster.py
        ;;
    5)
        python3 neptune_surge_stabilizer.py
        python3 neptune_transient_solver.py
        ;;
    6)
        python3 neptune_predictive_analyzer.py
        ;;
    7)
        open -a "GitHub Desktop"
        ;;
    8)
        exit 0
        ;;
    *)
        echo "⚠️ Invalid coordinate selection."
        ;;
esac

echo ""
echo "======================================================================"
echo "Process execution complete."
echo "======================================================================"
