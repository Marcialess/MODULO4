from Automovil import Automovil

class Carga(Automovil):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada, _peso_carga):
        super().__init__(_marca, _modelo, _numero_ruedas, _velocidad, _cilindrada)
        self.peso_carga = _peso_carga
