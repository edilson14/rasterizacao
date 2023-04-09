import numpy as np
class Imagem:
    def __init__(self) -> None:
        pass

    def criar_imagem_geometrica(todos_os_pontos, resolucao) -> any:
        imag = np.zeros((resolucao[0], resolucao[1], 3), dtype=np.uint8)
        for pontos in todos_os_pontos:
            eixo_x = []
            eixo_y = []
            for ponto in pontos:
                eixo_x.append(int(ponto[0]))
                eixo_y.append(int(ponto[1]))
            imag[eixo_y, eixo_x] = [255, 0, 0]
        return imag
    
    def criar_imagem_reta(pontos, resolucao) -> any:
        imag = np.zeros((resolucao[0], resolucao[1], 3), dtype=np.uint8)
        eixo_x = []
        eixo_y = []
        for ponto in pontos:
                eixo_x.append(int(ponto[0]))
                eixo_y.append(int(ponto[1]))
        imag[eixo_y, eixo_x] = [255, 0, 0]
        return imag
