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
                mostrar_menu_busqueda()
                opcion2 = input("Ingrese una opción: ")
                if opcion2 == '1':
                    buscar_estudiante_nombre(self.universidad)
                elif opcion2 == '2':
                    buscar_estudiante_identificacion(self.universidad)
                elif opcion2 == '3':
                    buscar_estudiante_edad(self.universidad)
                elif opcion2 == '4':
                    buscar_estudiante_carrera(self.universidad)
                elif opcion2 == '5':
                    mostrar_menu()
                else:
                    imprimir_cuadro("Opción inválida. Intente nuevamente.")
            elif opcion == '4':
                exportar_estudiantes(self.universidad)
            elif opcion == '5':
                imprimir_cuadro("Ha cerrado la sesión. ¡Hasta luego!")
                break
            else:
                imprimir_cuadro("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    programa = Main()
    programa.run()