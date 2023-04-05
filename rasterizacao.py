import math
import matplotlib.pyplot as plt
import numpy as np

altura, largura = 100, 100


class Ponto:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = self.scale_point(x, y, largura, altura)

    def scale_point(self, x, y, largura, altura):
        # Distância entre as coordenadas máxima e mínima para x
        x_dist = 1 - (-1)
        # Distância entre as coordenadas máxima e mínima para y
        y_dist = 1 - (-1)
        scaled_x = ((x / x_dist) + 0.5) * largura
        scaled_y = (1 - ((y / y_dist) + 0.5)) * altura
        return [round(scaled_x), round(scaled_y)]


def calula_delta(ponto_final: int, ponto_inicial: int) -> float:
    return (ponto_final - ponto_inicial)


def produz_fragmento(x: float, y: float) -> list:
    x_medio = (x)
    y_medio = y
    ponto_x_medio = math.floor(x_medio+0.5)
    ponto_y_medio = math.floor(y_medio+0.5)
    return [ponto_x_medio, ponto_y_medio]


def rasterizacao_delta_x_maior_delta_y(ponto1: Ponto, m, b, x2) -> list:
    x1,  y1 = ponto1.x,  ponto1.y
    pontos: list = []
    pontos.append(produz_fragmento(x1, y1))
    while (x1 < x2):
        x1 = x1 + 1
        if (m != 0):
            y1 = m*x1 + b
        pontos.append(produz_fragmento(x1, y1))
    return pontos


def rasterizacao_delta_y_maior_delta_x(ponto1: Ponto, m, b, ponto2: Ponto) -> list:
    x1, x2, y1, y2 = ponto1.x, ponto2.x, ponto1.y, ponto2.y

    pontos: list = []
    pontos.append(produz_fragmento(x1, y1))
    while (y1 < y2):
        y1 += 1
        if (m != 0):
            x1 = (y1-b)/m
        else:
            x1 = x2
        pontos.append(produz_fragmento(x1, y1))
    return pontos


def rasterizacao_de_retas(ponto1: Ponto, ponto2: Ponto) -> None:
    primeiro_ponto, segundo_ponto = ponto1, ponto2
    pontos: list

    if (ponto2.y < ponto1.y):
        primeiro_ponto, segundo_ponto = segundo_ponto, primeiro_ponto

    x = primeiro_ponto.x
    y = primeiro_ponto.y
    delta_x = calula_delta(segundo_ponto.x, primeiro_ponto.x)
    delta_y = calula_delta(segundo_ponto.y, primeiro_ponto.y)
    if (delta_x != 0):
        m = delta_y/delta_x
    else:
        m = 0  # como o x não varia , a reta não possui inclinação

    if (abs(delta_x) > abs(delta_y)):
        b = (y - m)*x
        pontos = rasterizacao_delta_x_maior_delta_y(
            primeiro_ponto, m, b, segundo_ponto.x)
    else:
        b = (y-m)*x
        pontos = rasterizacao_delta_y_maior_delta_x(
            primeiro_ponto, m, b, segundo_ponto)

    return pontos


todos_os_pontos = []

# PONTOS DO TRIANGULO
# BASE
primeiro_ponto = Ponto(-1, -1)
segundo_ponto = Ponto(1, -1)
# # reta vertical
r2_ponto1 = Ponto(1, -1)
r2_ponto2 = Ponto(0, 1)
r3_ponto1 = Ponto(0, 1)
r3_ponto2 = Ponto(-1, -1)

# PONTOS DO QUADRADO
#primeira aresta
quadrado_ponto1 = Ponto(-1, -1)
quadrado_ponto2 = Ponto(1, -1)
quadrado_ponto3 = Ponto(1, 1)
quadrado_ponto4 = Ponto(-1, 1)
#segunda aresta
#terceira aresta




#rasterização do triangulo
todos_os_pontos.append(
    rasterizacao_de_retas(primeiro_ponto, segundo_ponto))
todos_os_pontos.append(
    rasterizacao_de_retas(r2_ponto1, r2_ponto2))
todos_os_pontos.append(
    rasterizacao_de_retas(r3_ponto1, r3_ponto2))


#rasterizacao do quadrado
todos_os_pontos.append(
    rasterizacao_de_retas(quadrado_ponto1, quadrado_ponto2))
todos_os_pontos.append(
    rasterizacao_de_retas(quadrado_ponto2, quadrado_ponto3))
todos_os_pontos.append(
    rasterizacao_de_retas(quadrado_ponto3, quadrado_ponto4))
todos_os_pontos.append(
    rasterizacao_de_retas(quadrado_ponto3, quadrado_ponto1))



imag = np.zeros((altura, largura, 3), dtype=np.uint8)
for pontos in todos_os_pontos:
    eixo_x = []
    eixo_y = []
    print(pontos)
    for ponto in pontos:
        lista = tuple(ponto)
        # imag[int(lista[0]), int(lista[1])] = [255, 0, 0]
        eixo_x.append(int(ponto[0]))
        eixo_y.append(int(ponto[1]))
    # print(eixo_y)
    plt.plot(eixo_x, eixo_y)
# plt.imshow(imag)
plt.show()
