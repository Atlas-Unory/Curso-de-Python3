velocidade = 60 #velociade atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade maxima do radar
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #distancia onde o radar pega um carro

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_no_radar_1 = velocidade <= RADAR_1 or velocidade >= RADAR_1

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou o radar 1')

if carro_passou_no_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1 and velocidade_carro_passou_radar_1:
    print('carro multado radar 1')