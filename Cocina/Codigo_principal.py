from Tomate import Tomate
from Cebolla import Cebolla
from Agua import    Agua
from pasta import   Pasta
from Cuchillo import cuchillo
from Olla import Olla

Tomate = Tomate()
Cebolla = Cebolla()
Agua = Agua()
Pasta = Pasta()
cuchillo = cuchillo()
Olla = Olla()

print(Tomate.mostrar_info())
print(Cebolla.mostrar_info())
print(Agua.mostrar_info())
print(Pasta.mostrar_info())
print(cuchillo.mostrar_info())
print(Olla.mostrar_info())

print("Cortar ingredientes")

cuchillo.cortar(Tomate)
cuchillo.cortar(Cebolla)

print(Tomate.mostrar_info())
print(Cebolla.mostrar_info())
print(cuchillo.mostrar_info())

print("Afilar cuchillo")

cuchillo.afilar()
print(cuchillo.mostrar_info())

print("Hervir agua")

Agua.hervir()
print(Agua.mostrar_info())

print("Cocinar pasta")

Pasta.cocinar ()
print(Pasta.mostrar_info())

print("Agregar a la olla")

Olla.agregar(Tomate)
Olla.agregar(Cebolla)
Olla.agregar(Pasta)

print(Olla.mostrar_info())