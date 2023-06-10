import csv
from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada):
        super().__init__(_marca, _modelo, _numero_ruedas)
        self.velocidad = _velocidad
        self.cilindrada = _cilindrada

    def ingresar_automovil(self):
        cantidad_vehiculos = int(input("Cuántos vehículos desea insertar: "))

        for i in range(cantidad_vehiculos):
            print(f'***** Datos del automovil número {i+1} *****')
            marca = input("Inserte la marca del automovil: ")
            modelo = input("Inserte el modelo: ")
            num_ruedas = int(input("Inserte el número de ruedas: "))
            velocidad = int(input("Inserte la velocidad en km/h: "))
            cilindraje = float(input("Inserte el cilindraje en cc: "))
            automovil = Automovil(
                marca, modelo, num_ruedas, velocidad, cilindraje)
            self.vehiculos.append(automovil)

        print("Imprimiendo por pantalla los Vehículos")
        for i, vehiculo in enumerate(self.vehiculos):
            print(
                f'Datos del automóvil {i+1}: Marca {vehiculo.marca}, Modelo {vehiculo.modelo}, {vehiculo.numero_ruedas} ruedas {vehiculo.velocidad} Km/h, {vehiculo.cilindrada} cc')

    def guardar(self, nombre_archivo):
        with open(nombre_archivo, "w", newline="") as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in self.vehiculos:
                datos = [
                    vehiculo.marca,
                    vehiculo.modelo,
                    vehiculo.numero_ruedas,
                    vehiculo.velocidad,
                    vehiculo.cilindrada
                ]
                archivo_csv.writerow(datos)

    def recuperar(self, nombre_archivo):
        vehiculos = []
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for fila in archivo_csv:
                marca, modelo, num_ruedas, velocidad, cilindrada = fila
                automovil = Automovil(marca, modelo, int(
                    num_ruedas), int(velocidad), float(cilindrada))
                vehiculos.append(automovil)
        return vehiculos

