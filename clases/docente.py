from clases.persona import Persona


class Docente(Persona):
    def __init__(self, rut, nombre, email, especialidad):
        super().__init__(rut, nombre, email)
        self._especialidad = especialidad

    def asignar_curso(self, curso):
        curso.docente = self

    def get_especialidad(self):
        return self._especialidad

    # Polimorfismo
    def mostrar_info(self):
        return "Docente: {} | Especialidad: {}".format(self.get_nombre(), self.get_especialidad())