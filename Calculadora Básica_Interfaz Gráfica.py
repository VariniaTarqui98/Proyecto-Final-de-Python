#        CALCULADORA CON INTERFAZ GRÁFICA
#     Tarqui Lunda Varinia Stephany

# Importación de la librería tkinter
import tkinter as tk

root = tk.Tk()

mensaje = tk.StringVar()

sw = False

#def ingreso_numero():
#    global x, y
#   x = int(caja_x.get())
#   y = int(caja_y.get())

def suma():
    valor1 = int(caja_valor1.get())
    valor2 = int(caja_valor2.get())
    print('El resultado de la suma es: ', valor1 + valor2)
    mensaje.set(valor1 + valor2)

def resta():
    valor1 = int(caja_valor1.get())
    valor2 = int(caja_valor2.get())
    print('El resultado de la resta es: ', valor1 - valor2)
    mensaje.set(valor1 - valor2)


def producto():
    valor1 = int(caja_valor1.get())
    valor2 = int(caja_valor2.get())
    print('El resultado del producto es: ', valor1 * valor2)
    mensaje.set(valor1 * valor2)


def division():
    valor1 = int(caja_valor1.get())
    valor2 = int(caja_valor2.get())
    if valor2 == 0:
        print('No se puede dividir entre 0')
        mensaje.set('No se puede dividir entre 0')
    else:
        print('El resultado de la división es: ', valor1 / valor2)
        mensaje.set(valor1 / valor2)


#Pantalla
root.geometry('370x225')
root.title('CALCULADORA')
# Color
root.configure(bg="#F0F4C3")

# Etiquetas
tk.Label(root, text='Operaciones', bg="#F0F4C3", fg='black', font=('', 12)).place(x=223, y=18)
tk.Label(root, text='Valor 1 ', bg="#F0F4C3", fg='black', font=('', 11)).place(x=40, y=50)
tk.Label(root, text='Valor 2 ', bg="#F0F4C3", fg='black', font=('', 11)).place(x=40, y=90)

# Ingreso de Números
caja_valor1 = tk.Entry(justify='center')
caja_valor1.place(x=120, y=50, width=50, height=25)
caja_valor2 = tk.Entry(justify='center')
caja_valor2.place(x=120, y=90, width=50, height=25)


# Suma
tk.Button(text="Sumar", command=suma).place(x=250, y=45)

# Resta
tk.Button(text="Restar", command=resta).place(x=251, y=75)

# Multiplicación
tk.Button(text="Multiplicar", command=producto).place(x=238, y=105)

# División
tk.Button(text="Dividir", command=division).place(x=251, y=134)

# Resultado
tk.Label(root, text='Resultado', bg="#F0F4C3", fg='black', font=('', 11)).place(x=30, y=130)
tk.Entry(root, justify='center', textvariable=mensaje, bg="#FFECB3", fg='black', font=('', 10)).place(x=120, y=130, width=50, height=25)

# Salir
tk.Button(root, text='Salir', command=root.destroy).place(x=178, y=195)


root.mainloop()