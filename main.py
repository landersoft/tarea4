from clases.estudiante import Estudiante
import datetime

if __name__=="__main__":
    estudiante1 = Estudiante(rut="123", nombre="Rodrigo Lander", email="landersoft@gmail.com", matricula="20260101",fecha_nacimiento=datetime.datetime.strptime("2000-01-05","%Y-%m-%d"),beca=10)
    print(estudiante1.mostrar_info())



