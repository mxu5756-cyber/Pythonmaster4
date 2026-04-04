class Student :
    #propriete ou attribut: variable pour defenir
    name=None
    age=None
    #comprtement : méthode
    #self est utilisé pour designé l'objet de la classe lui mm
    def say_hi(self):
        print(f"Bonjour A tous , Je appelle {self.name} et jai {self.age} ans")
    #self est transparant lorsque l'argument est passé et peu etre ignoré
    def say_hi2(self,msg):
        print(f"Bonjour a tous , {msg}")
#objet = nom de la classe
stu1= Student()
stu1.name="Alex"
stu1.age=18
stu1.say_hi()

stu2=Student()
stu2.name="Lucie"
stu2.age=16
stu2.say_hi()
stu2.say_hi2("enchante")