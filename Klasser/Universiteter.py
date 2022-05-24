class Universiteter:
    """klasse for de Universiteter som systemet skal samarbejde med"""
    def __init__(self, KU, DTU):
        self.KU = KU
        self.DTU = DTU

        #Getters og sætters

    def get_KU(self): return self.KU
    def set_KU(self, new_KU): self.KU = new_KU

    def __str__(self):
        Universities = f"{self.KU}, {self.DTU}"
        return f"Universities: {Universities}"
    