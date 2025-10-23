# Catapulta Game

## Descripción
Catapulta Game es un juego interactivo donde los usuarios pueden construir su propia catapulta utilizando diferentes componentes como palos, gomas, tapones, corchos y pegamento. El objetivo del juego es lanzar proyectiles contra enemigos y eliminarlos.

## Estructura del Proyecto
El proyecto está organizado en varios archivos y carpetas:

- **catapulta/**: Contiene la lógica del juego y las clases que representan los componentes de la catapulta y los enemigos.
  - `__init__.py`: Inicializa el paquete `catapulta`.
  - `palos.py`: Define la clase `Palos`.
  - `gomas.py`: Define la clase `Gomas`.
  - `tapones.py`: Define la clase `Tapones`.
  - `corchos.py`: Define la clase `Corchos`.
  - `pegamento.py`: Define la clase `Pegamento`.
  - `catapulta.py`: Define la clase `Catapulta`.
  - `enemigo.py`: Define la clase `Enemigo`.

- **tests/**: Contiene pruebas unitarias para asegurar que la lógica del juego funcione correctamente.
  - `test_catapulta.py`: Pruebas para las clases y métodos del módulo `catapulta`.

- **main.py**: Punto de entrada del juego. Permite al usuario seleccionar los componentes para construir la catapulta y simula el lanzamiento contra los enemigos.

- **requirements.txt**: Lista las dependencias necesarias para el proyecto.

- **pyproject.toml**: Contiene la configuración del proyecto.

## Instrucciones para Ejecutar el Juego
1. Clona el repositorio o descarga los archivos del proyecto.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala las dependencias necesarias ejecutando:
   ```
   pip install -r requirements.txt
   ```
4. Ejecuta el juego con el siguiente comando:
   ```
   python main.py
   ```
5. Sigue las instrucciones en pantalla para construir tu catapulta y lanzar proyectiles contra los enemigos.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el juego, por favor abre un issue o un pull request en el repositorio.

## Licencia
Este proyecto está bajo la Licencia MIT.