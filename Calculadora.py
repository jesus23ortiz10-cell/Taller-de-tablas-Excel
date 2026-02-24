class calculadora:
    def __init__(self, num1, num2, fecha):
        self.num1 = num1
        self.num2 = num2
        self.fecha = fecha

    def calculo (self, operacion):
        if operacion == "suma":
            return self.num1 + self.num2
        elif operacion == "resta":
            return self.num1 - self.num2
        elif operacion == "multiplicacion":
            return self.num1 * self.num2
        elif operacion == "division":
            if self.num2 != 0:
                return self.num1 / self.num2
            else: 
                return "error: division por cero no permitido"
        else:
            return "operacion no valida"
        
    def get_num1 (self):
            return self.num1
    def set_num1 (self, nuevo_num1):
        self.num1 = nuevo_num1

    def get_num2 (self):
        return self.num2
    def set_num2 (self, nuevo_num2):
        self.num2 = nuevo_num2
            
    def get_fecha (self):
        return self.fecha
    def set_fecha (self,nueva_fecha):
        self.fecha = nueva_fecha

    def mostrar_info(self):
        print(f"num1: {self.num1}, num2: {self.num2}, fecha: {self.fecha}")