class Chati:

    def __init__(self, configuracion):
        self.memoria = configuracion.get("memoria", {})
        self.nombre = configuracion.get("nombre", "Sin nombre")
        self.personalidad = configuracion.get("personalidad", "Normal")
        self.version = configuracion.get("version", "0.0.0")

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")
        print(f"Mi personalidad es {self.personalidad}")
        print(f"Estoy usando la versión {self.version}")

    def responder(self, mensaje):
        mensaje = mensaje.lower()

        if mensaje == "hola":
            return "Hola, un gusto conocerte"

        elif "me llamo" in mensaje:
            nombre = mensaje.replace("me llamo ", "")
            self.memoria["jugador"] = nombre

            return f"Un gusto conocerte {nombre}"

        elif "como estas" in mensaje:
            return "Funcionando correctamente"

        elif "como me llamo" in mensaje:
            nombre = self.memoria.get("jugador", "todavía no lo sé")

            return f"Te llamas {nombre}"

        else:
            return "No entendí lo que dijiste"