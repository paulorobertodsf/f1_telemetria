import struct
from model import motion
from reciever import reciver

class RecieverMotion(reciver.Reciver):
    def __init__(self):
        super().__init__()
        self.FORMAT = '<ffffffhhhhhhffffff'
        self.FORMAT_TAMANHO = struct.calcsize(self.FORMAT)

    def get_dados(self):
        motion_lista = list()
        inicio = self.HEADER_FORMAT_TAMANHO

        for i in range(22): # 22 carros no grid

            posicao_carro = self.pacote[inicio : inicio + self.FORMAT_TAMANHO]
            posicao_carro_decodificado = struct.unpack(self.FORMAT, posicao_carro)
            
            model_motion = motion.ModelMotion(posicao_carro_decodificado)

            motion_lista.append(posicao_carro_decodificado)
            inicio += self.FORMAT_TAMANHO
       
        return motion_lista
