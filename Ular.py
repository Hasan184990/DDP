from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
        
    def cetak_ular(self):
        super().cetak()
        print("\nDesign  : ", self.design,
              "\nRacun   : ", self.racun)
        

anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur",
                "Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()            