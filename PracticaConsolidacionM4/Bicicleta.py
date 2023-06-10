from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, _marca, _modelo, _numero_ruedas, _tipo):
        super().__init__(_marca, _modelo, _numero_ruedas)
        self.tipo = _tipo
