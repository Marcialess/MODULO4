class Cine:
    price_ticket_type = {
        'regular': 4000,
        'vip': 7500,
    }
    
    def __init__(self,_name,_rut,_address):
        self.name = _name
        self.rut = _rut
        self.address = _address
        self.room = []
        self.cartelera = []
        self.ticket_vendido = []
        self.movies = []

    def total_entradas_vendidas(self,date):
        total_entradas_vendidas = 0
        for funcion in self.cartelera:
            if funcion.date == date:
                total_entradas_vendidas += funcion.getTicketVendido()
        print(f'Este el total de entradas vendidas en la fecha {date}: {total_entradas_vendidas}')

    def total_entradas_funcion(self):
        for funcion in self.cartelera:
            print(f'Este el total de entradas vendidas para la funcion {funcion.name.title}: {funcion.getTicketVendido()}')

    def total_entradas_peliculas(self):
        for pelicula in self.movies:

            contador = 0
                
            for ticket in self.ticket_vendido:
                if ticket["movie"] == pelicula.title:
                    contador += 1
            print(f"La cantidad de tickets vendidos para la película {pelicula.title} es : {contador}")

#- como Reportar las entradas totales vendidas por cada dia, película y funcion 
    def reporte_general(self):
        dates = []
        for ticket in self.ticket_vendido:
            dates.append(ticket["date"])
        dates = list(set(dates))  
        for date in dates:
            self.total_entradas_vendidas(date)
            for funcion in self.cartelera:
              if funcion.date == date:  
                print(f'Este el total de entradas vendidas para la funcion {funcion.name.title}: {funcion.getTicketVendido()}')
            for pelicula in self.movies:
                contador = 0
                for funcion in self.cartelera:
                    if funcion.name.title == pelicula.title and funcion.date == date:
                        contador += funcion.getTicketVendido()
                if contador > 0:        
                    print(f"La cantidad de tickets vendidos para la película {pelicula.title} es : {contador}")    




    def add_room (self,_room): 
        self.room.append(_room)

    def add_movie (self,_movie):
        self.movies.append(_movie)    

    def add_function(self,_function):
        self.cartelera.append(_function)

    def venderTicket (self,day,_function,_fila,_columna,type):
        for asiento in _function.room.seat:
            # print(type(asiento.column))
            if asiento.row == _fila and asiento.column == _columna:
                if asiento.vendido == True:
                    print("El asiento seleccionado esta vendido, fuiste bueno")
                    return 
                else:
                    asiento.sell()
                    _function.incrementarTicketVendido()
            

        self.ticket_vendido.append({
            'cine': self.name,
            'movie': _function.name.title,
            'date': day,
            'time': _function.time,
            'seat': _fila+str(_columna),
            'type': type,
            'price': self.price_ticket_type[type]
        })
        self.mostrar_venta()

    def mostrar_venta(self):
        print(self.ticket_vendido)

class Sala:
    def __init__(self,_number,_num_fila,_asientos_por_filas,_room_type):
        self.number = _number
        self.num_fila = _num_fila
        self.asientos_por_filas = _asientos_por_filas
        self.room_type = _room_type
        self.seat = self.crear_asientos()

    def crear_asientos(self):
        seats = []
        for fila in range(97, 97 + self.num_fila):
            for numero in range(1, self.asientos_por_filas + 1):
                asiento = Seat(chr(fila), numero)
                seats.append(asiento)        
        return seats        
                           
class Seat:
    def __init__(self,_row,_column):
        self.row = _row
        self.column = _column
        self.vendido = False
    # Este metodo cambia el status a False para mostrar que el ticket 
    # esta vendido.
    def soldOut(self):
         return self.vendido
    # Este metodo realiza la accion de vender un ticket
    def sell (self):
        self.vendido = True
    # Se obtiene el nombre o numero de asiento
    def getName(self):
        return f"{self.row}-{self.column}"

class Ticket:
    def __init__(self,_id,_movie,_cinema,_room,_date,_time,_price,_ticket_type):
        self.id = _id
        self.movie = _movie
        self.cinema = _cinema
        self.room = _room
        self.date = _date
        self.time = _time
        self.price = _price
        self.ticket_type = _ticket_type

class Function:
    def __init__(self,_movie,_time,_date,_room):
        self.name = _movie
        self.time = _time
        self.date = _date
        self.room = _room
        self.tickets_vendidos = 0

    def getTicketVendido(self):
        return self.tickets_vendidos

    def incrementarTicketVendido(self):
        self.tickets_vendidos += 1

class Movie:
    def __init__(self,_title,_category):
        self.title = _title
        self.category = _category


cineBadPractice = Cine("CineBadPractice","78.323.456-7","En Algun Lugar")

sala3 = Sala("Sala3",4,5,"VIP")

toyStory = Movie("ToyStory5","Todo Publico")
reyLeon = Movie("El Rey Leon","Todo Publico")

funCartelera = Function(toyStory,"12:00","21-05-2023",sala3)


cineBadPractice.add_function(funCartelera)
cineBadPractice.add_room(sala3)
cineBadPractice.add_movie(toyStory)
cineBadPractice.add_movie(reyLeon)

cineBadPractice.venderTicket("21-05-2023",funCartelera,"a",4,"vip")
cineBadPractice.venderTicket("21-05-2023",funCartelera,"a",4,"vip")
cineBadPractice.venderTicket("21-05-2023",funCartelera,"b",5,"vip")
cineBadPractice.venderTicket("21-05-2023",funCartelera,"b",1,"regular")
print(funCartelera.getTicketVendido())


# cineBadPractice.total_entradas_vendidas("21-05-2023")
# cineBadPractice.total_entradas_funcion()
# cineBadPractice.total_entradas_peliculas()
cineBadPractice.reporte_general()














# class Cartelera:
#     def __init__ (self,_date):
#         self.date = _date
#         self.movies = []

#     # Agrega la peliculas en la cartelera.

#     def addMovie(self,_movie,_time,_room):
#         self.movies.append({
#             "title": _movie.title,
#             "category": _movie.category,
#             "time": _time,
#             "room": _room
#         })  
        
        


