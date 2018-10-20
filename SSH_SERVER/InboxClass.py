#Atributos y funcion que llama a la BD para rellenarlo
class MatchesClass:
    nick = "Paola"
    fullName = "Paola"
    correo = "paola@est.fib.upc"

def __init__(self):
    self.data = []

def __init__(self,nick,fullname,correo):
    self.nick = nick
    self.fullName = fullname
    self.correo = correo