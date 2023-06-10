from Automovil import Automovil

class Particular(Automovil):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada, _numero_puestos):
        super().__init__(_marca, _modelo, _numero_ruedas, _velocidad, _cilindrada)
        self.numero_puestos = _numero_puestos
