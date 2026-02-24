class Pasta:
    def __init__(self):
        self.nombre = "Pasta"
        self.vida = 100
        self.cocida = False

    def recibir_corte(self):
        self.vida -= 100
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} lista para cocinar")

    def cocinar(self, agua):
        if self.vida == 0 and agua.hirviendo:
            self.cocida = True
            print("La pasta está cocida correctamente")
        else:
            print("No se puede cocinar la pasta")

    def mostrar_info(self):
        estado = "Cocida" if self.cocida else "Cruda"
        return f"{self.nombre} - Estado: {estado}"