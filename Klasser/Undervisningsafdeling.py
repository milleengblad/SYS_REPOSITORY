class Unervisningsafdeling:
    """Klasse for undervisningsafdelingerne"""
    def __init__(self, SUND, SCIENCE, DTU_Sundhedsteknologi, DTU_EngineeringTechnology):
        self.SUND = SUND
        self.SCIENCE = SCIENCE
        self.DTU_Sundhedsteknologi = DTU_Sundhedsteknologi
        self.DTU_EngineeringTechnology = DTU_EngineeringTechnology

        #getters og setters

    def get_SUND(self): return self.SUND
    def set_SUND(self, new_SUND): self.SUND = new_SUND

    def get_SCIENCE(self): return self.SCIENCE
    def set_SCIENCE(self, new_SCIENCE): self.SCIENCE = new_SCIENCE

    def get_DTU_Sundhedsteknologi(self): return self.DTU_Sundhedsteknologi
    def set_DTU_Sundhedsteknologi(self, new_DTU_Sundhedsteknologi): self.DTU_Sundhedsteknologi = new_DTU_Sundhedsteknologi

    def get_DTU_EngineeringTechnology(self): return self.DTU_EngineeringTechnology
    def set_DTU_EngineeringTechnology(self, new_DTU_EngineeringTechnology): self.DTU_EngineeringTechnology = new_DTU_EngineeringTechnology

    def __str__(self):
        Undervisningsafdelinger = f"{self.SUND}, {self.SCIENCE}, {self.DTU_EngineeringTechnology}, {self.get_DTU_Sundhedsteknologi()}"
        return f"Undervisningsafdelinger: {Undervisningsafdelinger}"