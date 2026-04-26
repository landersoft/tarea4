<p style="color: red;">Sistema Académico Orientado a Objetos</p>

Descripción general

Este proyecto corresponde al desarrollo de un sistema académico básico implementado utilizando Programación Orientada a Objetos (POO).

El sistema permite gestionar información de:

- Estudiantes
- Docentes
- Asignaturas
- Cursos

Incorpora funcionalidades como:

- Inscripción de estudiantes en cursos
- Asignación de docentes
- Registro de calificaciones
- Evaluación de aprobación o reprobación
- Cálculo de pagos considerando becas


---

Tecnologías utilizadas

- Lenguaje: **Python 3**
- Herramienta de modelado: **PlantUML**

---

Estructura del proyecto

```
/TAREA4
│
├── main.py
├── modelos/
│   ├── persona.py
│   ├── estudiante.py
│   ├── docente.py
│   ├── curso.py
│   └── asignatura.py
│
├── uml/
│   └── tarea4.puml
│   └── tarea4.png
│
└── README.md
```

---

Instrucciones de ejecución

1) Clonar el repositorio:

```
git clone https://github.com/landersoft/tarea4.git
```

2) Entrar al directorio:

```
cd tarea4
```

3) Ejecutar el programa:

```
python main.py
```

---

Diagrama UML

El sistema fue diseñado utilizando un diagrama de clases UML desarrollado en PlantUML.

Archivo:

```
/uml/tarea4.puml
/uml/tarea4.png
```

(Relación principal: herencia entre Persona → Estudiante y Docente, y asociación con Curso)


Funcionalidades principales

- Inscribir estudiante en curso
- Asignar docente a curso
- Registrar calificaciones
- Evaluar aprobación (Aprobado/Reprobado)
- Calcular mensualidad con beca