class Asignatura:
    def __init__(self, codigo, nombre, creditos):
        self._codigo = codigo
        self._nombre = nombre
        self._creditos = creditos

    def mostrar_info(self):
        return "Asignatura: {} ({}) - Créditos: {}".format(self.get_nombre, self.get_codigo, self.get_creditos)

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_creditos(self):
        return self._creditos