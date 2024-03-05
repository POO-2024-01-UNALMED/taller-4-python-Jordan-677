from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        if estudiantes==None:
            estudiantes = []
        if asignaturas==None:
            asignaturas = []
        self._asignaturas = asignaturas    
        self._grupo = grupo
        
        self.listaAlumnos = estudiantes

    def listaAsignaturas(self,**kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))     




    def agregarAlumno(self, alumno, lista=None):
        if lista==None:
            lista = []
        lista.append(alumno)
        self.listaAlumnos = self.listaAlumnos + lista


    def __str__(self):
        return "Grupo de estudiantes: "+self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
        
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
