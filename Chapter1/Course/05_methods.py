class student:
    name=None
    age=None

    def __init__(self,name,age):
        self.name=name
        self.age=age
# Les adresses ne sont pas très utiles ,et nous pouvons
#controler le comportement des conversions de classes en chaines
#de caracteres en utilisant la méthode str
    def __str__(self):
        return f"name={self.name},age={self.age}"
    #affchage
    def __lt__(self,other):
        return self.age < other.age
    #comparaison--> less than
    def __le__(self,other):
        return self.age <= other.age
    #less than or equal
    def __eq__(self,other ):
        return self.age == other.age
student1= student("Alex",18)
student2= student("luna ",20)
student3= student("Léon",20)
print(student1 > student2)
print(student2 <= student3)
print(student2 == student3)
