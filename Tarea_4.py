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
    
    def mostrar_info(self):  # Se realiza la función de mostrar información
        pass  # Esta función estará vacía momentaneamente

# Clase Cliente
class Cliente(Entidad): # Se crea la clase cliente

    # Constructor
    def __init__(self, nombre, correo, telefono):  # Se inicia el constructor de la clase Cliente

        try:  # Con try empezaremos a manejar los errores

            # Validación del nombre
            if not nombre.strip():  # Se verifica que el nombre no esté vacío
                raise ValueError("El nombre está vacío")  # Genera un error si el nombre está vacío

            # Validación del correo
            if "@" not in correo:  # Se verifica que el correo se válido usando al usar @
                raise ValueError("Correo inválido")  # Genera error si no es un correo válido

            # Validación del teléfono
            if not telefono.isdigit():  # Se verifica que el número de teléfno tenga solo números
                raise ValueError("El teléfono debe tener solo números")  # Genera error si el teléfono contiene letras u otros caracteres

            # Encapsulación de atributos
            self.__nombre = nombre  # Guarda el nombre como atributo privado
            self.__correo = correo  # Guarda el correo como atributo privado
            self.__telefono = telefono  # Guarda el teléfono como atributo privado

            # Registro en logs
            logging.info(f"Cliente creado: {nombre}")  # Registra en el log que el cliente fue creado

        except ValueError as error:  # Captura errores de validación.

            # Se Guarda el error en el log
            logging.error(error)

            # Muestra una excepción personalizada encadenando el error original
            raise ClienteError("No se pudo crear el cliente") from error

    
    def get_nombre(self):  # Obtiene el nombre del cliente
        return self.__nombre  # Retorna el nombre

    
    def get_correo(self):  # Obtiene el correo 
        return self.__correo  # Retorna el correo

    
    def get_telefono(self):  # Obtiene el teléfono
        return self.__telefono  # Retorna el teléfono

    
    def set_nombre(self, nuevo_nombre): # Función para modificar el nombre

        try:  # Lo usamos para manejar los errores

            # Validación
            if not nuevo_nombre.strip(): # Verifica que el nuevo nombre no esté vacío
                raise ClienteError("Nombre inválido")  # Muestra error si está vacío

            self.__nombre = nuevo_nombre  # Actualiza el nombre

            logging.info("Nombre actualizado")  # Guarda la actualización en el log

        except ClienteError as error:  # Captura el error

            logging.error(error)  # Guarda el error en el log

            print(error)  # Muestra en pantalla el error

    
    def set_correo(self, nuevo_correo):  # Función para modificar el correo

        try: # Lo usamos para manejar los errores

            if "@" not in nuevo_correo:  # Verifica que sea un correo válido
                raise ClienteError("Correo inválido")  # Muestra error si no es un correo válido

            
            self.__correo = nuevo_correo  # Actualiza el nuevo correo

            
            logging.info("Correo actualizado")  # Guarda la actualización en el log

        except ClienteError as error:  # Captura el error

            logging.error(error)  # Guarda el error en el log

            print(error)  # Muestra en pantalla el error

    def set_telefono(self, nuevo_telefono):  # Función para modificar el teléfono

        try:  # Lo usamos para manejar los errores

            
            if not nuevo_telefono.isdigit():  # Verifica que sean números los ingresados
                raise ClienteError( "El teléfono debe tener solo números")  # # Muestra error si no es un número

           
            self.__telefono = nuevo_telefono  # Guarda el nuevo número

            logging.info("Teléfono actualizado")  # Guarda la actualización en el log

        except ClienteError as error:  # Captura el error en el log

            logging.error(error)  # Guarda el error en el log

            print(error) # Muestra en pantalla el error   
    
    def mostrar_info(self): # Se usa la función de mostrar información
        # Se muestra en pantalla los datos del cliente registrado
        print("\n===== CLIENTE =====")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")










if __name__ == "__main__":  # Verifica que el archivo se esté ejecutando directamente

    print("\n========= SOFTWARE FJ =========") # Nombre de la empresa

    reservas = []  # Se crea la lista vacía en donde se guardarán las reservas

    # Contador de operaciones
    operaciones = 0  # Se hace un conteo del número de operaciones, esto porque la actividad solicita
                        # que el sistema permita realizar al menos 10 operaciones
   
    # CREACIÓN DEL CLIENTE
    while True:  # Crea un cliclo infinito hasta que se usa break, esto con el fin de que si hay errores
                    # vuelva a preguntar por los datos
        try:

            print("\n===== REGISTRO DE CLIENTE =====")  # Área del programa en la que se encuentra

            nombre = input("Ingrese el nombre: ")  # Solicita nombre del usuario

            correo = input("Ingrese el correo: ")  # Solicita el correo

            telefono = input("Ingrese el teléfono: ")  # Solicita teléfono

            # Crear cliente
            cliente1 = Cliente(  # Se crea un objeto cliente
                nombre,
                correo,
                telefono
            )

            # Operación exitosa
            operaciones += 1  # Incrementa el contador de operaciones

            print("\nCliente creado correctamente")  # Si todo sale bien, lo mostrará en pantalla

            cliente1.mostrar_info()  # Se muestra la información del cliente
            
            while True:  # Se crea un ciclo infinito, para hacer correciones del dato del cliente
                    # Se muestra en pantalla un menú en caso requerir modificación de los datos
                print("\n===== MODIFICAR CLIENTE =====")
                print("1. Modificar nombre")
                print("2. Modificar correo")
                print("3. Modificar teléfono")
                print("4. Continuar")  # Se hará brear para continuar con el programa

                opcion_modificar = input("Seleccione una opción: ")  # Se solicita la opción para continuar

                if opcion_modificar == "1":  # si presiona 1

                    nuevo_nombre = input(  # Se solicita ingresar el nuevo nombre
                        "Ingrese el nuevo nombre: "
                    )

                    cliente1.set_nombre(nuevo_nombre)  # Se hace el reemplazo

                elif opcion_modificar == "2":  # Si presiona 2

                    nuevo_correo = input(  # Se solicita ingresar el nuevo correo
                        "Ingrese el nuevo correo: "
                    )

                    cliente1.set_correo(nuevo_correo)  # Se hace el reemplazo

                elif opcion_modificar == "3":  # Si presiona 3

                    nuevo_telefono = input(  # Se solicita ingresar el nuevo teléfono
                        "Ingrese el nuevo teléfono: "
                    )

                    cliente1.set_telefono(nuevo_telefono)  # Se hace el reemplazo

                elif opcion_modificar == "4":  # Si presiona 4

                    break  # Se activa el break y sale de este while

                else:

                    print("Opción inválida")  # Si no presiona una de las opciones anteriores, mostrará que no fue una opción válida

                cliente1.mostrar_info()  # Muestra la información del cliente
            break  # Sale del while
        except Exception as error:  # Captura el error

            operaciones += 1  # Realiza el conteo de la operación

            print(f"\n{error}")  # Muestra en pantalla el error

            print("Por favor intente nuevamente...\n")  # Muestra en pantalla que intente        
            
            # CREACIÓN DEL SERVICIO
    
    while True:  # Se crea ciclo infinito, en donde se escogerá el servicio deseado por el cliente

        try:  # Se usa try para manejar los errores

            # Se muestra menú para escoger el servicio
            print("\n===== SERVICIOS DISPONIBLES =====")
            print("1. Reserva de Sala")
            print("2. Alquiler de Equipo")
            print("3. Asesoría Especializada")

            opcion = int( # Opción para ingresar el servicio
                input("\nSeleccione un servicio: ")
            )
                # RESERVA DE SALA
            
            if opcion == 1: # Si presiona tecla 1, escogerá la reserva de sala

                nombre_servicio = input(  # Se solicita ingresar cuál sala escogerá el usuario
                    "Ingrese nombre de la sala: "
                )

                precio = float(  # Se ingresa el costo de la sala
                    input("Ingrese precio base: ")
                )

                horas = int(  # Cantidad de horas que solicita el usuario
                    input("Ingrese cantidad de horas: ")
                )

                servicio = ReservaSala( # Guarda la información de la reserva
                    nombre_servicio,
                    precio,
                    horas
                )
                # ALQUILER DE EQUIPOS
            
            elif opcion == 2:  # Si presiona tecla 2, escogerá alquiler de equipos

                nombre_servicio = input(  # Se solicita ingresar el nombre del equipo a alquilar
                    "Ingrese nombre del equipo: "
                )

                precio = float(  # Se ingresa el costo del equipo
                    input("Ingrese precio base: ")
                )

                dias = int(  # Cantidad de dias que solicita el usuario
                    input("Ingrese cantidad de días: ")
                )

                servicio = AlquilerEquipo(  # Guarda la información de la reserva
                    nombre_servicio,
                    precio,
                    dias
                )
                 # ASESORÍA ESPECIALIZADA
            

            elif opcion == 3:  # Si presiona tecla 3, escogerá alquiler de equipos

                nombre_servicio = input(  # Se solicita ingresar el nombre o tipo de asesoría
                    "Ingrese nombre de la asesoría: "
                )

                precio = float(  # Precio de la asesoría
                    input("Ingrese precio base: ")
                )

                horas = int(  # Horas en la asesoría
                    input("Ingrese cantidad de horas: ")
                )

                servicio = AsesoriaEspecializada(  # Guarda la información
                    nombre_servicio,
                    precio,
                    horas
                )
            else:

                raise ValueError("Opción inválida")  # Saldrá error si no se escoge una de las opciones anteriores

            # Operación exitosa
            operaciones += 1  # Se suma el conteo de operaciónes

            print("\nServicio creado correctamente")  # Confirmación del servicio

            servicio.mostrar_info()  # Se muestra la información del servicio solicitado

            break  # Se sale del while de servicios

        except Exception as error: # Captura el error

            # Operación fallida
            operaciones += 1  # Suma a la operación

            print(f"\n{error}")  # Muestra en pantalla el error

            print("Por favor intente nuevamente...\n")  # Solicita ingresar nuevamente el servicio

            # CREACIÓN DE RESERVA
 
    while True:  # Se crea ciclo infinito, en donde se creará la reserva

        try:  # Se manejarán los errores

            print("\n===== CREAR RESERVA =====")  # Menú de crear reserva

            duracion = int(  # Lo que duró la reserva
                input("Ingrese duración de la reserva: ")
            )

            # Crear reserva
            reserva1 = Reserva(  # Se guarda los datos de la reserva
                cliente1,
                servicio,
                duracion
            )
            reservas.append(reserva1)  # Crea la reserva
            
            operaciones += 1  # Realiza el conteo de esta operación

            print("\nReserva creada correctamente")  # Confirmación de la reserva

            reserva1.mostrar_reserva()  # Muestra la información de la reserva

            break  # Sale del while
        except Exception as error:  # Se captura el error

            operaciones += 1  # Se realiza el conteo de la operación

            print(f"\n{error}")  # Muestra en pantalla el error

            print("Por favor intente nuevamente...\n")  # Solicita intentar nuevamente el ingreso del servicio
