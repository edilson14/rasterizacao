import math
import matplotlib.pyplot as plt


class Ponto:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def calula_delta(ponto_final: int, ponto_inicial: int) -> float:
    return math.fabs(ponto_final - ponto_inicial)


def produz_fragmento(x: float, y: float) -> list:
    x_medio = math.floor(x)
    y_medio = math.floor(y)
    ponto_x_medio = x_medio+0.5
    ponto_y_medio = y_medio+0.5
    return [ponto_x_medio, ponto_y_medio]


def rasterizacao_delta_x_maior_delta_y(ponto1: Ponto, m, b, x2) -> list:
    pontos: list = []
    pontos.append(produz_fragmento(ponto1.x, ponto1.y))
    while (ponto1.x < x2):
        ponto1.x = ponto1.x+1
        ponto1.y = m*ponto1.x + b
        pontos.append(produz_fragmento(ponto1.x, ponto1.y))
    return pontos


def rasterizacao_delta_y_maior_delta_x(ponto1: Ponto, m, b, ponto2: Ponto) -> list:
    pontos: list = []
    pontos.append(produz_fragmento(ponto1.x, ponto1.y))
    while (ponto1.y < ponto2.y):
        ponto1.y += 1
        if (m != 0):
            ponto1.x = (ponto1.y-b)/m
        else:
            ponto1.x = ponto2.x
        pontos.append(produz_fragmento(ponto1.x, ponto1.y))

    return pontos


def rasterizacao_de_retas(ponto1: Ponto, ponto2: Ponto) -> None:
    pontos: list
    # lista dos pontos para serem exibidas no grafico
    eixo_x: list = []
    eixo_y: list = []

    x = ponto1.x
    y = ponto1.y
    delta_x = calula_delta(ponto2.x, ponto1.x)
    delta_y = calula_delta(ponto2.y, ponto1.y)
    if (delta_x != 0):
        m = delta_y/delta_x
    else:
        m = 0

    if (abs(delta_x) > abs(delta_y)):
        b = (y - m)*x
        pontos = rasterizacao_delta_x_maior_delta_y(ponto1, m, b, ponto2.x)
    else:
        b = (y-m)*x
        pontos = rasterizacao_delta_y_maior_delta_x(ponto1, m, b, ponto2)
    print(pontos)
    for ponto in pontos:
        eixo_x.append(ponto[0])
        eixo_y.append(ponto[1])
    plt.ylabel('Eixo Y')
    plt.xlabel('Eixo X')
    plt.plot(eixo_x, eixo_y)
    plt.show()


primeiro_ponto = Ponto(9, 1)
segundo_ponto = Ponto(1, 3)

rasterizacao_de_retas(primeiro_ponto, segundo_ponto)
