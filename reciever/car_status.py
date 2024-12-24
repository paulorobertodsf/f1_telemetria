import struct
from model import car_status
from reciever import reciver

class RecieverCarStatus(reciver.Reciver):
    def __init__(self):
        super().__init__()
        self.FORMAT = '<BBBBBfffHHBBHBBBbfffBfffB'
        self.FORMAT_TAMANHO = struct.calcsize(self.FORMAT)

    def get_dados(self):
        status_carro_lista = list()
        inicio = self.HEADER_FORMAT_TAMANHO

        for i in range(22): # 22 carros no grid
            status_carro = self.pacote[inicio : inicio + self.FORMAT_TAMANHO]
            status_carro_decodificado = struct.unpack(self.FORMAT, status_carro)
            
            model_status_carro = car_status.ModelMotion(status_carro_decodificado)

            status_carro_lista.append(status_carro_decodificado)
            inicio += self.FORMAT_TAMANHO
       
        return status_carro_lista[0]