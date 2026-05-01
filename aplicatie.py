import json
import os
from datetime import datetime

def afiseaza_meniu():
    print("\n" + "="*35)
    print("🚀 MANAGER DE PROIECT PRO")
    print("="*35)
    print("1. Adaugă sarcină + Deadline")
    print("2. Vezi lista de activități")
    print("3. Șterge o sarcină")
    print("4. Salvare și Ieșire")
    print("="*35)

def aplicatie_concurs():
    sarcini = []
    if os.path.exists("concurs_data.json"):
        with open("concurs_data.json", "r") as f:
            sarcini = json.load(f)

    while True:
        afiseaza_meniu()
        optiune = input("Alege (1-4): ")

        if optiune == "1":
            text = input("Ce ai de făcut?: ")
            data_str = input("Introdu termenul (Format: ZI-LUNA-AN, ex: 25-12-2024): ")
            sarcini.append({"task": text, "deadline": data_str})
            print("✅ Salvat cu succes!")

        elif optiune == "2":
            print("\n📋 LISTA TA DE ACTIVITĂȚI:")
            azi = datetime.now()
            
            for i, s in enumerate(sarcini):
                try:
                    data_limit = datetime.strptime(s['deadline'], "%d-%m-%Y")
                    diferenta = data_limit - azi
                    
                    if diferenta.days < 0:
                        status = "⚠️ TERMEN DEPĂȘIT!"
                    else:
                        status = f"⏳ Mai ai {diferenta.days} zile"
                    
                    print(f"{i+1}. {s['task']} | Termen: {s['deadline']} -> {status}")
                except ValueError:
                    print(f"{i+1}. {s['task']} | Data formatată greșit!")
            
            if not sarcini: print("Nimic de făcut momentan.")

        elif optiune == "3":
            index = int(input("Nr. sarcinii de șters: ")) - 1
            if 0 <= index < len(sarcini):
                sarcini.pop(index)
                print("🗑️ Șters!")

        elif optiune == "4":
            with open("concurs_data.json", "w") as f:
                json.dump(sarcini, f)
            print("Toate datele au fost securizate. Baftă!")
            break

if _name_ == "_main_":
    aplicatie_concurs()