import matplotlib.pyplot as plt
import numpy as np

# Data - Nejvyšší budovy světa (výška v metrech)
buildings = [
    'Burj Khalifa\n(Dubaj)',
    'Merdeka 118\n(Kuala Lumpur)',
    'Shanghai Tower\n(Šanghaj)',
    'Abraj Al-Bait\n(Mekka)',
    'Ping An Finance\n(Šen-čen)',
    'Lotte World Tower\n(Soul)',
    'One World Trade\n(New York)',
    'Guangzhou CTF\n(Kanton)',
    'Tianjin CTF\n(Ťien-ťin)',
    'China Zun\n(Peking)'
]

heights = [828, 679, 632, 601, 599, 555, 541, 530, 530, 528]

# Vytvoření grafu
plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(buildings)), heights, color='skyblue', edgecolor='navy', linewidth=1.5)

# Přidání hodnot nad sloupcemi
for i, (bar, height) in enumerate(zip(bars, heights)):
    plt.text(bar.get_x() + bar.get_width()/2, height + 10, 
             f'{height}m', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Nastavení grafu
plt.xlabel('Budovy', fontsize=12, fontweight='bold')
plt.ylabel('Výška (metry)', fontsize=12, fontweight='bold')
plt.title('TOP 10 Nejvyšších budov světa', fontsize=16, fontweight='bold', pad=20)
plt.xticks(range(len(buildings)), buildings, rotation=45, ha='right', fontsize=9)
plt.ylim(0, max(heights) + 50)
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()

# Uložení a zobrazení grafu
plt.savefig('nejvyssi_budovy.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Graf byl vytvořen a uložen jako 'nejvyssi_budovy.png'")
