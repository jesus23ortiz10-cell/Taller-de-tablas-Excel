from Usuario import Usuario
from Carro import Carro
from Parqueadero import Parqueadero

obj_usuario1 = Usuario("Jesus", "10904251", "Cliente")
obj_carro1 = Carro("TXS101", "Toyota", "Negro")
obj_parqueadero = Parqueadero("P4", "23/02/26", "6:59", "Ocupado")

obj_usuario1.mostrar_info()
obj_carro1.mostrar_info()
obj_parqueadero.mostrar_info()
obj_parqueadero.registrar_salida("9:20")
obj_parqueadero.mostrar_info()