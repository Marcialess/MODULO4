# Autos y Motos, Bicicletas
# Autos [color,tipo_motor,ruedas,cantidad_puertas,]

class Vehiculo:
    def __init__(self, _color,_ruedas,_tipo_freno):
        self.color = _color
        self.ruedas = _ruedas
        self.tipo_freno = _tipo_freno

class VehiculoMotorizado:
    def __init__(self,_tipo_motor,_tipo_encendido):
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido
               

class Auto(Vehiculo,VehiculoMotorizado):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido):
        Vehiculo.__init__(_color, _ruedas, _tipo_freno)
        VehiculoMotorizado.__init__(self, _tipo_motor, _tipo_encendido)
        

    def frenar(self):
        print("Frenando")

class Moto(Vehiculo,VehiculoMotorizado):
    def __init__(self,_color,_ruedas,_tipo_freno,_tipo_motor,_tipo_encendido,_tipo_cadena):
        Vehiculo.__init__(self,_color,_ruedas,_tipo_freno)
        VehiculoMotorizado.__init__(self,_tipo_motor,_tipo_encendido)
        self.tipo_cadena = _tipo_cadena

class Bicicleta(Vehiculo):
    def __init__(self,_color,_ruedas,_tipo_freno,_tipo_manubrio):
        super().__init__(self,_color,_ruedas,_tipo_freno)
        self.tipo_manubrio = _tipo_manubrio

    def pedalear(self,sentido):
        print("Pedalando en hacia {sentido} ")

