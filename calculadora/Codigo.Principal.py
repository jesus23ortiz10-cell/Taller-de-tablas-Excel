import tkinter as tk
from Usuario import usuario
from Numero import numero 
from Calculadora import calculadora

def calcular(operacion):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())

        num1 = numero(n1)
        num2 = numero(n2)

        calc = calculadora(num1.get_num(), num2.get_num(), "2026-02-27")
        resultado = calc.calculo(operacion)

        etiqueta_resultado.config(text="Resultado: " + str(resultado))

    except:
        etiqueta_resultado.config(text="Error: ingrese numeros validos")

def restaurar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado:")
    entrada1.focus()

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")

obj_usuario = usuario("Eduardo", "231008")

tk.Label(ventana, text="Numero 1", bg="yellow").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Numero 2", bg="yellow").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Suma", bg="yellow",
          command=lambda: calcular("suma")).pack(pady=5)

tk.Button(ventana, text="Resta", bg="red",
          command=lambda: calcular("resta")).pack(pady=5)

tk.Button(ventana, text="Multiplicacion", bg="green",
          command=lambda: calcular("multiplicacion")).pack(pady=5)

tk.Button(ventana, text="Division", bg="orange",
          command=lambda: calcular("division")).pack(pady=5)

tk.Button(ventana, text="Restaurar", bg="blue",
          command=restaurar).pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado")
etiqueta_resultado.pack()

ventana.mainloop()