class Phone :
    producer = "HUAWAI"

    def call_by_5g(self):
        print("Father 5g call")
class MyPhone(Phone):
    #override
    producer = "APPLE"
    def call_by_5g(self):
        print("Child 5g calls ")

my_phone = MyPhone
print(my_phone.producer )
my_phone.call_by_5g()