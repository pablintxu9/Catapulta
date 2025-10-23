class Enemigo:
    def __init__(self, vida):
        self.vida = vida

    def recibir_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def esta_eliminado(self):
        return self.vida == 0

    def __str__(self):
        return f"Enemigo con {self.vida} de vida."