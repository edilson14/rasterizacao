import math
import matplotlib.pyplot as plt
import imagem as forms
# import numpy as np

largura, altura = 100, 100
resolucao1 = largura, altura
resolucao2 = largura*3, altura*3
resolucao3 = largura*6, altura*6
resolucao4 = largura*8, altura*6
resolucao5 = int(altura*19.2), int(altura*10.8)


class Ponto:
    def __init__(self, x: int, y: int, resolucao: list) -> None:
        self.x, self.y = self.scale_point(x, y, resolucao[0], resolucao[1])

    def scale_point(self, x, y, largura, altura):
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
    ponto_x_medio = int(x_medio+0.5)
    ponto_y_medio = int(y_medio+0.5)
    return [ponto_x_medio, ponto_y_medio]


def rasterizacao_delta_x_maior_delta_y(ponto1: Ponto, m, b, x2) -> list:
    x1,  y1 = ponto1.x,  ponto1.y
    pontos: list = []
    pontos.append(produz_fragmento(x1, y1))
    if (x1 < x2):
        while (x1 <= x2):
            x1 = x1 + 1
            if (m != 0):
                y1 = math.ceil(m*x1 + b)
            pontos.append(produz_fragmento(x1, y1))
    else:
        aux = x1
        while (x2 <= aux):
            x2 = x2 + 1
            x1 = x1-1
            if (m != 0):
                y1 = math.ceil(m*x1 + b)
            pontos.append(produz_fragmento(x1, y1))
    return pontos


def rasterizacao_delta_y_maior_delta_x(ponto1: Ponto, m, b, ponto2: Ponto) -> list:
    x1,  y1, y2 = ponto1.x,  ponto1.y, ponto2.y

    pontos: list = []
    if (y1 < y2):
        while (y1 <= y2):
            pontos.append(produz_fragmento(x1, y1))
            y1 = y1 + 1
            if (m != 0):
                x1 = ((y1-b)/m)
    else:
        aux = y1
        while y2 <= aux:
            pontos.append(produz_fragmento(x1, y1))
            y2 = y2 + 1
            y1 = y1 - 1
            if (m != 0):
                x1 = math.ceil((y1-b) / m)

    return pontos


def rasterizacao_de_retas(ponto1: Ponto, ponto2: Ponto) -> None:
    primeiro_ponto,  = ponto1,
    pontos: list

    delta_x = calula_delta(ponto2.x, ponto1.x)
    delta_y = calula_delta(ponto2.y, ponto1.y)

    x = primeiro_ponto.x
    y = primeiro_ponto.y
    if (delta_x != 0):
        m = delta_y/delta_x
        b = y - m * x
    else:
        m = 0  # como o x não varia , a reta não possui inclinação
        b = 0

    if (abs(delta_x) > abs(delta_y)):
        pontos = rasterizacao_delta_x_maior_delta_y(
            primeiro_ponto, m, b, ponto2.x)
    else:
        pontos = rasterizacao_delta_y_maior_delta_x(
            primeiro_ponto, m, b, ponto2)

    return pontos


def rasteriza_poligno(poligno):
    largura, altura = poligno.shape[:2]
    pontos_internos = []
    for i in range(largura):
        count = 0
        aux = []
        for j in range(altura):
            if np.array_equal(poligno[i, j], [1, 1, 1]):
                count += 1
                if count == 1:
                    aux.append(j)
        if count % 2 == 1:
            for k in range(0, len(aux), 2):
                for j in range(aux[k], aux[k+1]+1 if k+1 < len(aux) else altura):
                    pontos_internos.append([i, j])
    return pontos_internos


tri_ponto1 = (-0.5, -0.87)
tri_ponto2 = (0.5, -0.87)
tri_ponto3 = (0, 0.73)


def triangulo(tri_ponto1, tri_ponto2, tri_ponto3, resolucao):
    pontos = []
    tri_ponto1 = Ponto(tri_ponto1[0], tri_ponto1[1], resolucao)
    tri_ponto2 = Ponto(tri_ponto2[0], tri_ponto2[1], resolucao)
    tri_ponto3 = Ponto(tri_ponto3[0], tri_ponto3[1], resolucao)
    pontos.append(rasterizacao_de_retas(tri_ponto1, tri_ponto2))
    pontos.append(rasterizacao_de_retas(tri_ponto2, tri_ponto3))
    pontos.append(rasterizacao_de_retas(tri_ponto3, tri_ponto1))
    return pontos


pontosImagem1 = triangulo(tri_ponto1,tri_ponto2,tri_ponto3,resolucao4) 

# pontosImagem1.extend(pontosInternos)


Image1 = forms.Imagem.criar_imagem_geometrica(pontosImagem1, resolucao4)

# print(Image1[5, 2])

# Image2 = criar_imagem(pontosImagem2, resolucao2, False)
# Image3 = criar_imagem(pontosImagem3, resolucao4, True)
# Image3_3 = criar_imagem(pontosImagem3, resolucao4, False)

for pontos in pontosInternos:
        print(pontos)
        Image1[pontos[1],pontos[0]] = [255,255,255]
# for ponto in pontos:

fig = plt.figure(figsize=(10, 7))
rows = 1
columns = 3


fig.add_subplot(rows, columns, 1)
plt.imshow(Image1)
plt.axis('off')
plt.title("100x100")

# fig.add_subplot(rows, columns, 2)
# plt.imshow(Image2)
# plt.axis('off')
# plt.title("300x300")

# fig.add_subplot(rows, columns, 3)
# plt.imshow(Image3)
# plt.axis('off')
# plt.title("600x600")


plt.show()
