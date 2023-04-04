import math
import matplotlib.pyplot as plt


class Ponto:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def calula_delta(ponto_final: int, ponto_inicial: int) -> float:
    return (ponto_final - ponto_inicial)


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
        ponto1.x += 1
        if (m != 0):
            ponto1.y = m*ponto1.x + b
        pontos.append(produz_fragmento(ponto1.x, ponto1.y))
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
    # lista dos pontos para serem exibidas no grafico
    eixo_x: list = []
    eixo_y: list = []
    if (ponto2.y < ponto1.y or ponto2.x < ponto1.y):
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
    print(pontos)
    # pontos.reverse()
    print(pontos)
    for ponto in pontos:
        eixo_x.append(ponto[0])
        eixo_y.append(ponto[1])
    plt.ylabel('Eixo Y')
    plt.xlabel('Eixo X')
    plt.plot(eixo_x, eixo_y)
    plt.show()


primeiro_ponto = Ponto(9, 3)
segundo_ponto = Ponto(0, 3)

rasterizacao_de_retas(primeiro_ponto, segundo_ponto)
