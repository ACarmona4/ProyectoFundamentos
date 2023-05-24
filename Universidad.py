import csv

from Estudiante import *


class Universidad:
    def __init__(self):
        self.estudiantes = []

    def registrar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiantes_por_nombre(self, nombre):
        resultados = []
        for estudiante in self.estudiantes:
            if estudiante.nombre.lower() == nombre.lower():
                resultados.append(estudiante)
        return resultados
    
    def buscar_estudiantes_por_identificacion(self, identificacion):
        resultados = []
        for estudiante in self.estudiantes:
            if estudiante.identificacion.lower() == identificacion.lower():
                resultados.append(estudiante)
        return resultados
    
    def buscar_estudiantes_por_edad(self, edad):
        resultados = []
        for estudiante in self.estudiantes:
            if estudiante.edad == edad:
                resultados.append(estudiante)
        return resultados
    
    def buscar_estudiantes_por_carrera(self, carrera):
        resultados = []
        for estudiante in self.estudiantes:
            if estudiante.carrera.lower() == carrera.lower():
                resultados.append(estudiante)
        return resultados

    def exportar_estudiantes(self, nombre_archivo):
        with open(nombre_archivo, 'w', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow(['Nombre', 'Identificación', 'Edad', 'Carrera', 'Promedio'])
            for estudiante in self.estudiantes:
                promedio = estudiante.calcular_promedio()
                escritor_csv.writerow([estudiante.nombre, estudiante.identificacion, estudiante.edad,
                                       estudiante.carrera, promedio])

def validar_entero_positivo(valor):
    try:
        entero = int(valor)
        if entero <= 0:
            raise ValueError
        return entero
    except ValueError:
        return None

def validar_flotante_positivo(valor):
    try:
        flotante = float(valor)
        if flotante <= 0.0:
            raise ValueError
        return flotante
    except ValueError:
        return None

def imprimir_linea():
    print("--------------------------------------------------")

def imprimir_cuadro(contenido):
    imprimir_linea()
    print(contenido)
    imprimir_linea()

def mostrar_menu():
    imprimir_cuadro("MENÚ PRINCIPAL")
    print("1. Registrar estudiante")
    print("2. Ingresar notas")
    print("3. Búsqueda de estudiantes")
    print("4. Exportar estudiantes")
    print("5. Salir")
    
def mostrar_menu_busqueda():
    imprimir_cuadro("MENÚ BÚSQUEDA DE ESTUDIANTES")
    print("1. Buscar estudiante por nombre")
    print("2. Buscar estudiante por identificación")
    print("3. Buscar estudiante por edad")
    print("4. Buscar estudiante por carrera")
    print("5. Volver al menú principal")

def registrar_estudiante(universidad):
    imprimir_cuadro("REGISTRO DE ESTUDIANTE")
    nombre = input("Nombre: ")
    identificacion = input("Identificación: ")
    edad = validar_entero_positivo(input("Edad: "))
    carrera = input("Carrera: ")
    if nombre and identificacion and edad and carrera:
        estudiante = Estudiante(nombre, identificacion, edad, carrera)
        universidad.registrar_estudiante(estudiante)
        imprimir_cuadro("Estudiante registrado correctamente.")
    else:
        imprimir_cuadro("Datos inválidos. El estudiante no pudo ser registrado. Verifique las casillas.")

def ingresar_notas(universidad):
    imprimir_cuadro("INGRESO DE NOTAS")
    identificacion = input("Identificación del estudiante: ")
    estudiante = None
    for e in universidad.estudiantes:
        if e.identificacion == identificacion:
            estudiante = e
            break
    if estudiante:
        while True:
            nota_str = input("Ingrese una nota (o 'f' para terminar): ")
            if nota_str == 'f':
                break
            nota = validar_flotante_positivo(nota_str)
            if nota is not None:
                estudiante.agregar_nota(nota)
                imprimir_cuadro("Nota agregada correctamente.")
            else:
                imprimir_cuadro("Nota inválida. Intente nuevamente.")
    else:
        imprimir_cuadro("No se encontró un estudiante con la identificación proporcionada.")

def buscar_estudiante_nombre(universidad):
    i = 1
    imprimir_cuadro("BÚSQUEDA DE ESTUDIANTE POR NOMBRE")
    nombre = input("Nombre del estudiante: ")
    resultados = universidad.buscar_estudiantes_por_nombre(nombre)
    if resultados:
        for estudiante in resultados:
            imprimir_cuadro(f'ESTUDIANTE {i}')
            imprimir_cuadro(f"Nombre: {estudiante.nombre}")
            imprimir_cuadro(f"Identificación: {estudiante.identificacion}")
            imprimir_cuadro(f"Edad: {estudiante.edad}")
            imprimir_cuadro(f"Carrera: {estudiante.carrera}")
            promedio = estudiante.calcular_promedio()
            imprimir_cuadro(f"Promedio: {promedio}")
            i+=1
    else:
        imprimir_cuadro("No se encontraron estudiantes con el nombre proporcionado.")
        
def buscar_estudiante_identificacion(universidad):
    i = 1
    imprimir_cuadro("BÚSQUEDA DE ESTUDIANTE POR ID")
    identificacion = input("Identificación: ")
    resultados = universidad.buscar_estudiantes_por_identificacion(identificacion)
    if resultados:
        for estudiante in resultados:
            imprimir_cuadro(f'ESTUDIANTE {i}')
            imprimir_cuadro(f"Nombre: {estudiante.nombre}")
            imprimir_cuadro(f"Identificación: {estudiante.identificacion}")
            imprimir_cuadro(f"Edad: {estudiante.edad}")
            imprimir_cuadro(f"Carrera: {estudiante.carrera}")
            promedio = estudiante.calcular_promedio()
            imprimir_cuadro(f"Promedio: {promedio}")
            i+=1
    else:
        imprimir_cuadro("No se encontraron estudiantes con la identificación proporcionada.")
        
def buscar_estudiante_edad(universidad):
    i = 1
    imprimir_cuadro("BÚSQUEDA DE ESTUDIANTE POR EDAD")
    edad = validar_entero_positivo(input("Edad: "))
    if edad is not None:
        resultados = universidad.buscar_estudiantes_por_edad(edad)
        if resultados:
            for estudiante in resultados:
                imprimir_cuadro(f'ESTUDIANTE {i}')
                imprimir_cuadro(f"Nombre: {estudiante.nombre}")
                imprimir_cuadro(f"Identificación: {estudiante.identificacion}")
                imprimir_cuadro(f"Edad: {estudiante.edad}")
                imprimir_cuadro(f"Carrera: {estudiante.carrera}")
                promedio = estudiante.calcular_promedio()
                imprimir_cuadro(f"Promedio: {promedio}")
                i+=1
        else:
            imprimir_cuadro("No se encontraron estudiantes con la edad proporcionada.")
    else:
        imprimir_cuadro("Error al buscar. Ingrese una edad válida.") 
        
def buscar_estudiante_carrera(universidad):
    i = 1
    imprimir_cuadro("BÚSQUEDA DE ESTUDIANTE POR CARRERA")
    carrera = input("Carrera: ")
    resultados = universidad.buscar_estudiantes_por_carrera(carrera)
    if resultados:
        for estudiante in resultados:
            imprimir_cuadro(f'ESTUDIANTE {i}')
            imprimir_cuadro(f"Nombre: {estudiante.nombre}")
            imprimir_cuadro(f"Identificación: {estudiante.identificacion}")
            imprimir_cuadro(f"Edad: {estudiante.edad}")
            imprimir_cuadro(f"Carrera: {estudiante.carrera}")
            promedio = estudiante.calcular_promedio()
            imprimir_cuadro(f"Promedio: {promedio}")
            i+=1
    else:
        imprimir_cuadro("No se encontraron estudiantes con la carrera proporcionada.")

def exportar_estudiantes(universidad):
    imprimir_cuadro("EXPORTAR ESTUDIANTES")
    nombre_archivo = input("Nombre del archivo CSV: ")
    universidad.exportar_estudiantes(nombre_archivo)
    imprimir_cuadro("Estudiantes exportados correctamente.")
