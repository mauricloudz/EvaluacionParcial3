import time
import FuncionesEvaluacion3 as fn

print("Bienvenido a automotora Auto Seguro.")
usuario = input("Ingrese su nombre: ")

def main():
    registro = {}
    
    while True:
        print("\nPor favor elija una opcion: ")
        print("1. Grabar vehículo")
        print("2. Buscar vehículo")
        print("3. Imprimir certificados")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            fn.grabar_vehiculo(registro)
        elif opcion == "2":
            fn.buscar_vehiculo(registro)
        elif opcion == "3":
            fn.imprimir_certificados(registro)
        elif opcion == "4":
            print(f"Hasta luego {usuario}. Gracias por usar Auto Seguro.\nversion 1.0")
            print("Cerrando...")
            time.sleep(5)
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

if __name__ == "__main__":
    main()
