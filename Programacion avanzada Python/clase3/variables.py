class Alumno:
    # variable de clase
    semestre = 1
    asignaturas = ["Python", "Javascript", "Base de Datos"]

    def init(self, _name):
        # variable de instancia
        self.name = _name
        self.asignatura = ""

    def inscribir_asignatura(self, _asignatura):
        self.asignatura = _asignatura

# crear un metodo que permita registrar tres notas, una a una,
# crear un metodo que obtenga el promedio de notas
    def registrar_notas(self, _nota):
        self.nota = _nota

    def obtener_promedio(self):
        pass

alumno1 = Alumno("María")
alumno2 = Alumno("Sol")
alumno3 = Alumno("Marcial")

print(f'alumno1: {alumno1.name}, semestre: {alumno1.semestre}')
alumno1.semestre = 6
print(f'alumno1: {alumno1.name}, semestre {alumno1.semestre}')
print(f'alumno2: {alumno2.name}, semestre {alumno2.semestre}')

alumno1.asignatura = "Python"
print(f'alumno1: {alumno1.name}, semestre {alumno1.semestre} en {alumno1.asignatura}')