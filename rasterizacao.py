from ponto import Pontos
from math import ceil


class Rasterizacao:
    def __init__(self) -> None:
        self.pontos_rasterizados = []

    def __produz_fragmento(self, x: float, y: float) -> list[int]:

        return [int(x+.05), int(y+0.5)]

    def rasterizacao_de_retas(self, ponto1: Pontos, ponto2: Pontos) -> list[int]:

        delta_x = Pontos.calcula_delta(
            ponto_final=ponto2.x_value, ponto_inicial=ponto1.x_value)
        delta_y = Pontos.calcula_delta(
            ponto_inicial=ponto1.y_value, ponto_final=ponto2.y_value)

        x = ponto1.x_value
        y = ponto1.y_value
        if (delta_x != 0):
            # inclinação da reta
            inclinacao = delta_y/delta_x
            b = y - inclinacao * x
        else:
            inclinacao = 0  # deltax nao varia então a reta nao possui inclinação
            b = 0

        if (abs(delta_x) > abs(delta_y)):
            self.__rasterizacao_deltax_maior_deltay(
                ponto1=ponto1, inclinacao=inclinacao, b=b, x2=ponto2.x)
        else:
            self.__rasterizacao_deltay_maior_deltax()

    # como a iteração está sendo feito no eixo de x , é passado o x2 para saber até onde ele vai percorrer

    def __rasterizacao_deltax_maior_deltay(self, ponto1: Pontos, inclinacao: int, b: int, x2: int) -> list:
        x1, y1 = ponto1.x, ponto1.y
        self.pontos_rasterizados.append(self.__produz_fragmento(x=x1, y=y1))
        if (x1 < x2):
            while (x1 < x2):
                x1 = x1+1
                if (inclinacao != 0):
                    y1 = ceil(inclinacao*x1 + b)
                self.pontos_rasterizados.append(
                    self.__produz_fragmento(x=x1, y=y1))
        # caso o x2 for maior a gente decrementa o valor do x2 até chegar no x1
        else:
            aux = x1
            while (x2 < aux):
                x2 = x2+1
                x1 = x1 - 1
                if (inclinacao != 0):
                    y1 = ceil(inclinacao * x1 + b)
                self.pontos_rasterizados.append(
                    self.__produz_fragmento(x1, y1))
    # tendo em conta que o y varia mais do que o x , faz sentido percorrer o eixo do y

    def __rasterizacao_deltay_maior_deltax(self, ponto1: Pontos, inclinacao: int, b: int, ponto2: Pontos) -> list:
        x1, y1, y2 = ponto1.x, ponto1.y, ponto2.y

        if (y1 < y2):
            while (y1 < y2):
                self.pontos_rasterizados.append(
                    self.__produz_fragmento(x1, y1))
                y1 = y1+1
                if (inclinacao != 0):
                    x1 = ceil((y1 - b)/inclinacao)
        else:
            aux = y1
            while (y2 < aux):
                self.pontos_rasterizados.append(
                    self.__produz_fragmento(x1, y1))
                if(inclinacao != 0):
                    x1 = ceil((y1-b)/inclinacao)
