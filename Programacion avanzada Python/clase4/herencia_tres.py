# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases
# plazofijo cajahorro. Definir los atributos titular y cantidad y un metodo 
# para imprimir los datos en la clase Cuenta. La clase CajaAhorro tendra un metodo
# para heredar los datos y uno para mostrar la informacion.
# la clase plazoFijo tendra dos atributos propios, plazo e interes. 
# tendra un metodo para obtener el importe del interes(cantidad * interes / 100)
# y otro metodo para mostrar la informacion, datos del titular, plazo, interes y total de interes
# Crear al menos un objeto de cada subclase.

class Cuenta:
    def __init__(self, _titular,_cuenta_numero,_saldo):
        self.titular = _titular
        self.cuenta_numero = _cuenta_numero
        self.saldo = _saldo
   
class PlazoFijo(Cuenta):
    def __init__(self, _titular, _cuenta_numero,_saldo, _plazo, _interes):
        super().__init__(_titular, _cuenta_numero,_saldo)
        self.plazo = _plazo
        self.interes = _interes

    def calcular_importe(self):
        return (((self.interes / 100) * self.saldo)*self.plazo)
    

class CajaAhorro(Cuenta):
    def __init__(self, _titular,_cuenta_numero,_saldo):
        super().__init__(_titular,_cuenta_numero,_saldo)

    def  mostrar_informacion(self):
        print(f"Titular: {self.titular} \n Numero de cuenta: {self.cuenta_numero} \n Saldo: {self.saldo}" )


MariaSol = Cuenta("Maria Antonieta Soledad Infante",2919292,1000)
Johetsy = CajaAhorro("Johetsy Alvarez", 232322, 8700)
Miguel = PlazoFijo("Miguel Velasco", 120203, 10000,2,10)

# MariaSol.mostrar_informacion()

Johetsy.mostrar_informacion()
print(Miguel.calcular_importe())









    






