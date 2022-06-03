class Persegi: 
    
    def __init__(self, sisi: float):
        self.__sisi = sisi
    
    def set_sisi(self, sisi: float)-> None:
        self.__sisi = sisi
        
    def getsisi(self)-> float:
        return self.__sisi