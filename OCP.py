""" 
OCP - OPEN/CLOSED PRINCIPLE 
Permitir agregar funcionalidades nuevas, sin tener que modificar el codigo anterior de la clase
Open para extender 
Closed para modificar
 """
class Notificador:
    def __init__(self, usuario, mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje

    # NotImplementedError Obligo a las clases hijas a implementar este metodo sin necesidad de usar clases abstractas
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Whatsapp a {self.usuario.whatsapp}")

class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Twitter a {self.usuario.twitter}")