# Superclase de docente, y estudiante
class Persona:
    def __init__(self, rut, nombre,apellido_paterno, email):
        self._rut = rut
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._email = email

    def get_nombre(self):
        return self._nombre +" "+self._apellido_paterno

    def get_email(self):
        return self._email

    def mostrar_info(self):
        return "Nombre: {} - Email: {}".format(self.get_nombre(), self.get_email())
