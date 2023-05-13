

class Taza:
    sizes = {
        'small': 'pequeño',
        'medium': 'mediano',
        'large': 'grande'
    }
    def __init__(self) -> None:
            self.size = self.sizes['small']

class Maquina:
    def __init__(self,_tipo_cafe,_cantidad_agua,_cantidad_cafe) -> None:
         self.tipo_cafe = _tipo_cafe
         self.cantidad_agua = _cantidad_agua
         self.cantidad_cafe = _cantidad_cafe

class Cafe:
    coffee_types = {
        'coffee_type': 'arabic',
        'coffee_type1': 'roasted',
        'coffee_type2': 'decaf'
    }
    def __init__ (self):
        self.coffee_type = self.coffee_types["arabic"]

class Leche:
     def __init__ (self):
          self.type_milk = {
     'lactose_free': 'lactose_free',
     'type_milk_2': 'complete',
     'type_milk_3': 'whole_milk'
}
    