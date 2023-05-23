class Cine:
    def __init__(self, nombre, rut, direccion):
        self.nombre = nombre
        self.rut = rut
        self.direccion = direccion
        self.salas = []
        self.cartelera = []

    # def registrarCine(self, nombre, rut, direccion):
    #     self.nombre = nombre
    #     self.rut = rut
    #     self.direccion = direccion

    def agregarSala(self, sala):
        self.salas.append(sala)

    def agregarFuncion(self, funcion):
        self.cartelera.append(funcion)

    def venderBoleto(self, dia, funcion, asiento, tipo):
        if asiento.estaVendido():
            print("El asiento seleccionado ya está vendido.")
            return

        asiento.vender()

        valor_entrada = tipo.getValor()

        # print("Venta realizada:")
        # print("Cine:", self.nombre)
        # print("Película:", funcion.getPelicula().getNombre())
        # print("Fecha:", dia)
        # print("Horario:", funcion.getHorario())
        # print("Sala:", funcion.getSala().getSala())
        # print("Asiento:", asiento.getNumero())
        # print("Tipo de entrada:", tipo.getNombre())
        # print("Valor de entrada:", valor_entrada)

    def reporteEntradasPorDia(self, dia):
        total_entradas = 0
        for funcion in self.cartelera:
            if funcion.getDia() == dia:
                total_entradas += funcion.getEntradasVendidas()
        return total_entradas

    def reporteEntradasPorFuncion(self, funcion):
        return funcion.getEntradasVendidas()

    def reporteEntradasPorPelicula(self, pelicula):
        total_entradas = 0
        for funcion in self.cartelera:
            if funcion.getPelicula() == pelicula:
                total_entradas += funcion.getEntradasVendidas()
        return total_entradas

    def reporteEntradasPorDiaFuncionPelicula(self, dia, funcion, pelicula):
        if funcion.getDia() == dia and funcion.getPelicula() == pelicula:
            return funcion.getEntradasVendidas()
        else:
            return 0

class Sala:
    def __init__(self, letras_filas, numero_columnas):
        self.letras_filas = letras_filas
        self.numero_columnas = numero_columnas
        self.asientos = self.crearAsientos()

    def crearAsientos(self):
        asientos = []
        for letra_fila in self.letras_filas:
            for numero_columna in range(1, self.numero_columnas + 1):
                tipo = "Normal"  # Puedes ajustar el tipo de asiento según tus necesidades
                asiento = Asiento(letra_fila, numero_columna, tipo)
                asientos.append(asiento)
        return asientos
    
    def agregarAsiento(self, asiento):
        self.asientos.append(asiento)

    def getSala(self):
        return self.numero

    def getAsientos(self):
        return self.asientos

# class Asiento:
#     def __init__(self, fila, columna, tipo):
#         self.fila = fila
#         self.columna = columna
#         self.tipo = tipo
#         self.vendido = False

#     def estaVendido(self):
#         return self.vendido

#     def vender(self):
#         self.vendido = True

#     def getNombre(self):
#         return f"{self.fila}-{self.columna}"

#     def getTipo(self):
#         return self.tipo

class Funcion:
    def __init__(self, pelicula, horario, sala, dia):
        self.pelicula = pelicula
        self.horario = horario
        self.sala = sala
        self.dia = dia
        self.entradas_vendidas = 0

    def getPelicula(self):
        return self.pelicula

    def getHorario(self):
        return self.horario

    def getSala(self):
        return self.sala

    def getDia(self):
        return self.dia

    def getEntradasVendidas(self):
        return self.entradas_vendidas

    def incrementarEntradasVendidas(self):
        self.entradas_vendidas += 1

class Pelicula:
    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self

class TipoEntrada:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def getNombre(self):
        return self.nombre

    def getValor(self):
        return self.valor
    

    def reporte_general(self):
    dates = []
    for ticket in self.ticket_vendido:
        dates.append(ticket["date"])
    dates = list(set(dates))
    
    for date in dates:
        self.total_entradas_vendidas(date)
        
        for funcion in self.cartelera:
            if funcion.date == date:
                print(f'Este es el total de entradas vendidas para la función {funcion.name.title()}: {funcion.getTicketVendido()}')
        
        for pelicula in self.movies:
            contador = 0
            for funcion in self.cartelera:
                if funcion.name.title() == pelicula.title and funcion.date == date:
                    contador += 1
            if contador > 0:
                print(f"La cantidad de tickets vendidos para la película {pelicula.title} es: {contador}")
