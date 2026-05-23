class Animal:
    def speak(self):
        pass
class Dog(Animal):
        def speak(self):
            print("woof wooof woof")
class Cat(Animal):
    def speak(self):
        print("Miao Miao Miao")
def make_noise (animal:Animal):
    animal.speak()
dog=Dog()
cat=Cat()

make_noise(dog)
make_noise(cat)
#Polymorphise états multiples lors de l'execution dans certian comportement
#different objets sont utilisé pour obtenir des differents états

#meme comportement , introduction d'objet différent obtention d'etat dfférent
#classe abstraits une clase contenant des méthodes abstraites  est appelé classes absaitres
#méthode abstraites :une méthode dans le corps est une implémentation vide(pass) est appelé méthode absaitre