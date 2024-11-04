from tarea import Tarea
from lista import Lista

# opciones = ["Agregar", "Modificar", "Elminar", "Salir"]
opcion = 0
while opcion != 3:
    # DEFINIDOS LAS OPCIONES DEL MENU
    print(f"MENU DE OPCIONES \n <0> Agregar Tarea \n <1> Modificar Tarea \n <2> Eliminar tarea \n <3> Salir \n")
    # SE INGRESA LA OPCION DEL MENU
    opcion = int(input("Ingresar opcion: "))
    #CONDICIONES
    if opcion < 0 or opcion > 3:
        print(">>> LA OPCION INGRESADA NO SE ENCUENTRA DENTRO DEL RANGO")
    else:
        lista1 = Lista("Tareas.json")
        
        if opcion == 0:
            titulo = input("INGRESA TITULO: ")
            contenido = input("INGRESA CONTENIDO: ")
            
            tarea1 = Tarea(titulo,contenido)

            lista1.add_tarea(tarea1)

    # SALTO DE LINEA - FINAL DEL CODIGO
        print("\n")
#### ESTRUCUTRA DEL PROGRAMA
# MENU
# COMANDOS