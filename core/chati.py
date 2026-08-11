import json
class Chati:

    def __init__(self, configuracion):
        self.idioma = configuracion.get("idioma", "es")
        self.nombre = configuracion.get("nombre", "Sin nombre")
        self.jugador_actual = None
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
        respuesta = ""

        if "hola" in mensaje:
            respuesta = "Hola, un gusto conocerte"

        elif "como me llamo" in mensaje:
            if self.jugador_actual:
                jugador = self.memoria.get("jugadores", {}).get(self.jugador_actual)

                if jugador:
                    respuesta = f"Tu nombre es {jugador['nombre']}"
                else:
                    respuesta = "Todavía no sé tu nombre"
            else:
                respuesta = "Todavía no sé tu nombre"

        elif "me llamo" in mensaje:
            nombre = mensaje.replace("me llamo ", "")
            self.crear_jugador(nombre)
            respuesta = self.establecer_jugador_actual(nombre)

        elif "como estas" in mensaje:
            respuesta = "Funcionando correctamente"
        else:
            respuesta = "No entendí lo que dijiste"
        self.guardar_historial(mensaje, respuesta)
        return respuesta
    
    def guardar_memoria(self):
        with open("data/memoria.json", "w", encoding="utf-8") as archivo:
            json.dump(self.memoria, archivo, ensure_ascii=False, indent=4)

    def establecer_jugador_actual(self, nombre):
        if nombre in self.memoria.get("jugadores", {}):
            self.jugador_actual = nombre
            return f"Jugador actual establecido a {nombre}"
        else:
            return f"No se encontró el jugador {nombre} en la memoria."

    def guardar_historial(self, mensaje, respuesta):
        if self.jugador_actual:
            jugador = self.memoria.get("jugadores", {}).get(self.jugador_actual)

            if jugador:
                jugador["historial"].append({
                    "mensaje": mensaje,
                    "respuesta": respuesta
                })
                self.guardar_memoria()