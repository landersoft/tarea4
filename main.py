from clases.estudiante import Estudiante
from clases.docente import Docente
from clases.asignatura import Asignatura
from clases.curso import Curso
import datetime

if __name__=="__main__":
    estudiante1 = Estudiante(rut="123", nombre="Rodrigo",apellido_paterno="Lander", email="landersoft@gmail.com", matricula="20260101",fecha_nacimiento=datetime.datetime.strptime("2000-01-05","%Y-%m-%d"),beca=10)
    print(estudiante1.mostrar_info())
    docente1 = Docente(rut="1234", nombre="Alvaro", apellido_paterno= "Pérez", email="aperez@ucsc.cl", especialidad="Matemáticas")
    print(docente1.mostrar_info())

    asignatura1 = Asignatura("MAT101", "Álgebra", 5)
    print(asignatura1.mostrar_info())
    curso1 = Curso(1, asignatura1, "Lunes 10:00")


    docente1.asignar_curso(curso1) #Asignar objeto curso a docente1
    estudiante1.inscribir_curso(curso1)
    curso1.registrar_nota(estudiante1, 5.5)

    print("Mensualidad :", estudiante1.calcular_pago())
    print("Estado:", curso1.evaluar_estudiante(estudiante1))
