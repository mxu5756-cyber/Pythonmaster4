class Phone:
    serial_number=None
    producer="huwai"

    def call_by_Sg(self):
        print("5g calls")

class NFCReader:
    nfc_type="Fifth generation"
    producer="HM"
    def read_card(self):
        print("Write NFC cards")
    def write_card(self):
        print("Write NFC cards")
class RemoteControl:
    rc_type="IR remote cpntrol"
    def control(self):
        print("inferead remote control opening")
#Les classes peres multiples dont les memebres portent le meme nom sont prioritaire
#par defaut dans l'ordre de l'hritage (de gauche de droit)
class Myphone(Phone, NFCReader,RemoteControl):
    pass

my_phone=Myphone()
my_phone.call_by_Sg()
my_phone.control()
print(my_phone.producer)