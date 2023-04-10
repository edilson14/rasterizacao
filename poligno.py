import numpy as np


def rasterizacao_de_face(arestas, largura, altura):
    img_face_orig = np.zeros((altura, largura, 3), dtype="uint8")
    img_face = np.zeros((altura, largura, 3), dtype="uint8")

    for aresta in arestas:
        for ponto in aresta:
            img_face_orig[ponto[0], ponto[1]] = [255, 255, 255]

    for i in range(altura):
        cont_h = 0
        sava_ponto_h = []
        cont_v = 0
        sava_ponto_v = []
        for j in range(largura - 1):
            # Horizontal
            if np.array_equal(img_face_orig[i, j], [1, 1, 1]):
                cont_h += 1
                if len(sava_ponto_h) > 1:
                    del sava_ponto_h[0]
                sava_ponto_h.append([i, j])
            if cont_h == 2:
                variacao_h = abs(sava_ponto_h[1][1] - sava_ponto_h[0][1])
                for w in range(variacao_h):
                    img_face[i, w + sava_ponto_h[0][1]] = [255, 255, 255]
                cont_h = 1

            # Vertical
            if np.array_equal(img_face_orig[j, i], [1, 1, 1]):
                cont_v += 1
                if len(sava_ponto_v) > 1:
                    del sava_ponto_v[0]
                sava_ponto_v.append([j, i])
            if cont_v == 2:
                variacao_v = sava_ponto_v[1][0] - sava_ponto_v[0][0]
                for z in range(variacao_v):
                    img_face[z + sava_ponto_v[0][0], i] = [255, 255, 255]
                cont_v = 1

    arestas_rasterizadas = []
    for i in range(altura):
        for j in range(largura):
            if np.array_equal(img_face[i, j], img_face_orig[i, j]):
                continue

            if np.array_equal(img_face[i, j], [255, 255, 255]):
                arestas_rasterizadas.append([i, j])

    return arestas_rasterizadas
