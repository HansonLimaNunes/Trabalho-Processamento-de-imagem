import numpy as np
import matplotlib.pyplot as plt

def mmatrix_segmentada(matriz_cinza: np.array, threshold: np.int ):
    linhas = matriz_cinza.shape[0]
    colunas = matriz_cinza.shape[1]
    matrix_segmentada = np.zeros((linhas, colunas))
    for i in range(linhas):
        for j in range(colunas):
            cor = matriz_cinza[i,j]
            if cor < threshold:
                matrix_segmentada[i,j] = 255
            else:
                matrix_segmentada[i,j] = 0
    plt.imshow(matrix_segmentada, cmap='gray')
    return plt.show()
