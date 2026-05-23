class Phone:
    serial_number= None
    producer="Huawai"

    def call_by_5G(self):
        print("5g calls")
class Myphone(Phone):
    producer="Apple"

    def call_by_5G(self):
        #La premiere facon d'appeler un membre de la classe pere
        print(f"La marque de la classe est {self.producer}")
        print(f"La marque de la classe pere est {Phone.producer} ")
        Phone.call_by_5G(self)

        print("________________________")
        print(f"La marque de la classe pere est {super().producer}")
        super().call_by_5G()
my_phone=Myphone()
my_phone.call_by_5G()

# Override redéfinit une variable ou un eméthode memebre d'une classe pere 