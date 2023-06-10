from Automovil import Automovil
from Vehiculo import Vehiculo
from Carga import Carga
from Particular import Particular
from Bicicleta import Bicicleta
from Motocicletas import Motocicleta

auto1 = Automovil('', '', '', '', '')
auto1.ingresar_automovil()
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
print('\n*****Verificación de Objetos*****')
print(f'Marca {particular.marca}, Modelo {particular.modelo}, {particular.numero_ruedas} ruedas {particular.velocidad} Km/h, {particular.cilindrada} cc Puestos:{particular.numero_puestos}')
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
print(f'Marca {carga.marca}, Modelo {carga.modelo}, {carga.numero_ruedas} ruedas {carga.velocidad} Km/h, {carga.cilindrada} cc Carga:{carga.peso_carga}')
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
print(f'Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.numero_ruedas} ruedas, Tipo: {bicicleta.tipo}')
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
print(f'Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.numero_ruedas} ruedas, Tipo: {motocicleta.tipo}, Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Número de Radios: {motocicleta.nro_radios}')
print('\n*****Verificación de Relaciones*****')
print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automóvil:", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))

auto1.guardar("ejemplo.csv")
automoviles = auto1.recuperar("ejemplo.csv")
for automovil in automoviles:
    print(automovil.marca, automovil.modelo, automovil.numero_ruedas, automovil.velocidad, automovil.cilindrada)
