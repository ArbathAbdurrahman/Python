from abc import ABC, abstractmethod

class IBergerak(ABC):
    @abstractmethod
    def bergerak(self):
        pass

class Mobil(IBergerak):
    def bergerak(self):
        print("Mobil bergerak menggunakan roda")
