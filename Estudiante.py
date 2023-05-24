import csv

class Estudiante:
    def __init__(self, nombre, identificacion, edad, carrera):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = edad
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if len(self.notas) > 0:
            promedio = sum(self.notas) / len(self.notas)
            if (promedio>=3.0):
                print("El estudiante ha aprobado el curso!")
                return promedio
            else:
                print("El estudiante ha reprobado el curso.")
                return promedio
        else:
            print("El estudiante no cuenta con notas registradas.")
            return 0.0
        
            
