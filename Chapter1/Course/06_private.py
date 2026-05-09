class Phone:
    #Variales membre publiques
    serial_number= None
    producer= None
    #Variable mesures privé
    __current_voltage=None
    def call_by_5g(self):
        #Les méthodes privés ne peuvent pas etre utilisé directement par les objets de la classe
        #mais peuvent etre utilisé par les méthodes publique de la classe (d'autre membre)
        if self.__current_voltage >=1:
            self.__Keep_single_core()
        print("Les appels 5g désormais possible")

    def __Keep_single_core(self):
        print("faire fonctionner l'unité centrale en mode mono_coeur pour éconmiser de l'énergie")
phone=Phone()
phone.serial_number="123"
#Les méthodes privés ne peuvent pas etre utilisé directemnt par les objets de la classe
phone.__Keep_single_core()
