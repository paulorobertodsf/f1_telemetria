import struct
from model import telemetry
from reciever import reciver

class RecieverTelemtry(reciver.Reciver):
    def __init__(self):
        super().__init__()
        self.FORMAT = '<HfffBbHBBHHHHHBBBBBBBBHffffBBBB'
        # tem o resto que é 'BBb', mas acho q nunca vo precisar
        self.FORMAT_TAMANHO = struct.calcsize(self.FORMAT)

    def get_dados(self):
        telemtria_lista = list()
        inicio = self.HEADER_FORMAT_TAMANHO

        for i in range(22):
            telemtria = self.pacote[inicio : inicio + self.FORMAT_TAMANHO]
            telemtria_decodificado = struct.unpack(self.FORMAT, telemtria)

            telemtria_lista.append(telemtria_decodificado)
            inicio += self.FORMAT_TAMANHO
        

        return telemtria_lista