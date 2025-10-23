class Palos:
    def __init__(self, longitud):
        self.longitud = longitud

    def obtener_longitud(self):
        return self.longitud

    def __str__(self):
        return f"Palos de longitud: {self.longitud} cm"