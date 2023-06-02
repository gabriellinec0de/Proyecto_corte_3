import csv
ventas=[]
def realizar_venta():
    venta_realiz={}
    codigo=input('Ingrese el codigo de la venta-> ')
    direccion =input("Ingrese la codigo del inmueble->  ")
    documento_usuario=input('ingrese le documento del usuario-> ')
    fieldnames = ["cedula", "nombre", "apellido", "edad", "propiedades"]
    with open("carpeta_ususarios\data.txt", "r", encoding="UTF-8", newline="") as f:
        csv_file = csv.DictReader(f, fieldnames=fieldnames, quotechar='"')
        for raw in csv_file:
            if documento_usuario==raw.get("cedula"):
                names_=['Codigo_propiedad','Tamaño_propiedad','Numero_habitaciones','Propiedad_amueblada']
                with open("carpeta_articulos\Aticle_list.txt","r",encoding="UTF-8",newline="") as archivo:
                    csv_file=csv.DictReader(archivo,fieldnames=names_,quotechar='"')
                    for row in csv_file:
                            if direccion==row.get('Codigo_propiedad'):
                                precio_metro_cuadrado = int(input("Ingrese el precio por metro cuadrado->  "))
                                area = int(row.get('Tamaño_propiedad'))
                                precio_total = precio_metro_cuadrado * area
                                venta_realiz["codigo_venta"]=codigo
                                venta_realiz["codigo_propiedad"]=direccion
                                venta_realiz["documento_usuario"]=documento_usuario
                                venta_realiz["precio_venta"]=precio_total
                                ventas.append(venta_realiz)
                                try:
                                    fieldnames_=["codigo_venta","codigo_propiedad","documento_usuario","precio_venta"]
                                    with open("ventas.txt","a",encoding="UTF-8",newline="") as file:
                                        csv_write=csv.DictWriter(file,fieldnames=fieldnames_,delimiter=",",quotechar='"')
                                        for row in ventas:
                                            csv_write.writerow(row)
                                    print("Los datos fueron agregados en la BD correctamente")
                                except FileNotFoundError:
                                    print('ocurrio un error ')

def editar_ventas():
    codigo = input("Ingrese el código de la venta a editar: ")
    ventas = []
    with open('ventas.txt', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] == codigo:
                direccion = input("Ingrese la nueva dirección del inmueble: ")
                precio_metro_cuadrado = float(input("Ingrese el nuevo precio por metro cuadrado: "))
                area = float(input("Ingrese el nuevo área del inmueble en metros cuadrados: "))
                precio_total = precio_metro_cuadrado * area
                fila[1] = direccion
                fila[2] = precio_metro_cuadrado
                fila[3] = area
                fila[4] = precio_total
                print("La venta se ha editado correctamente.")
            ventas.append(fila)

    with open('ventas.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        for venta in ventas:
            escritor.writerow(venta)

def eliminar_registros_ventas():
    codigo = input("Ingrese el código de la venta a eliminar: ")
    ventas = []
    eliminado = False
    with open('ventas.txt', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] != codigo:
                ventas.append(fila)
            else:
                eliminado = True

    with open('ventas.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        for venta in ventas:
            escritor.writerow(venta)

    if eliminado:
        print("La venta se ha eliminado correctamente.")
    else:
        print("No se encontró ninguna venta con el código ingresado.")

def mostrar_menu():
    while True:
        print('__MENU--VENTAS__')
        print("1. Realizar la venta de un predio")
        print("2. Editar ventas")
        print("3. Eliminar registros de ventas")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            realizar_venta()
        elif opcion == '2':
            editar_ventas()
        elif opcion == '3':
            eliminar_registros_ventas()
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__=="__main__":
    mostrar_menu()