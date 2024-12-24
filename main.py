import socket
from reciever.motion import RecieverMotion
from reciever.car_status import RecieverCarStatus
from reciever.telemetry import RecieverTelemtry
import sys

IP = "0.0.0.0"
PORTA = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORTA))

reciever_motion = RecieverMotion()
reciever_car_status = RecieverCarStatus()
reciever_telemetry = RecieverTelemtry()

print(f"Receptor escutando no endereço {IP}:{PORTA}...")
try:
    while True:
        dados, endereco = sock.recvfrom(2048)
        if len(dados) == 1349:
            reciever_motion.set_pacote(dados)
            carro = reciever_motion.get_dados()[0]
            #print(carro)

        if len(dados) == 1239:
            reciever_car_status.set_pacote(dados)
            carro = reciever_car_status.get_dados()
            #print(carro)
        
        if len(dados) == 1352:
            reciever_telemetry.set_pacote(dados)
            telemetria = reciever_telemetry.get_dados()
            for i, c in enumerate(telemetria):
        # Move o cursor para a linha correspondente
                sys.stdout.write(f"\033[{i+1}H")  # Muda para a linha i+1 do terminal
                # Atualiza as informações do carro
                sys.stdout.write(f"Carro {i+1}: {c}       \n")
            sys.stdout.flush()
        
except KeyboardInterrupt:
    print("\nReceptor finalizado.")
finally:
    sock.close()