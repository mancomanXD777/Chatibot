class Chati:

    def __init__(self, configuracion):
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

        elif mensaje == "como estas":
            return "Funcionando correctamente"

        else:
            return "No entendí lo que dijiste"