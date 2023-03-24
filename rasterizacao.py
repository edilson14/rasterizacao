import math
import matplotlib.pyplot as plt


class Ponto:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def calula_delta(ponto_final: int, ponto_inicial: int) -> float:
    return math.fabs(ponto_final - ponto_inicial)


def produz_fragmento(x: float, y: float) -> list:
    x_medio = math.ceil(x)
    y_medio = math.ceil(y)
    ponto_x_medio = x_medio+0.5
    ponto_y_medio = y_medio+0.5
    return [ponto_x_medio, ponto_y_medio]


def rasterizacao_delta_x_maior_delta_y(x, y, m, b, x2) -> list:
    pontos: list = []
    pontos.append(produz_fragmento(x, y))
    while (x < x2):
        x = x+1
        y = m*x + b
        pontos.append(produz_fragmento(x, y))
    return pontos


def rasterizacao_delta_y_maior_delta_x(x, y, m, b, y2) -> list:
    pontos: list = []
    pontos.append(produz_fragmento(x, y))
    while (y < y2):
        y = y+1
        x = (y-b)/m
        pontos.append(produz_fragmento(x, y))
    return pontos


def rasterizacao_de_retas(ponto1: Ponto, ponto2: Ponto) -> None:
    pontos: list
    eixo_x: list = []
    eixo_y: list = []
    x = ponto1.x
    y = ponto1.y
    delta_x = calula_delta(ponto2.x, ponto1.x)
    delta_y = calula_delta(ponto2.y, ponto1.y)
    if (delta_x > delta_y):
        if (delta_x != 0):
            m = delta_y/delta_x
        else:
            m = delta_y
        b = y - m*x
        pontos = (rasterizacao_delta_x_maior_delta_y(x, y, m, b, ponto2.x))
    else:
        m = delta_y/delta_x
        b = y-m*x
        pontos = rasterizacao_delta_y_maior_delta_x(x, y, m, b, ponto2.y)
    print(pontos)
    for ponto in pontos:
        eixo_x.append(ponto[0])
        eixo_y.append(ponto[1])
    plt.plot(eixo_x, eixo_y)
    plt.show()


primeiro_ponto = Ponto(0, 9)
segundo_ponto = Ponto(3, 1)

rasterizacao_de_retas(primeiro_ponto, segundo_ponto)
