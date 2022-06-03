from balok import Balok

class BalokController:
    
    def hitung_panjang(self, balok: Balok)-> float:
        return balok.get_panjang() * balok.get_panjang()
    
    def hitung_lebar(self, balok: Balok)-> float:
        return balok.get_lebar() * balok.get_lebar()
    
    def hitung_tinggi(self, balok: Balok)-> float:
        return balok.get_tinggi() * balok.get_tinggi()
    
    def hitung_volume(self, balok: Balok)-> float:
        return balok.get_panjang() * balok.get_lebar()+balok.get_tinggi()
    
    def hitung_luas(self, balok: Balok)-> float:
        return 2 * (balok.get_panjang()+balok.get_lebar()+balok.get_tinggi())
    
    def hitung_keliling(self, balok: Balok)-> float:
        return 4 * (balok.get_panjang()+balok.get_lebar()+balok.get_tinggi())