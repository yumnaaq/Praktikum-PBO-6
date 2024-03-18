from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, merek, model):
        self.merek = merek
        self.model = model
    
    @abstractmethod
    def berkendara(self):
        pass
    
    @abstractmethod
    def berhenti(self):
        pass

class Mobil(Kendaraan):
    def __init__(self, merek, model, jenis_bahan_bakar):
        super().__init__(merek, model)
        self.jenis_bahan_bakar = jenis_bahan_bakar
    
    def berkendara(self):
        print(f"{self.merek} {self.model} sedang berkendara.")
    
    def berhenti(self):
        print(f"{self.merek} {self.model} telah berhenti.")

class Sepeda(Kendaraan):
    def __init__(self, merek, model):
        super().__init__(merek, model)
    
    def berkendara(self):
        print(f"{self.merek} {self.model} sedang mengayuh sepeda.")
    
    def berhenti(self):
        print(f"{self.merek} {self.model} telah berhenti.")

def main():
    mobil = Mobil("Toyota", "Corolla", "Bensin")
    mobil.berkendara()
    mobil.berhenti()

    sepeda = Sepeda("Polygon", "Xtrada")
    sepeda.berkendara()
    sepeda.berhenti()

if __name__ == "__main__":
    main()
