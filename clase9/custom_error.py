class NecesitasAgregarGuion(Exception):
    def __init__(self, _message):
        super().__init__(_message)

try:
    guion = input("Introduce tu rut: ")
    if guion.isdigit() == True:
        raise NecesitasAgregarGuion("necesitas agregar guion")
    else:
        print("Rut válido")
except Exception as error:
    print(type(error))
    print(error.args)       

# def validar_guion(self):
