from abc import ABC, abstractmethod

#Abstract Products, è un'interfaccia che definisce il comportamento dei prodotti concreti 
#Viene definita un'interfaccia per ogni tipo di prodotto (Pieno, Vuoto, Base) che le classi concrete dovranno implementare.
class Pieno(ABC):
    @abstractmethod
    def simbolo(self) -> str: ...
class Vuoto(ABC):
    @abstractmethod
    def simbolo(self) -> str: ...
class Base(ABC):
    @abstractmethod
    def simbolo(self) -> str: ...

#Concrete Products
class AsteriscoPieno(Pieno):
    def simbolo(self): return "*"
class SpazioVuoto(Vuoto):
    def simbolo(self): return " "
class TrattoBase(Base):
    def simbolo(self): return "|"

class CancellettoPieno(Pieno): 
    def simbolo(self): return "#"
class PuntoVuoto(Vuoto):
    def simbolo(self): return "."
class UgualeBase(Base): 
    def simbolo(self): return "╠"

class RectanglePieno(Pieno): 
    def simbolo(self): return "█"
class RectangleVuoto(Vuoto): 
    def simbolo(self): return "×"
class RectangleBase(Base):
    def simbolo(self): return "¦"

#Abstract Factory: 
class StileFactory(ABC):
    @abstractmethod
    def crea_pieno(self) -> Pieno: ...
    @abstractmethod
    def crea_vuoto(self) -> Vuoto: ...
    @abstractmethod
    def crea_base(self) -> Base: ...

#Concrete Factory
class AstecriscoFactory(StileFactory):
    def crea_pieno(self):
        return AsteriscoPieno()
    def crea_vuoto(self):
        return SpazioVuoto()
    def crea_base(self):
        return TrattoBase()

class CancellettoFactory(StileFactory):
    def crea_pieno(self):
        return CancellettoPieno()
    def crea_vuoto(self):
        return PuntoVuoto()
    def crea_base(self):
        return UgualeBase()

class RectangleFactory(StileFactory):
    def crea_pieno(self):
        return RectanglePieno()
    def crea_vuoto(self):
        return RectangleVuoto()
    def crea_base(self):
        return RectangleBase()

class IstogrammaOrizzontale:
    def __init__(self, factory: StileFactory):
        self.pieno = factory.crea_pieno()
        self.base = factory.crea_base()
        self.vuoto = factory.crea_vuoto()
    def stampa(self, listaNum):
        maxVal = max(listaNum)
        if maxVal > 50:
            self.tripleStampa(listaNum)
        else:
            self.singleStampa(listaNum)
    
    def singleStampa(self, listaNum):
        maxVal = max(listaNum)
        for i in listaNum:
            print(f"{self.base.simbolo()} {self.pieno.simbolo()*i}{self.vuoto.simbolo()*(maxVal-i)} {i}")
            if i != listaNum[-1]:
                print(f"{self.base.simbolo()}")

    def tripleStampa(self, listaNum):
        maxVal = max(listaNum)
        for i in listaNum:
            print(f"{self.base.simbolo()} {self.pieno.simbolo()*i}{self.vuoto.simbolo()*(maxVal-i)}")
            print(f"{self.base.simbolo()} {self.pieno.simbolo()*i}{self.vuoto.simbolo()*(maxVal-i)} {i}")
            print(f"{self.base.simbolo()} {self.pieno.simbolo()*i}{self.vuoto.simbolo()*(maxVal-i)}")
            if i != listaNum[-1]:
                print(f"{self.base.simbolo()}")

dati = [13, 52, 2, 5, 4]

print("Istogramma con Asterisco Factory")
factory = AstecriscoFactory()      # cambi solo questa riga
IstogrammaOrizzontale(factory).stampa(dati)
print("\n")
print("Istogramma con Cancelletto Factory")
factory2 = CancellettoFactory()      # cambi solo questa riga
IstogrammaOrizzontale(factory2).stampa(dati)
print("\n")
print("Istogramma con Rectangle Factory")
factory3 = RectangleFactory()      # cambi solo questa riga
IstogrammaOrizzontale(factory3).stampa(dati)