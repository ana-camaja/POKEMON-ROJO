import os
import requests
from TIENDA import tienda

def menu_inicial():
    os.system('cls')
    os.system('color E0')
    
    print('\n\t\tBIENVENIDO A POKEMON ROJO \n')
    print('\t Ingrese su nombre de entrenador Pokemon')
    entrenador= input('\t ')
    print('\t Pokemon inicial-- Pokemons disponibles:')
    print('\t 1->Bulbasaur')
    print('\t 2->Charmander')
    print('\t 3->Squirtle')
    res = str(input('\t ->'))
    if res=='1':
        acceder=1
        menu_principal(acceder)
    elif res=='2':
        acceder=4
        menu_principal(acceder)
    elif res=='3':
        acceder=7
        menu_principal(acceder)
    else:
        print('\tERROR-> La opción elejida no existe.\n')
        os.system('pause')
        menu_inicial()
    


def menu_principal(opcion):
    while True:
        os.system('color E0')
        os.system('cls')
        res=""
        pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
        pokemon_inicial= pokemon['name']
        print('\n\t\tMENÚ PRINCIPAL')
        print('_________________________________________________________')
        print('\t 1. Equipo Pokemon')
        print('\t 2. Batallas con Pokemons salvajes')
        print('\t 3. Pokédex')
        print('\t 4. Tienda')
        print('\t 0. Salir del juego')
        print('\n\tOPCION: "\t')
        res = str(input('\t '))
        if res=='1':
            equipo_pokemon()
        elif res=='2':
            batalla_pokemon()
        elif res=='3':
            pokedex()
        elif res=='4':
            tienda()
        elif res=='0':
            break
        else:
            print('\tERROR-> La opción elejida no existe.\n')
            os.system('pause')
            
def equipo_pokemon():
    pass
def batalla_pokemon():
    dinero=0
    pocion=0
    superpocion=0
    hiperpocion=0
    pokeball=0
    superball=0
    ultraball=0
    masterball=0
    tienda(pocion,superpocion,hiperpocion,pokeball,superball,ultraball,masterball)
    tienda_objetos(dinero)
def pokedex():
    pass
def tienda_objetos(dinero):
    os.system('cls')
    valor=dinero
    print('\n\t\tTIENDA POKEMON \n')
    print('\t 1-> Comprar objetos curativos')
    print('\t 2-> Comprar Poké Ball')
    res = str(input('\t ->'))
    if res=='1':
        print('\t   NOMBRE           |PUNTOS DE SALUD   |VALOR')
        print('\t-----------------------------------------------_')
        print('\t 1 Poción           |20                |300')
        print('\t 2 Superpoción      |50                |700')
        print('\t 3 Hiperpoción      |200               |1200')
        print('\t 4 Restaurar todo   |Vida completa     |3000')
        opcion= int(input('\t->	'))
        os.system('pause')
    elif res=='2':
        print('\t   NOMBRE           |PROPORCION DE    |VALOR')
        print('\t                    |CAPTURA          |')
        print('\t -------------------------------------------------')
        print('\t 1 Pokéball         |1                |200')
        print('\t 2 Superball        |1.5              |600')
        print('\t 3 Ultraball        |2                |1200')
        print('\t 4 Masterball       |255              |100000')
        opcion= int(input('\t->	'))
        os.system('pause')
    else:
        print('\tERROR-> La opción elejida no existe.\n')
        os.system('pause')

os.system('cls')
os.system('color F0')
print('\n\n\t\t  ANA ELENA CAMAJÁ RODRÍGUEZ   1590219')
print('\t\t  ANA ELENA CAMAJÁ RODRÍGUEZ   1590219')
print('\t\t  ANA ELENA CAMAJÁ RODRÍGUEZ   1590219')
print('\t\t  ANA ELENA CAMAJÁ RODRÍGUEZ   1590219\n')



os.system('pause')
menu_inicial()
print('\t¡FIN PROGRAMA, GRACIAS POR PARTICIPAR ;)  !\n\n\n')
os.system('pause')
