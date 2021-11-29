import numpy as np
import matplotlib.pyplot as plt

def histo (matriz_cinza: np.array):

    histograma = np.zeros(256).astype(int)
    print(histograma)

    linhas = matriz_cinza.shape[0]
    colunas = matriz_cinza.shape[1]
    for i in range(linhas):
        for j in range(colunas):
            cor = matriz_cinza[i,j]
            cor = int(cor)
            histograma[cor] = histograma[cor] + 1
            
    print(histograma)
    plt.plot(range(256), histograma)
    
    return plt.show()

def histo2(matriz_cinza: np.array):
    histograma = np.zeros(256).astype(int)
    print(histograma)

    linhas = matriz_cinza.shape[0]
    colunas = matriz_cinza.shape[1]
    for i in range(linhas):
        for j in range(colunas):
            cor = matriz_cinza[i,j]
            cor = int(cor)
            histograma[cor] = histograma[cor] + 1
    print(histograma)
    plt.plot(range(256), histograma)
    
    return histograma