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
        """Formata a carta para aparecer bonitinha no terminal (ex: 2C, 13P) com cores."""
        # Códigos ANSI para colorir o texto no terminal
        VERMELHO = '\033[91m'
        RESET = '\033[0m'
        
        texto_carta = f"{self.numero}{self.naipe.upper()}"
        
        # Se for Copas ('c') ou Ouros ('o'), pinta de vermelho. Se não, deixa a cor padrão.
        if self.naipe in ['c', 'o']:
            return f"{VERMELHO}{texto_carta}{RESET}"
        return texto_carta
        
    def __repr__(self):
        return self.__str__()