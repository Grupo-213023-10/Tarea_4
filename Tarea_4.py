# Nombre del estudiante: Emilson David Aguilar Feria
# Grupo: 213023_10
# Programa: Ingeniería electrónica
# Código Fuente: autoría propia

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

# Excepción para servicios
class ServicioError(Exception):
    pass

# Excepción para reservas
class ReservaError(Exception):
    pass
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

# Clase abstracta Servicio
class Servicio(Entidad):  # Clase padre, Para seleccionar el servicio

    # Constructor
    def __init__(self, nombre, precio_base):  # Constructor de la clase

        try:  # Maneja los errores

            
            if not nombre.strip():  # Validación si el nombre del servicio está vacío
                raise ValueError("Nombre del servicio vacío")  # Muestra error si está vacío

            # Validamos precio
            if precio_base <= 0:  # Verifica que el precio base no sea 0
                raise ValueError("Precio inválido")  # Muestra error si está vacío

            
            self._nombre = nombre  # Obtiene el nombre del servicio, es un atributo protegido
            self._precio_base = precio_base  # Obtiene el precio base, atributo protegido

            logging.info(f"Servicio creado: {nombre}")  # Guarda en log la información del servicio
        except ValueError as error:  # Captura el error

            logging.error(error)  # Guarda el error en el archivo log

            raise ServicioError("No se pudo crear el servicio") from error  # Muestra el mensaje de error 
         
        # Método abstracto
    @abstractmethod
    def calcular_costo(self):  # Se usará para calcular costo en cada tio de servicio
        pass

    # Método abstracto
    @abstractmethod
    def descripcion(self):  # Se usará para mostrar datos de la reserva
        pass

    # Método implementado
    def mostrar_info(self):  # Se usará para mostrar toda la información
            # Muestra en pantalla los datos
        print(f"Servicio: {self._nombre}")
        print(f"Precio base: ${self._precio_base}")    


class ReservaSala(Servicio):  # Clase Hija de Servicio

    
    def __init__(self, nombre, precio_base, horas):  # Inicia el constructor de la clase

        
        super().__init__(nombre, precio_base) # Se llama al contructor de la clase padre

        try:  # Manejará los errores

            
            if horas <= 0:  # Valida que las horas sean mayores a 0
                raise ValueError("Horas inválidas")  # Sino muestra el error y el mensaje

            self.horas = horas  # Guarda las horas

            # Log
            logging.info("ReservaSala creada")  # Guarda la reserva de sala en el archivo log

        except ValueError as error:  # Captura el error

            logging.error(error)  # Guarda el error en el archivo log

            raise ServicioError("Error en ReservaSala") from error  # Muestra error
        
    def calcular_costo(self, impuesto=0.5, descuento=0.3):  # Aquí aplicamos un poliformismo con esta función

        # Cálculo
        total1 = self._precio_base * self.horas
        
        # Aplica Impuesto
        total2 = total1 * impuesto

        # Aplica Descuento
        total3 = total1 * descuento

        total = (total1 + total2 - total3)

        return total  # Devuelve el total a cobrar
    
    def descripcion(self): # Mostrará los datos de la reserva 

        return f"Reserva de sala por {self.horas} horas" # Retornará este mensaje

    # Mostrar información
    def mostrar_info(self):  # Mostrará información completa de la reserva
            # Muestra en pantalla datos
        print("\n===== RESERVA DE SALA =====")
        print(f"Nombre: {self._nombre}")
        print(f"Horas: {self.horas}")
        print(f"Precio base: ${self._precio_base}")


class AlquilerEquipo(Servicio):  # Clase hija de servicio

    # Constructor
    def __init__(self, nombre, precio_base, dias):  # Construye a la clase        

        super().__init__(nombre, precio_base)  # Hace un llamado al constructor de la clase padre

        try:  # Maneja los errores

            
            if dias <= 0:  # Valida que se indique la cantidad de dias
                raise ValueError("Días inválidos")  # Muestra error si no se escribe o si el valor es 0

            self.dias = dias  # Guarda los dias

            logging.info("AlquilerEquipo creado")  # Guarda en el archivo los datos para el servicio 

        except ValueError as error:  # Captura el error

            logging.error(error)  # Guarda el error en el archivo log

            raise ServicioError("Error en AlquilerEquipo") from error  # Muestra error
        
    def calcular_costo(self, impuesto=0.3, descuento=0.1):  # Aplicamos polimorfismo en esta función

        # Cálculo
        total1 = self._precio_base * self.dias
        
        # Aplica Impuesto
        total2 = total1 * impuesto

        # Aplica Descuento
        total3 = total1 * descuento

        total = (total1 + total2 - total3)

        return total  # Devuelve el total del servicio
    
    def descripcion(self):  # Arroja el dato del alquiler en # de días

        return f"Alquiler de equipo por {self.dias} días"

    # Muestra información
    def mostrar_info(self):
            # Se muestra en pantalla toda la informaión del servicio de alquiler
        print("\n===== ALQUILER DE EQUIPO =====")
        print(f"Nombre: {self._nombre}")
        print(f"Días: {self.dias}")
        print(f"Precio base: ${self._precio_base}")

class AsesoriaEspecializada(Servicio):  # Clase hija de servicio

    
    def __init__(self, nombre, precio_base, horas):  # Constructor de la clase

        
        super().__init__(nombre, precio_base)  # Se llama al constructor de la clase padre

        try:  # Se manejan los errores

            
            if horas <= 0:  # Se valida el numero de horas de las asesorias
                raise ValueError("Horas inválidas")  # Muestra un error si es menor a 0

           
            self.horas = horas  # Guarda la cantidad de horas

            
            logging.info("AsesoriaEspecializada creada")  # Guarda en archivo log el servicio creado

        except ValueError as error:  # Captura el error

            logging.error(error)  # Guarda en el archivo log el error

            raise ServicioError("Error en AsesoriaEspecializada") from error  # Muestra el error
        
    def calcular_costo(self, impuesto=0.2, descuento=0.4):  # Se aplica polimorfismo 

        # Cálculo
        total1 = self._precio_base * self.horas
        
        # Aplica Impuesto
        total2 = total1 * impuesto

        # Aplica Descuento
        total3 = total1 * descuento

        total = (total1 + total2 - total3)

        return total  # Retorna el valor total
     # Descripción
    def descripcion(self):  # Muestra la cantidad de Horas de la asesoria

        return f"Asesoría especializada por {self.horas} horas"  # Muestra el valor

    # Mostrar información
    def mostrar_info(self):
                # Muestra información en pantalla de la asesoria
        print("\n===== ASESORÍA =====")
        print(f"Nombre: {self._nombre}")
        print(f"Horas: {self.horas}")
        print(f"Precio base: ${self._precio_base}") 

class Reserva:  # Se crea la clase Reserva, quien creará, confirmará o cancelará la reserva

    
    def __init__(self, cliente, servicio, duracion):  # Constructor de la clase
        try: # Manejará los errores

            
            if cliente is None:  # Valida que se haya escrito el cliente
                raise ReservaError("Cliente inexistente")  # Muestra el error si no se ha escrito el cliente

            
            if servicio is None:  # Valida que se haya escrito el servicio
                raise ReservaError("Servicio inexistente")  # Muestra el error si no se ha escrito el servicio

            
            if duracion <= 0:  # Valida la cantidad de horas del servicio
                raise ReservaError("Duración inválida")  # Muestra el error si no se escribe un valor

            # Captura los Atributos de cliente, servicio y duración
            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion

            
            self.estado = "Pendiente"  # Muestra el estado del servicio

            
            self.fecha = datetime.now()  # Muestra la fecha 
            
            logging.info("Reserva creada")  # Guarda en el archivo log la información de la reserva

        except ReservaError as error:  # Captura el error

            logging.error(error)  # Guarda en el log el error

            print(error)  # Muestra en pantalla el error 
            
    # Confirmar reserva
    def confirmar(self):  # Función que confirmará la reserva

        try:  # Manejará los errores

            if self.estado == "Confirmada":  # validará el estado de confirmación
                raise ReservaError("La reserva ya está confirmada")  # Mostrará que ya está confirmada

            self.estado = "Confirmada"  # Cambio de estado

            # Log
            logging.info("Reserva confirmada")  # Se guardará en el archivo log la reserva confirmada

        except ReservaError as error:  # Captura el error

            logging.error(error)  # Guarda en el log el error

            print(error)  # Muestra en pantalla el error

        else:  # Si no hay error

            print("Reserva confirmada exitosamente")  # Muestra en pantalla la confirmación de la reserva

    def cancelar(self):  # Función que cancelará la reserva

        try: # Manejará los errores

            
            if self.estado == "Cancelada":  # validará el estado de la cancelación
                raise ReservaError("La reserva ya está cancelada")  # Mostrará que ya está cancelada

            self.estado = "Cancelada"  # Cambio de estado

            logging.info("Reserva cancelada")  # Se guardará en el archivo log la reserva cancelada

        except ReservaError as error:  # Captura el error

            logging.error(error)  # Guarda en el log el error

            print(error)  # Muestra en pantalla el error

        else:  # Si no hay error

            print("Reserva cancelada correctamente")  # Muestra en pantalla la cancelación de la reserva

    def procesar(self):  # Función para Procesar la reserva

        try:  # Manejará los errores

            
            if self.estado == "Cancelada":  # Valida si el estado de la reserva es cancelada
                raise ReservaError(  # Si la reserva está cancelada, no se puede procesar
                    "No se puede procesar una reserva cancelada"
                )

            # Cálculo del total
            total = self.servicio.calcular_costo()  # Guarda el costo total

            # Muestra en pantalla la factura, con la información completa
            print("\n===== FACTURA =====")
            print(f"Cliente: {self.cliente.get_nombre()}")
            print(f"Servicio: {self.servicio.descripcion()}")
            print(f"Estado: {self.estado}")
            print(f"Total a pagar: ${total}")

            logging.info("Reserva procesada")  # Se guarda en log la reserva

        except Exception as error:  # Captura el error

            logging.error(error)  # Guarda en log el error

            print(error)  # Muestra en pantalla el error

        finally:  # Ejecuta obligatoriamente lo que tiene dentro

            print("Proceso finalizado\n")  # Muestra en pantalla la finalización del proceso

 # Mostrar información
    def mostrar_reserva(self):  # Función para mostrar toda la información en pantalla
            # Muestra en pantalla datos de la reserva
        print("\n===== RESERVA =====")
        print(f"Cliente: {self.cliente.get_nombre()}")
        print(f"Servicio: {self.servicio.descripcion()}")
        print(f"Duración: {self.duracion}")
        print(f"Estado: {self.estado}")
        print(f"Fecha: {self.fecha}")

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
                    input("Ingrese cantidad de horas solicitadas: ")
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
                    input("Ingrese cantidad de días solicitados: ")
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
                    input("Ingrese cantidad de horas solicitadas: ")
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
                input("Ingrese duración real de la reserva: ")
            )
            servicio.horas = duracion
            servicio.dias = duracion

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

    try: # Se manejan los errores

        confirmar = input(  # Se confirma la reserva
            "\n¿Desea confirmar la reserva? (s/n): "
        )

        if confirmar.lower() == "s":  # Si se presiona s, lo convertirá a minuscula, 

            reserva1.confirmar()  # Mostrará los datos de la reserva y lo confirmará

            operaciones += 1  # Suma una operación

        else:  # Si no presiona s, la reserva no se confirmará

            print("\nReserva no confirmada")  # Mostrará en pantalla 

            operaciones += 1  # Se suma la operación
    except Exception as error:  # Captura el error

        operaciones += 1  # Suma una operación

        print(f"\n{error}")  # Muestra en pantalla el error

    try:  # Manejo de errores

        procesar = input(  # Ingreso del procesamiento de la reserva
            "\n¿Desea procesar la reserva? (s/n): "
        )

        if procesar.lower() == "s":  # Se presiona s, si si va a procesar la reserva

            reserva1.procesar()  # Procesa la reserva

            operaciones += 1  # Suma una operación

        else:  # Si no presiona s, no procesará la reserva

            print("\nReserva no procesada")  # Lo muestra en pantalla

            operaciones += 1  # Suma una operación  
    except Exception as error:  # Captura el error

        operaciones += 1  # Suma una operación

        print(f"\n{error}")  # Muestra en pantalla el error

    print(f"\nOperaciones realizadas: {operaciones}")  # Muestra en pantalla todas las operaciones realizadas
    
    print("\n========= FIN DEL SISTEMA =========")  # Indica la finalización del programa                  