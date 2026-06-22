# ==========================================================================
# PROJECT:   PROJECT ECHO (SANDBOX TRACK)
# ENGINE:    AUTOMATED WORKSPACE LOG ROTATOR & ARTICFACT CLEANER
# FILE:      echo_cleaner.py
# SECURITY:  SANDBOX ISOLATED // LOCAL DESK USE ONLY
# ==========================================================================

import os
import glob

def clear_runtime_artifacts():
    print("==========================================================================")
    print("🧽 PROJECT ECHO: ARTIFACT CLEANUP & DIRECTORY OPTIMIZATION")
    print("==========================================================================")
    
    # Locate obsolete .rtf fragments or temporary session files
    target_pattern = os.path.join(os.getcwd(), "*.rtf")
    rtf_files = glob.glob(target_pattern)
    
    print(f"[*] Scanning workspace for unnecessary artifact signatures...")
    
    if not rtf_files:
        print("[i] Clean sweep complete. No redundant .rtf files detected.")
    else:
        for file_path in rtf_files:
            try:
                os.remove(file_path)
                print(f"[+] Successfully purged artifact file: {os.path.basename(file_path)}")
            except Exception as e:
                print(f"[!] Warning: Unable to remove {os.path.basename(file_path)}: {str(e)}")
                
    print("==========================================================================")
    print("[+] Workspace data structures optimized and pristine.")
    print("==========================================================================")

if __name__ == "__main__":
    clear_runtime_artifacts()
