# Escribir una clase python para encontrar la validaes de una cadena de parentesis,
# '(',')','{','}','['']. Los parentesis deben aparecer en el orden correcto
# por ejemplo "()" y "()[]{}" son validos, pero "[)","({[)]" y "{{{"
# son invalidos

class ValidadorParentesis(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.pila = []
        self.pares = {')': '(', ']': '[', '}': '{'}

    def es_valido(self, cadena):
        try:
            for caracter in cadena:
                if caracter in '([{':
                    self.pila.append(caracter)
                elif caracter in ')]}':
                    if len(self.pila) == 0 or self.pila.pop() != self.pares[caracter]:
                        raise ValidadorParentesis("Los paréntesis no están balanceados")
        except ValidadorParentesis as error:
            print(error)
            return False
        return len(self.pila) == 0


# Ejemplo de uso
validador = ValidadorParentesis("Los paréntesis no están balanceados")
cadena = input("ingrese el caracter:")
resultado = validador.es_valido(cadena)
if resultado:
    print("Los paréntesis están balanceados correctamente")

()