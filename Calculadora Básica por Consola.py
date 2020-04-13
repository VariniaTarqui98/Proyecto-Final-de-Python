#        CALCULADORA POR CONSOLA
#     Tarqui Lunda Varinia Stephany

def ingreso_numero():
    global x, y
    x = int(input('Ingrese un número: '))
    y = int(input('Ingrese otro número: '))

def suma():
    print('El resultado es: ', x+y)
    input()

def resta():
    print('El resultado es: ', x-y)
    input()

def producto():
    print('El resultado es: ', x*y)
    input()

def division():
    if y == 0:
        print('No se puede dividir entre 0')
    else:
        print('El resultado es: ', x/y)
        input()

def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False

def opcion_no_disponible():
    print('Opcion no disponible')

# La interfaz del usuario

menu = '''
======= CALCULADORA ======
1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir
'''

sw = True
while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        ingreso_numero()
        suma()
    elif opcion == 2:
        ingreso_numero()
        resta()
    elif opcion == 3:
        ingreso_numero()
        producto()
    elif opcion == 4:
        ingreso_numero()
        division()
    elif opcion == 5:
        terminar_programa()
    else:
        opcion_no_disponible()