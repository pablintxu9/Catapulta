class Pegamento:
    def __init__(self, resistencia):
        self.resistencia = resistencia

    def verificar_union(self):
        if self.resistencia > 5:
            return True
        return False

    def __str__(self):
        return f"Pegamento con resistencia: {self.resistencia}"