from Universidad import *
import csv



class Main:
    def __init__(self):
        self.universidad = Universidad()

    def run(self):
        while True:
            mostrar_menu()
            opcion = input("Ingrese una opción: ")

            if opcion == '1':
                registrar_estudiante(self.universidad)
            elif opcion == '2':
                ingresar_notas(self.universidad)
            elif opcion == '3':
                buscar_estudiante_nombre(self.universidad)
            elif opcion == '4':
                buscar_estudiante_identificacion(self.universidad)
            elif opcion == '5':
                buscar_estudiante_edad(self.universidad)
            elif opcion == '6':
                buscar_estudiante_carrera(self.universidad)
            elif opcion == '7':
                exportar_estudiantes(self.universidad)
            elif opcion == '8':
                imprimir_cuadro("¡Hasta luego!")
                break
            else:
                imprimir_cuadro("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    programa = Main()
    programa.run()