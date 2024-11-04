import json

class Lista:
    def __init__(self, ruta):
        self.ruta = f"proyecto_nelrom/{ruta}"

    def add_tarea(self, tarea):
        try:
            with open(self.ruta , "r") as file:
                datos_e = json.load(file)
        except FileNotFoundError:
            datos_e = []

        datos_e.append(tarea.get_tarea())

        with open(self.ruta , "w") as file:
            json.dump(datos_e, file, indent=4)