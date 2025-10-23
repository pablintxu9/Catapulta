class Gomas:
    def __init__(self, elasticidad):
        self.elasticidad = elasticidad

    def calcular_fuerza(self, distancia):
        return self.elasticidad * distancia

    def __str__(self):
        return f"Gomas con elasticidad: {self.elasticidad}"