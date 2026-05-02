class Student :
    name=None
    age=None
    tel=None
    #methode de constrcution
    #Elle est automatiquement transmis lors de la creation de l'objet class
    #les arguments entrants sont automatiquemment tansmis a la methode
    #init pour etre utilise lors d'un objet de class
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("la classe Etudiant crée un obligé")
stu=Student("Alex",18,"110")
print(stu.name)
stu2=Student("Luna",20,"120")
print(stu2.name)