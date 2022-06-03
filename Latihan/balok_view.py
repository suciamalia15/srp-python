from balok import Balok
from balok_controller import BalokController


class BalokView:
    
    def show_luas(self, balok: Balok, balok_controller:BalokController):
        print (balok_controller.hitung_luas(balok))
        
    def show_volumes(self, balok: Balok, balok_controller:BalokController):
        print (balok_controller.hitung_volumes(balok))
        
    def show_keliling(self, balok: Balok, balok_controller:BalokController):
        print (balok_controller.hitung_keliling(balok))