class Catapulta:
    def __init__(self, palos, gomas, tapones, corchos, pegamento):
        self.palos = palos
        self.gomas = gomas
        self.tapones = tapones
        self.corchos = corchos
        self.pegamento = pegamento
        self.construida = False

    def construir(self):
        if self.palos and self.gomas and self.tapones and self.corchos and self.pegamento:
            self.construida = True
            return "Catapulta construida con éxito."
        else:
            return "Faltan componentes para construir la catapulta."

    def lanzar(self, enemigo):
        if not self.construida:
            return "La catapulta no está construida."
        
        fuerza_lanzamiento = self.gomas.elasticidad * len(self.palos)
        enemigo.recibir_dano(fuerza_lanzamiento)
        return f"Se lanzó un proyectil con fuerza {fuerza_lanzamiento}."

    def estado(self):
        return "Construida" if self.construida else "No construida"