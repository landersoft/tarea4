from clases.persona import Persona
# Clase estudiante hereda de Persona
class Estudiante(Persona):
    def __init__(self, rut, nombre,apellido_paterno, email, matricula,fecha_nacimiento,beca=0):
        super().__init__(rut, nombre,apellido_paterno, email)
        self._matricula = matricula
        self._beca = beca  # Expresado en %
        self._cursos = []
        self._fecha_nacimiento = fecha_nacimiento #tipo datetime


    def inscribir_curso(self, curso):
        self._cursos.append(curso)
        curso.agregar_estudiante(self)

    def calcular_pago(self):
        costo_base = 1000
        descuento = costo_base * (self._beca / 100)
        return costo_base - descuento

    def get_matricula(self):
        return self._matricula

    # Polimorfismo
    def mostrar_info(self):
        return "Estudiante: {} | Matricula: {}".format(self.get_nombre(), self.get_matricula())