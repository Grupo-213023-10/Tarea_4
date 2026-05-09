from abc import ABC, abstractmethod  # Librería para crear clases abstractas
import logging  # Librería para manejar logs
from datetime import datetime  # Librería para fechas

logging.basicConfig(

    # Nombre del archivo
    filename="logs.txt",

    # Nivel de registro
    level=logging.INFO,

    # Formato del mensaje
    format="%(asctime)s - %(levelname)s - %(message)s"
)
