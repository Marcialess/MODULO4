# Crear la superclase Persona
# crear la subclase Maestro que herede de la superclase Persona.
# Crear la subclase Estudiante que herede de la subclase Persona
# Crear la subclase Universitario que herede de la subclase estudiante

class Persona:
    def __init__(self, _name, _rut, _age, _sexo):
        self.name = _name
        self.rut = _rut
        self.age = _age
        self.sexo = _sexo


class Maestro (Persona):
    def __init__(self, _name, _rut, _age, _sexo, _materias):
        super().__init__(_name, _rut, _age, _sexo)
        self.materias = _materias
        


class Estudiante (Persona):
    def __init__(self, _name, _rut, _age,_sexo, _asignatura, _nivel):
        super().__init__(_name, _rut, _age,_sexo)
        self.asignatura = _asignatura
        self.nivel = _nivel

    def Estudiar(self):
        print(f"{self.name} esta estudiando en el discord")    


class Universitario(Estudiante):
    def __init__(self, _name, _rut, _age,_sexo, _asignatura, _nivel, _university, _course_year):
        super().__init__(_name, _rut, _age,_sexo, _asignatura, _nivel)
        self.universidad = _university
        self.course_year = _course_year


Quiti = Estudiante("Maria Fernanda",13483,30,"F","Artes",2)
print(Quiti.name,Quiti.age)
Marcial = Universitario("Marcialess",234242,17,"M","PEYTON",2,"EDUTECNO",2023)
Marcial.Estudiar()
