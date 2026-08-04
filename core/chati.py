import json
class Chati:

    def __init__(self, configuracion):
        self.idioma = configuracion.get("idioma", "es")
        self.nombre = configuracion.get("nombre", "Sin nombre")
        self.personalidad = configuracion.get("personalidad", "Normal")
        self.version = configuracion.get("version", "0.0.0")

       #Memoria de chati
        self.memoria = {}
        self.cargar_memoria()


    def presentarse(self):
        print(f"Hola, soy {self.nombre}")
        print(f"Mi personalidad es {self.personalidad}")
        print(f"Estoy usando la versión {self.version}")

    def cargar_memoria(self):
        try:
            with open("data/memoria.json", "r", encoding="utf-8") as archivo:
                self.memoria = json.load(archivo)
        except FileNotFoundError:
            self.memoria = {}

    def crear_jugador(self, nombre):

        # Si no existe la lista de jugadores, la creamos
        if "jugadores" not in self.memoria:
            self.memoria["jugadores"] = {}

        # Si el jugador ya existe, terminamos la función
        if nombre in self.memoria["jugadores"]:
            return f"El jugador {nombre} ya existe en la memoria."

        # Si llegamos hasta aquí, significa que es un jugador nuevo
        self.memoria["jugadores"][nombre] = {
            "nombre": nombre,
            "ultima_conexion": "",
            "historial": []
        }

        self.guardar_memoria()

        return f"Jugador {nombre} creado correctamente."


    def responder(self, mensaje):
        mensaje = mensaje.lower()

        if mensaje == "hola":
            return "Hola, un gusto conocerte"

        elif "como me llamo" in mensaje:
            nombre = self.memoria.get("jugador", "todavía no lo sé")
            return f"Te llamas {nombre}"

        elif "me llamo" in mensaje:
            nombre = mensaje.replace("me llamo ", "")
            self.memoria["jugador"] = nombre
            self.guardar_memoria()

            return f"Un gusto conocerte {nombre}"

        elif "como estas" in mensaje:
            return "Funcionando correctamente"
        else:
            return "No entendí lo que dijiste"

    def guardar_memoria(self):
        with open("data/memoria.json", "w", encoding="utf-8") as archivo:
            json.dump(self.memoria, archivo, ensure_ascii=False, indent=4)