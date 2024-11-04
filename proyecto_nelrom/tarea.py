from datetime import datetime
class Tarea:
    def __init__(self, titulo, content):
        self.ttl = titulo
        self.msg = content
        self.time = datetime.now().time().strftime("%H:%M:%S")

    def get_tarea(self):
        tarea = {
            "titulo": self.ttl,
            "contenido": self.msg,
            "f_creacion" : self.time
        }
        return tarea
