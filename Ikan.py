from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, berkumis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.berkumis = berkumis
        
    def cetak_Ikan(self):
        super().cetak()
        print("\nJenis \t : ", self.jenis,
              "\nBerkumis : ", self.berkumis)
        

Lele = Ikan("Lele", "makan kotoran", "di air", "Bertelur",
                "hitam abu abu", "sungut peraba")
Lele.cetak_Ikan()