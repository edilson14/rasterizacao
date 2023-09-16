class Pontos:
    def __init__(self, x_value: float, y_value: float, altura: int, largura: int) -> list[int]:
        self.__x_value = x_value
        self.__y_value = y_value
        self.x
        self.y
        self.__normalizar(altura=altura, largura=largura)

    # transforma os pontos entre zero e um para uma escala definida
    def __normalizar(self, altura: int, largura: int) -> list[int]:
        """
        :param altura - altura a ser transformada, correspondente a x 
        :param largura - largura da resoluçao a ser transformada

        """
        x = ((largura - 1) * (self.__x_value+1))/2
        y = ((altura - 1) * (self.__y_value+1))/2

    def calcula_delta(self, ponto_inicial: int, ponto_final: int) -> int:
        return ponto_final - ponto_inicial
