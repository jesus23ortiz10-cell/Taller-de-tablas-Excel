class numero:
    def __init__(self,num):
        self.num = num

    def get_num (self):
        return self.num
    
    def set_num (self, numero_nuevo):
        self.num = numero_nuevo

    def mostrar_info(self):
        print(f"numero: {self.num}")