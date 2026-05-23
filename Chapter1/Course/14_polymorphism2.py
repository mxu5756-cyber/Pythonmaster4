class AC:
    def coll_wind(self):
        """refrigération"""
        pass
    def hot_wind(self):
        """Cahleur"""
        pass

    def swing_l_r(self):
        """Le vent souffle a droite et a gauche"""

class Midea_AC(AC):
    def cool_wind(self):
        print("La climatisation et refroidissement par Midee")

    def hot_wind(self):
        print("Chauffage par Midea")
    def swingl_r(self):
        print("Les climatisatuers Midea se balencent de gauche a droite")


class GREE_AC(AC):
    def cool_wind(self):
        print("climatisation et refroidissement par GREE")
    def hot_wind(self):
        print("Chauffage par GREE")
    def swing_l_r(self):
        print("Les climatisateur par GREE se balancent de gauche a droite ")
def make_cool(ac:AC):
    ac.cool_wind()
midea_ac=Midea_AC()
gree_ac=GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)