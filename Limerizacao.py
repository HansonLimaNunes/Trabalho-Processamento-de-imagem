import os
import srcs.histograma as his 
import srcs.matriz as ma
import srcs.imagens_file as imfi
import srcs.imagens_transformacoes as transformacoes
import numpy as np
import matplotlib.pyplot as plt
import cv2

nome_file = os.path.join('Glaze.jpg')
matriz_colorida = imfi.file_to_matriz(nome_file)
plt.imshow(matriz_colorida)
plt.show()

matriz_cinza = transformacoes.imagem_to_cinza(matriz_colorida)
print(matriz_colorida.shape)
print(matriz_cinza.shape)
plt.imshow(matriz_cinza, cmap='gray')
plt.show()


image = cv2.imread('Glaze.jpg')
T = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
T = cv2.threshold(T, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

his.histo(matriz_cinza)

histograma = his.histo2(matriz_cinza)
threshold = T[0]
print(threshold)
plt.plot(range(256), histograma)
plt.plot([threshold, threshold], [0, 40_000])
plt.show()
 
ma.mmatrix_segmentada(matriz_cinza, threshold)