class Carta:
    def __init__(self, numero, naipe):
        # número (int - de 1 até 13)
        self.numero = numero
        # naipe (char- {c, o, p, e} representando Copas, Ouros, Paus, Espadas)
        self.naipe = naipe
        # status (boolean - será usado na lista ligada)
        # False pode significar "virada para baixo" e True "virada para cima"
        self.status = False 

    def __str__(self):
        """Formata a carta para aparecer bonitinha no terminal (ex: 2C, 13P)"""
        return f"{self.numero}{self.naipe.upper()}"
        
    def __repr__(self):
        return self.__str__()