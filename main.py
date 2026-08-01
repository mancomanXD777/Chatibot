"""
===========================================
Proyecto : ChatiBot
Version  : 0.0.1 Alpha
Archivo  : main.py
===========================================
"""

import json

from core.chati import Chati


def cargar_configuracion():
    with open("config/config.json", "r", encoding="utf-8") as archivo:
        configuracion = json.load(archivo)

    return configuracion


configuracion = cargar_configuracion()


print("================================")
print("Iniciando ChatiBot...")
print("================================")

print(f"Nombre: {configuracion.get('nombre', 'Sin nombre')}")
print(f"Version: {configuracion.get('version', 'Desconocida')}")
print(f"Idioma: {configuracion.get('idioma', 'Sin idioma')}")
print(f"Personalidad: {configuracion.get('personalidad', 'Normal')}")

bot = Chati(configuracion)

bot.presentarse()