from Bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, _marca, _modelo, _numero_ruedas, _tipo, _motor, _cuadro, _nro_radios):
        super().__init__(_marca, _modelo, _numero_ruedas, _tipo)
        self.nro_radios = _nro_radios
        self.cuadro = _cuadro
        self.motor = _motor
