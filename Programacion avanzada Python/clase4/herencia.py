class Padre:
    def __init__(self, _name_padre, _rut_padre):
        self.name = _name_padre
        self.rut_padre = _rut_padre
        self.money = 0

    def pintar(self, _color):
        print(f'{self.name} esta pintando con el color {_color}')


class Hijo(Padre):
    def __init__(self, _name_hijo, _rut_hijo,_color_ojos):
        super().__init__(_name_hijo, _rut_hijo)
        self.color_ojos = _color_ojos

    def lijar(self):
        print(f'{self.name} esta lijando')


Diego = Hijo("Diego Carreño", 26,"Brown")
Marcial = Padre("Marcial Abad",25)

print(Marcial.name, Marcial.money)
print(Diego.name,Diego.money)

Diego.pintar("green")
Marcial.pintar("brown")