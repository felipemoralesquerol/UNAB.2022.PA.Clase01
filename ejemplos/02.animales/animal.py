# Pilares del POO

class Animal:

    # Edad es un argumento opcional
    def __init__(self, nombre, edad = -1):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print('Soy ' + self.nombre + ' y digo .....')

class Perro(Animal):
    texto_hablar = 'Guau!'

    def hablar(self):
        print('Soy ' + super.nombre + ' y digo ' + self.texto_hablar)   

class Gato(Animal):
    def hablar(self):
        print('Soy ' + self.nombre + ' y digo Miau!')

class Raton(Animal):
    pass


for animal in Perro('Spike'), Gato('Tom'), Raton('Jerry', 3): 
    animal.hablar()

#print(Perro().texto_hablar)    