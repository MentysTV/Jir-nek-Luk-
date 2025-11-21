# ⚔️ Práce se seznamem zbraní v Rustu
# Autor: [Vaše jméno]
# Datum: 21.11.2025

# 1. Vytvoření listu ze zkopírovaného seznamu
weapons = [
    "Revolver",
    "Python Revolver",
    "Semi-Automatic Pistol (SAP)",
    "M92 Pistol",
    "Nailgun",
    "Waterpipe Shotgun",
    "Pump Shotgun",
    "Double Barrel Shotgun",
    "Spas-12",
    "Custom SMG",
    "Thompson",
    "MP5A4",
    "Semi-Automatic Rifle",
    "Assault Rifle (AK)",
    "LR-300 Assault Rifle",
    "Bolt Action Rifle",
    "M39 Rifle",
    "M249",
    "L96 Sniper Rifle",
    "Grenade Launcher",
    "Rocket Launcher",
    "F1 Grenade",
    "Beancan Grenade",
    "Satchel Charge",
    "Timed Explosive Charge (C4)",
    "Rocket (HV / Regular / Incendiary)",
    "Incendiary Grenade",
    "Molotov Cocktail",
    "Stone Spear",
    "Wooden Spear",
    "Machete",
    "Sword",
    "Bone Knife",
    "Combat Knife",
    "Salvaged Sword",
    "Paddle",
    "Stone Hatchet / Stone Pickaxe",
    "Metal Hatchet / Metal Pickaxe",
    "Hunting Bow",
    "Compound Bow",
    "Crossbow",
    "Eoka Pistol",
    "Flamethrower",
    "Chainsaw"
]

print("=== PŮVODNÍ SEZNAM ===")
print(f"Délka seznamu: {len(weapons)}")
print(f"První zbraň: {weapons[0]}")
print(f"Poslední zbraň: {weapons[-1]}")
print()

# 2. Přidání další položky do listu
weapons.append("Snowball Gun")
print("=== PO PŘIDÁNÍ POLOŽKY ===")
print(f"Přidána položka: Snowball Gun")
print(f"Nová délka seznamu: {len(weapons)}")
print()

# 3. Odstranění první položky z listu
removed_item = weapons.pop(0)
print("=== PO ODSTRANĚNÍ PRVNÍ POLOŽKY ===")
print(f"Odstraněna položka: {removed_item}")
print()

# 4. Vypsání délky listu
print("=== AKTUÁLNÍ STAV ===")
print(f"Aktuální délka seznamu: {len(weapons)}")
print()

# 5. Vypsání celého listu
print("=== FINÁLNÍ SEZNAM VŠECH ZBRANÍ ===")
for i, weapon in enumerate(weapons, 1):
    print(f"{i}. {weapon}")
