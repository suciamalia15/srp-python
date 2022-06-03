class Balok:    
    
    def __init__(self, panjang, lebar, tinggi : float):
        self.__panjang = panjang
        self.__lebar = lebar
        self.__tinggi = tinggi

    def set_panjang (self, panjang: float) -> None:
        self.__panjang = panjang

    def set_lebar (self, lebar: float) -> None:
        self.__lebar = lebar

    def set_tinggi (self, tinggi: float) -> None:
        self.__tinggi = tinggi

    def get_panjang (self) -> float:
        return self.__panjang

    def get_lebar (self) -> float:
        return self.__lebar

    def get_tinggi (self) -> float:
        return self.__tinggi