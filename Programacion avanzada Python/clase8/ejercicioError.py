# Generar en diferentes class, al menos una clase por error
# las siguientes exceptions
# - TypeError
# - IndexError
# - KeyError?

# class IndexTypeError:
#     def __init__(self, _mensaje):
#         self.mensaje = _mensaje

# data = ["computer",47,"im,cadena"]

# try:
#     print(data[int(input("into your range: "))])
# except IndexError as error:
#         print(error)


class KeyErrorExample:
    def __init__(self):
        self.dict = {
            "name": "John",
            "age": 30,
            "city": "New York",
            "sex": "M"
        }

    def intentar(self):
        try:
            key = input("into your key: ")
            (self.dict[key])
        except KeyError as error:
            print("esto no es un valor de la key")
            
            


prueba = KeyErrorExample()
prueba.intentar()
