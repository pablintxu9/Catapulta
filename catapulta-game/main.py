from catapulta.catapulta import Catapulta
from catapulta.enemigo import Enemigo

def main():
    print("Bienvenido al juego de la Catapulta!")
    
    # Crear enemigos
    enemigos = [Enemigo(vida=100) for _ in range(3)]
    
    # Selección de componentes para la catapulta
    longitud = float(input("Ingrese la longitud de los palos: "))
    elasticidad = float(input("Ingrese la elasticidad de las gomas: "))
    tamaño = float(input("Ingrese el tamaño de los tapones: "))
    flotabilidad = float(input("Ingrese la flotabilidad de los corchos: "))
    resistencia = float(input("Ingrese la resistencia del pegamento: "))
    
    # Construir la catapulta
    catapulta = Catapulta(longitud, elasticidad, tamaño, flotabilidad, resistencia)
    catapulta.construir()
    
    # Lanzar proyectiles contra los enemigos
    for enemigo in enemigos:
        catapulta.lanzar(enemigo)
        print(f"Enemigo con vida: {enemigo.vida}")
        if enemigo.vida <= 0:
            print("¡Enemigo eliminado!")
        else:
            print("El enemigo sigue en pie.")

if __name__ == "__main__":
    main()