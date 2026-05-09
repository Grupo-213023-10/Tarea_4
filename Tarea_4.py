from abc import ABC, abstractmethod  # Librería para crear clases abstractas
import logging  # Librería para manejar logs
from datetime import datetime  # Librería para fechas

logging.basicConfig( # Configura el sistema de logs

    # Nombre del archivo
    filename="logs.txt",
    level=logging.INFO, # Define que se guardarán mensajes desde el nivel INFO en adelante
    format="%(asctime)s - %(levelname)s - %(message)s" # Define el formato de cada mensaje del log: fecha, nivel y mensaje.
)
# Excepción para clientes
class ClienteError(Exception): # Crea una excepción personalizada 
    pass # Indica que la clase estará vacía

class Entidad(ABC):  # Se crea la clase abstracta entidad

    @abstractmethod  # Indica que el método siguiente debe implementarse obligatoriamente en las clases hijas.
    
    def mostrar_info(self):
        pass

# Clase Cliente
class Cliente(Entidad):

    # Constructor
    def __init__(self, nombre, correo, telefono):

        try:

            # Validación del nombre
            if not nombre.strip():
                raise ValueError("El nombre está vacío")

            # Validación del correo
            if "@" not in correo:
                raise ValueError("Correo inválido")

            # Validación del teléfono
            if not telefono.isdigit():
                raise ValueError("El teléfono debe tener solo números")

            # Encapsulación de atributos
            self.__nombre = nombre
            self.__correo = correo
            self.__telefono = telefono

            # Registro en logs
            logging.info(f"Cliente creado: {nombre}")

        except ValueError as error:

            # Guardamos error
            logging.error(error)

            # Encadenamiento de excepción
            raise ClienteError("No se pudo crear el cliente") from error

    # Getter nombre
    def get_nombre(self):
        return self.__nombre

    # Getter correo
    def get_correo(self):
        return self.__correo

    # Getter teléfono
    def get_telefono(self):
        return self.__telefono

    # Setter nombre
    def set_nombre(self, nuevo_nombre):

        try:

            # Validación
            if not nuevo_nombre.strip():
                raise ClienteError("Nombre inválido")

            # Actualización
            self.__nombre = nuevo_nombre

            # Log
            logging.info("Nombre actualizado")

        except ClienteError as error:

            logging.error(error)

            print(error)

    # Setter correo
    def set_correo(self, nuevo_correo):

        try:

            # Validación
            if "@" not in nuevo_correo:
                raise ClienteError("Correo inválido")

            # Actualización
            self.__correo = nuevo_correo

            # Log
            logging.info("Correo actualizado")

        except ClienteError as error:

            logging.error(error)

            print(error)

    # Método obligatorio heredado
    def mostrar_info(self):

        print("\n===== CLIENTE =====")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")