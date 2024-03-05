class Asignatura:
    
    def __init__(self, n, salon="remoto"):
        self._nombre = n
        self._salon = salon
        
    def __str__(self):
        return self._nombre+" "+self._salon
    