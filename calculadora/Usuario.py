class usuario :
    def __init__(self,id,nombre):
        self.nombre = nombre
        self.id = id

    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo

    def get_id(self):
        return self.id
    def set_id(self,nuevo_id):
        self.id = nuevo_id
    

    def imprimir_info(self):
        print(f"nombre: {self.nombre}, id: {self.id}")
