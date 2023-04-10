# import rasterizacao
# import numpy as np
# import matplotlib.pyplot as plt

from rasterizacao import Ponto, rasterizacao_de_retas


# ponto = rasterizacao
# Resoluções

altura, largura = 100, 100
resolucao1 = altura, largura
resolucao2 = altura*3, largura*3
resolucao3 = altura*6, largura*6
resolucao4 = altura*8, largura*6
resolucao5 = int(altura*19.2), int(largura*10.8)

# EXEMPLO DE RETAS
reta1_ponto1 = (-0.5, -0.8)
reta1_ponto2 = (-0.5, 0, 8)

reta2_ponto1 = (0, 5, 0, 5)
reta2_ponto2 = (0, 5, 0, 5)

reta3_ponto1 = ()
reta3_ponto2 = ()

reta4_ponto1 = ()
reta4_ponto2 = ()


# EXEMPLO PONTOS DO TRIANGULO
tri_ponto1 = (-0.5, -0.87)
tri_ponto2 = (0.5, -0.87)
tri_ponto3 = (0, 0.73)

tri2_ponto1 = (-1, 0)
tri2_ponto2 = (0, 0.73)
tri2_ponto3 = (1, 0)

# EXEMPLO PONTOS DO QUADRADO
quadrado_ponto1 = (-0.9, -0.9)
quadrado_ponto2 = (-0.9, 0.9)
quadrado_ponto3 = (0.9, 0.9)
quadrado_ponto4 = (0.9, -0.9)

quadrado2_ponto1 = (-0.5, -0.5)
quadrado2_ponto2 = (-0.5, 0.5)
quadrado2_ponto3 = (0.5, 0.5)
quadrado2_ponto4 = (0.5, -0.5)
# segunda aresta
# terceira aresta


# HEXAGONO 1

hex_ponto1 = (-0.5, -0.87)
hex_ponto2 = (-1, 0)
hex_ponto3 = (-0.5, 0.87)
hex_ponto4 = (0.5, 0.87)
hex_ponto5 = (1, 0)
hex_ponto6 = (0.5, -0.87)


def triangulo(tri_ponto1, tri_ponto2, tri_ponto3, resolucao):
    pontos = []
    tri_ponto1 = Ponto(tri_ponto1[0], tri_ponto1[1], resolucao)
    tri_ponto2 = Ponto(tri_ponto2[0], tri_ponto2[1], resolucao)
    tri_ponto3 = Ponto(tri_ponto3[0], tri_ponto3[1], resolucao)
    pontos.append(rasterizacao_de_retas(tri_ponto1, tri_ponto2))
    pontos.append(rasterizacao_de_retas(tri_ponto2, tri_ponto3))
    pontos.append(rasterizacao_de_retas(tri_ponto3, tri_ponto1))
    return pontos
