from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super().cetak()
        print("\nJenis  : ", self.jenis,
              "\nBunyi   : ", self.bunyi)
        

gereja = Burung("Gereja", "jagung", "sawah", "Bertelur",
                "Batik Solo", "kukuruyuk")
gereja.cetak_burung()
