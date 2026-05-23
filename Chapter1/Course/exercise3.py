class Phone:
    __is_5g_enable = None

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g activée")
        else:
            print("5g off, utilisation du réseau 4g")
    def call_by_5g(self):
        self.__check_5g()
        print("Appel en cours")
phone = Phone()
phone._Phone__is_5g_enable = True
phone.call_by_5g()