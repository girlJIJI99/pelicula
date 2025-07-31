
#CODIGO ZOE
#CODIGO ZOE 
#CODIGO ZOEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
votos = {}


def ingresar_datos ( ) :
    numerocategorias = int( input (" Escribe las categorias que desas ingresar"))
    
    for _ in range(numerocategorias):
        categ = input(" Nombre de  la categoria : ")
        votos[categ] = {}
        num_peliculas = int(input(f"Cual es el numero de pelicualas que hay en  '{categ}'?: "))
        
        for _ in range(num_peliculas):
            pelicula = input("  Nombre de la película:  ")
            votos[categ][pelicula] = 0


def votar():
    print (" VOTACION ")
    for categ, peliculas in votos.items():
        print (f"Categoria:  { categ}")
        print(" Opciones:")
        for i, pelicula in enumerate(peliculas, 1):
            print(f"{i}. { pelicula }")
        
        opcion = int (input("Escribe el numero de pelicula por la que sera tu votacion : ") )
        pelicula_elegida =   list(peliculas.keys()) [ opcion - 1 ]
        votos [categ] [pelicula_elegida] += 1
        print (f"Voto registrado para {  pelicula_elegida}")


def mostrar_resultados():
    print("\n RESULTADOS :")
    for categ, peliculas in votos.items():
        print(f" {categ}")
        for pelicula, cantidad in peliculas.items():
            print(f" {pelicula}: {cantidad} votos")

def ganadores():
    print("\n Categroaias ganadoras:")
    for categ, peliculas in votos.items():
        ganadora = max(peliculas, key=peliculas.get)
        print(f"   {categ}: {ganadora} con {peliculas[ganadora]} votos  ")
#MORELIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA





categorias ={}

def registrar_pelicula():
    print("Registre una pelicula segun su categoria")
    categ= input("Ingrese la categoria ").strip()
    pelicula = input("Ingrese el nombre del programa").strip

    if categ not in categorias:
        categorias[categ] = {} 
        
    if pelicula in categorias[categ]:
        print(f"La película '{pelicula}' ya está registrada en la categoría '{categ}'.")
    else:
        categorias[categ][pelicula] = 0
        print(f"Película '{pelicula}' registrada en la categoría '{categ}' con 0 votos.")

def votar_pelicula():
    print("Vota por una categoria")
    categ= input("Ingrese la categoria al que desea votar")
    pelicula = input("Ingrese la pelicula a votar")

    try:
        if categ not in categorias:
            raise KeyError("La categoria no existe")
        
        if pelicula not in categorias:
            raise ValueError("La pelicula no se encuentra en esta categoria ")
         
        categorias[categ][pelicula] += 1
        print(f"Voto registrado para '{pelicula}' en la categoría '{categ}'.")
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar película")
        print("2. Votar película")
        print("3. Mostrar resultados")
        print("4. Determinar ganadoras por categoría")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número del 1 al 5.")
            continue

        if opcion == 1:
            registrar_pelicula()
        elif opcion == 2:
            votar_pelicula()
        elif opcion == 3:
            mostrar_resultados()
        elif opcion == 4:
            ganadores()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción fuera de rango, intente de nuevo.")

menu()