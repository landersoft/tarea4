class Curso:
    def __init__(self, id, asignatura, horario):
        self._id = id
        self._asignatura = asignatura
        self._horario = horario
        self._estudiantes = []
        self._docente = None
        self._notas = {}

    def agregar_estudiante(self, estudiante):
        self._estudiantes.append(estudiante)

    def registrar_nota(self, estudiante, nota):
        self._notas[estudiante.get_matricula()] = nota

    def evaluar_estudiante(self, estudiante):
        nota = self._notas.get(estudiante.get_matricula(), 0)
        if nota >= 4.0:
            return "Aprobado"
        return "Reprobado"