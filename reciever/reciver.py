import struct

class Reciver:
    
    def set_pacote(self, pacote):
        self.HEADER_FORMAT = '<HBBBBBQfIIBB'
        self.HEADER_FORMAT_TAMANHO = struct.calcsize(self.HEADER_FORMAT)
        self.pacote = pacote
    