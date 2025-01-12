class ModelMotion:
    def __init__(self, dados):
        self.posicao_x           = dados[0]
        self.posicao_y           = dados[1]
        self.posicao_z           = dados[2]
        self.velocidade_x        = dados[3]
        self.velocidade_y        = dados[4]
        self.velocidade_z        = dados[5]
        self.frente_x            = dados[6]
        self.frente_y            = dados[7]
        self.frente_z            = dados[8]
        self.lateral_x           = dados[9]
        self.lateral_y           = dados[10]
        self.lateral_z           = dados[11]
        self.forcag_lateral      = dados[12]
        self.forcag_longitudinal = dados[13]
        self.forcag_vertical     = dados[14]
        self.yaw                 = dados[15]
        self.pitch               = dados[16]
        self.roll                = dados[17]