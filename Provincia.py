class Provincia:
    nombre: str
    superficie: float

    def __init__(self, nombre: str, superficie: float) -> None:
        self.nombre = nombre
        self.superficie = superficie
    

    def __gt__(self, otro):
        if not isinstance(otro, Provincia):
            raise Exception("No se puede comparar una provincia con un dato del tipo {0}".format(type(otro)))
        return self.superficie > otro.superficie
    
    def __lt__(self, otro):
        if not isinstance(otro, Provincia):
            raise Exception("No se puede comparar una provincia con un dato del tipo {0}".format(type(otro)))
        return self.superficie < otro.superficie

    def __eq__(self, otro):
        if not isinstance(otro, Provincia):
            raise Exception("No se puede comparar una provincia con un dato del tipo {0}".format(type(otro)))
        return self.superficie == otro.superficie