from abc import ABC, abstractmethod  # Librería para crear clases abstractas
import logging  # Librería para manejar logs
from datetime import datetime  # Librería para fechas

# Configuración del archivo logs.txt
logging.basicConfig(

    # Nombre del archivo
    filename="logs.txt",

    # Nivel de registro
    level=logging.INFO,

    # Formato del mensaje
    format="%(asctime)s - %(levelname)s - %(message)s"
<<<<<<< HEAD
)
=======
)
>>>>>>> 7d5da7e26bac278cba758e956c8a8a1eea15c6bd
