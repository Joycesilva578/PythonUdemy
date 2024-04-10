velocidade = 60
local_carro = 99


radar_1 = 60
local_1 = 100
radar_range = 1

if velocidade > radar_1:
    print('velocidade carro passou do radar 1')

if local_carro >= (local_1 - radar_range) and local_carro <= (local_1 + radar_range) and \
    velocidade > radar_1:
    print('carro multado em radar 1')