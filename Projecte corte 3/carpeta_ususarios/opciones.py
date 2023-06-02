import csv 
def crear_archivo():
    try:
        file_estudiante = "data"
        fieldnames_clientes = ["cedula", "nombre", "apellido", "edad","propiedades"]
        with open (file_estudiante + ".txt", "w", encoding="UTF-8", newline="") as f:
            csv_write = csv.DictWriter(f, fieldnames=fieldnames_clientes, quotechar='"')
            csv_write.writeheader()
    except FileNotFoundError: 
        print("Ocurrio un error.")

def agregar():
    data = []
    while(True):
        base_data = {}
        cedula = input("Ingrese la cedula : ")
        nombre = input("Ingrese el nombre : ").capitalize()
        apellido = input("Ingrese el apellido: ").capitalize()
        edad=int(input("edad del cliente:"))
        propiedades=int(input("cuantas propiedades tiene:"))
        base_data["cedula"] = cedula
        base_data["nombre"] = nombre
        base_data["apellido"] = apellido
        base_data["edad"]=edad
        base_data["propiedades"]=propiedades
        data.append(base_data)
        new = input("Desea agregar otro? [si/no]: ").lower()
        if new == "si":
            continue
        else:
            return data

def escribir_archivo(data):
    
    file_cliente = "data"
    fieldnames = ["cedula", "nombre", "apellido", "edad", "propiedades"]
    with open(file_cliente + ".txt", "a", encoding="UTF-8", newline="") as f:
        csv_write = csv.DictWriter(f, fieldnames=fieldnames, quotechar='"')
        for row in data:
            csv_write.writerow(row)
        print("Los datos fueros agregados")

def editar():
    print("Ha elegido editar cliente")
    identificacion = input("Ingrese el numero de identificacion del cliente que desea editar: ")
    clientes = []
    with open("data.txt", "r", encoding="UTF-8") as archivo:
        lector_csv = csv.DictReader(archivo)
        for cliente in lector_csv:
            clientes.append(cliente)
    cliente_encontrado = None
    for cliente in clientes:
        if cliente["cedula"] == identificacion:
            cliente_encontrado = cliente
            break
    if cliente_encontrado:
        print(f"Cliente encontrado:\n{cliente_encontrado}")
        nuevo_nombre = input("Ingrese el nuevo nombre: ").capitalize()
        nuevo_apellido = input("Ingrese el nuevo apellido: ").capitalize()
        nueva_edad = int(input("Ingrese la nueva edad: "))
        nuevo_propiedades = int(input("Ingrese la cantidad de propiedades actualizada: "))
        cliente_encontrado["nombre"] = nuevo_nombre
        cliente_encontrado["apellido"] = nuevo_apellido
        cliente_encontrado["edad"] = nueva_edad
        cliente_encontrado["propiedades"] = nuevo_propiedades
        with open("data.txt", "w", encoding="UTF-8", newline="") as archivo:
            escritor_csv = csv.DictWriter(archivo, fieldnames=cliente_encontrado.keys())
            escritor_csv.writeheader()
            escritor_csv.writerows(clientes)
        print("Los datos del cliente han sido actualizados.")
    else:
        print("Cliente no encontrado.")

def eliminar():
    
    print("Ha elegido eliminar cliente")
    identificacion = input("Ingrese el número de identificación del cliente que desea eliminar: ")
    clientes = []
    with open("data.txt", "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
        cabecera = lineas[0].strip().split(",")  
        for linea in lineas[1:]:
            cliente = linea.strip().split(",")
            clientes.append(cliente)
    cliente_encontrado = None
    for cliente in clientes:
        if cliente[cabecera.index("cedula")] == identificacion:
            cliente_encontrado = cliente
            break
    if cliente_encontrado:
        print(f"Cliente encontrado:\n{cliente_encontrado}")
        confirmacion = input("¿Está seguro que desea eliminar este cliente? [si/no]: ").lower()
        if confirmacion == "si":
            clientes.remove(cliente_encontrado)
            with open("data.txt", "w", encoding="UTF-8") as archivo:
                archivo.write(",".join(cabecera) + "\n")  
                for cliente in clientes:
                    linea = ",".join(cliente)
                    archivo.write(linea + "\n")
            print("El cliente ha sido eliminado.")
        else:
            print("Operación de eliminación cancelada.")
    else:
        print("Cliente no encontrado.")

def main():
    while True:
        print('__MENU--CLINETES__')
        print("\n1. agregar cliente \n2. modificar cliente \n3. eliminar cliente \n4. salir")
        opcion=int(input("que desea hacer?"))
        if opcion > 4:
            print("error")
        elif opcion == 1:
            crear_archivo()
            data=agregar()
            escribir_archivo(data)
        elif opcion == 2:
            editar()
        elif opcion ==3:
            eliminar()
        elif opcion == 4:
            break

if __name__=="__main__":
    crear_archivo()