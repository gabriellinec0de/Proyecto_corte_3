import csv
from os import system
Articulos=[]
def menu_articulos():
    system("cls")
    while True:
        print('''
        ____MENU__ARTICULOS___
        | 1.Acceder a la Lista de Articulos
        | 2.Agregar un nuevo articulo
        | 3.Modificar los Elementos de la lista de Articulos
        | 4.Eliminar el Articulo Deseado
        | 5.Volver al Menu Principal
        ''')
        op_menu_articles=int(input('ingrese su eleccion-> '))
        if op_menu_articles==1:
            acceder_articles()
        elif op_menu_articles==2:
            agregar_article()
        elif op_menu_articles==3:
            modificar_article()
        elif op_menu_articles==4:
            eliminar_article()
        elif op_menu_articles==5:
            input('regresando al menu principal')
            break
        else:
            print('eleccion invalida por favor intente de nuevo')

def acceder_articles():
    system("cls")
    print("Accediendo a los articulos")
    try:
        names_=['Codigo_propiedad','Tamaño_propiedad','Numero_habitaciones','Propiedad_amueblada']
        with open("Aticle_list.txt","r",encoding="UTF-8",newline="") as fil:
            csv_file=csv.DictReader(fil,fieldnames=names_,quotechar='"')
            print("La lista de articulos son")
            for row in csv_file:
                Articulos.append(row)
                print(f"\t{row['Codigo_propiedad']}---{row['Tamaño_propiedad']}---{row['Numero_habitaciones']}---{row['Propiedad_amueblada']}")
    except FileNotFoundError:
        print('ocurrio un error ')

def agregar_article():
    system('cls')
    new_article={}
    while(True):
        print('Agregando un articulo nuevo')
        codigo_propiedad=int(input('Ingrese el codigo del inmueble-> '))
        tamaño_propiedad=int(input('Ingrese el tamaño de la propiedad en metros cuadrados-> '))
        numero_habitaciones=int(input('Ingrese el numero de habitaciones del inmueble->  '))
        propiedad_amueblada=input('Esta la propiedad amueblada [si/no]-> ')
        new_article["Codigo_propiedad"]=codigo_propiedad
        new_article["Tamaño_propiedad"]=tamaño_propiedad
        new_article["Numero_habitaciones"]=numero_habitaciones
        if propiedad_amueblada=="si":
            new_article["Propiedad_amueblada"]=True
        elif propiedad_amueblada=="no":
            new_article["Propiedad_amueblada"]=False
        else :
            new_article["Propiedad_amueblada"]=False
        Articulos.append(new_article)
        seleccion=input('Desea agregar otro articulo-[si/no]=> ')
        if seleccion=="si":
            continue
        elif seleccion=="no":
            tipo_escritura=False
            escribir_archivo(Articulos,tipo_escritura)
            break

def escribir_archivo(articles,tipo_archivo):
    if tipo_archivo==False:
        try:
            fieldnames_=['Codigo_propiedad','Tamaño_propiedad','Numero_habitaciones','Propiedad_amueblada']
            with open("Aticle_list.txt","a",encoding="UTF-8",newline="") as file:
                csv_write=csv.DictWriter(file,fieldnames=fieldnames_,delimiter=",",quotechar='"')
                for row in articles:
                    csv_write.writerow(row)
            print("Los datos fueron agregados en la BD correctamente")
        except FileNotFoundError:
            print('ocurrio un error ')
    elif tipo_archivo==True:
        try:
            fieldnames_=['Codigo_propiedad','Tamaño_propiedad','Numero_habitaciones','Propiedad_amueblada']
            with open("Aticle_list.txt","w",encoding="UTF-8",newline="") as file:
                csv_write=csv.DictWriter(file,fieldnames=fieldnames_,delimiter=",",quotechar='"')
                for row in articles:
                    csv_write.writerow(row)
            print("Los datos fueron agregados en la BD correctamente")
        except FileNotFoundError:
            print('ocurrio un error ')

def modificar_article():
    system('cls')
    print('--Modificando un articulo-- ')
    try:
        fieldnames_=['Codigo_propiedad','Tamaño_propiedad','Numero_habitaciones','Propiedad_amueblada']
        with open("Aticle_list.txt","r",encoding="UTF-8",newline="") as file:
            csv_write=csv.DictReader(file,fieldnames=fieldnames_,delimiter=",",quotechar='"')
            print("Articulos en lista:")
            x=0
            for row in csv_write:
                Articulos.append(row)
                print(x,row.values())
                x+=1
            ident=int(input("seleccione el articulo que desea modificar->"))
            mody_file=Articulos.pop(ident)
            print('======================================================')
            y=1
            for miror in mody_file.items():
                print(y,miror,"\n")
                y+=1
            op_sel=int(input('Ingrese el numero del elemento a modificar-> '))
            if op_sel==1:
                print('Usted selecciono -- codigo propiedad--')
                new_date=input('Ingrese el dato nuevo-> ')
                mody_file.update("Codigo_propiedad",new_date)
            elif op_sel==2:
                print('Usted selecciono -- tamaño de la propiedad--')
                new_date=input('Ingrese el dato nuevo-> ')
                mody_file.update("Codigo_propiedad",new_date)
            elif op_sel==3:
                print('Usted selecciono -- numero de habitaciones --')
                new_date=input('Ingrese el dato nuevo-> ')
                mody_file.update("Codigo_propiedad",new_date)
            elif op_sel==4:
                print('Usted selecciono -- propiedad amueblada --')
                new_date=input('Ingrese el dato nuevo-> ')
                mody_file.update({"Codigo_propiedad":new_date})
            else:
                print('Opcion invalida ')
            Articulos.append(mody_file)
            tipo_archivo=True
            escribir_archivo(Articulos,tipo_archivo)
            print('Datos actualizados correctamente')
    except FileNotFoundError:
        print('ocurrio un error ')

def eliminar_article():
    system('cls')
    print('--eliminanado un articulo-- ')
    try:
        fieldnames_=['Codigo_propiedad','Tamaño_propiedad','Numero_habitaciones','Propiedad_amueblada']
        with open("Aticle_list.txt","r",encoding="UTF-8",newline="") as file:
            csv_write=csv.DictReader(file,fieldnames=fieldnames_,delimiter=",",quotechar='"')
            print("Articulos en lista:")
            x=0
            for row in csv_write:
                Articulos.append(row)
                print(x,row.values())
                x+=1
            ident=int(input("seleccione el articulo que desea eliminar->"))
            mody_file=Articulos.pop(ident) #posibilidad de guardar el registro eliminado
            tipo_archivo=True
            escribir_archivo(Articulos,tipo_archivo)
            print('Datos actualizados correctamente')
            print('======================================================')
    except FileNotFoundError:
        print('ocurrio un error ')

if __name__=="__main__":
    menu_articulos()