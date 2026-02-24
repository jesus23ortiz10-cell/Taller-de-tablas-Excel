from Usuario import usuario
from Numero import numero 
from Calculadora import calculadora

obj_usuario = usuario ( "Eduardo", "231008")
obj_usuario.imprimir_info
print()

# Crear numeros
num1=numero(3)
num2=numero(5)

num1.mostrar_info()
num2.mostrar_info()
print()

calc = calculadora(num1.get_num(), num2.get_num(), "2026,2,15")

print (f"suma:",calc.calculo("suma"))
print (f"resta:",calc.calculo("resta"))
print (f"multiplicacion:", calc.calculo("multiplicacion"))
print (f"division", calc.calculo("division"))
