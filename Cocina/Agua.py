class Agua:
    def __init__(self):
        self.cantidad = "1 litro"
        self.hirviendo = False

    def hervir(self):
        self.hirviendo = True
        print("El agua está hirviendo")

    def mostrar_info(self):
        estado = "Hirviendo" if self.hirviendo else "Fría"
        return f"Agua - Estado: {estado}"
