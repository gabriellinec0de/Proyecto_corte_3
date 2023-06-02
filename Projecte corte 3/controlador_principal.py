import carpeta_articulos.Archivos_articulos
import carpeta_ususarios.opciones
import carpeta_ventas.otro
from os import system

while(True):
    system('cls')
    print('''
    __MENU--PRINCIPAL__
    1.Acceder a articulos
    2.Acceder a usuarios
    3.Acceder a ventas
    ''')
    opcion=int(input('ingrese su seleccion-> '))
    if opcion==1:
        carpeta_articulos.Archivos_articulos.menu_articulos()
    elif opcion==2:
        carpeta_ususarios.opciones.main()
    elif opcion==3:
        carpeta_ventas.otro.mostrar_menu()
    else:
        print('Opcion fuera de rango')