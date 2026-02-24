class Cebolla:
    def __init__(self):
        self.nombre = "Cebolla"
        self.vida = 100

    def recibir_corte(self):
        self.vida -= 50
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} tiene {self.vida}% de vida")

    def esta_listo(self):
        return self.vida == 0

    def mostrar_info(self):
        return f"{self.nombre} - Vida {self.vida}%"