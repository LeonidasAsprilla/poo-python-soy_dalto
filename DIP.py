""" 
DIP - DEPENDENCY INVERSION PRINCIPLE
Los modulos de alto nivel no tienen depender de los modulos de bajo nivel, si no que los dos tienen que depender de las abstracciones. 
Las abstracciones no tienen que depender de los detalles, sino lo contrario.
 """
""" class Diccionario: 
    def verificar_palabra(self, palabara): 
        # Lógica para verificar polabras
        pass

# El CorrectorOrtografico(alto nivel) depende de Diccionario(bajo nivel), violando el DIP
class CorrectorOrotografico:
    def __init__(self) -> None:
        self.diccionario = Diccionario()

    # si diccionario cambia, corregir_texto tambien, violando el DIP
    def corregir_texto(self, texto):
        # Usamos el diccionario para corregir el texto
        pass """

# para solucionar... 

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self):
        # Lógica para verficar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabras):
        # Lógica para verificar palabras si está en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self):
        # Lógico para verificar palabras desde el servicio web
        pass

# el corrector ahora depende de la abstraccion del verificador, no del diccionario
class CorrectorOrotografico:
    def __init__(self, verficador):
        self.verificador = verficador

    def corregir_texto(self, texto): 
        # usamos el verificador para corregir texto
        pass