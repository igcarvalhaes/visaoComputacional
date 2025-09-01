import numpy as np 
import matplotlib.pyplot as plt

# somando dois numeros  
a = 4;
b = 5;

soma = a + b;

print("O resultado da soma é: " + str(soma));

# criando um vetor
vetor = []
vetor.append(4)

print(vetor)

vetor.append(-58);
print(vetor)

# percorrendo vetor 
for i in vetor:
    print(i)

# criando um vetor vazio
vetor1 = []
# adicionando elementos de 0 a 4 no vetor1
for i in range(5):
    vetor1.append(i)

print(vetor1)

# criando copia do vetor
vetor2 = vetor1.copy()
print(vetor2)

# criando uma matriz
#biblioteca que suporta o processamento de  grandes multi-dimensionais arranjos e matrizes, juntamente com uma grande coleção de funções matemáticas de alto nível para operar sobre
# estas matrizes.

matriz = np.array([[5, 8, 4], [6, 10, 64], [22, 74, 61]]);

print(matriz)

# acessando linha 0 e coluna 0 da matriz
matriz[0, 0] #isso retorna o numero 5

# acessando os elementos da segunda coluna da matriz
matriz[:, 1] #isso retorna a segunda coluna [8, 10, 74]

# acessando os elementos da terceira linha da matriz
matriz[2, :] #isso retorna a terceira linha [22, 74, 61]

# criando matriz de 3 camadas 8x9x3. As primeira, segunda e terceira camadas serão compostas pelas variaçoes de tons das camadas vermelha, azul e verde. 


# Cada camada é uma matriz! Para declarar uma matriz de 1’s com 8 linhas, 9 colunas e 3 camadas

R = np.array([
 [1, 1, 0, 0, 0, 0, 0, 1, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1],
 [0, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 1, 1, 1, 1, 1, 1, 1, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 0, 1, 1, 1, 0, 1, 1],
 [1, 1, 0, 1, 1, 1, 0, 1, 1],
 [1, 1, 1, 0, 0, 0, 1, 1, 1]
], dtype=np.float32)
G = np.array([
 [1, 1, 0, 0, 0, 0, 0, 1, 1],
 [1, 0, 1, 0, 0, 1, 1, 0, 1],
 [0, 0, 1, 0, 0, 1, 0, 1, 0],
 [0, 0, 0, 1, 1, 0, 0, 1, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 0, 1, 1, 1, 0, 1, 1],
 [1, 1, 0, 1, 1, 1, 0, 1, 1],
 [1, 1, 1, 0, 0, 0, 1, 1, 1]
], dtype=np.float32)
B = np.array([
 [1, 1, 0, 0, 0, 0, 0, 1, 1],
 [1, 0, 1, 0, 0, 1, 1, 0, 1],
 [0, 0, 1, 0, 0, 1, 0, 1, 0],
 [0, 0, 0, 1, 1, 0, 0, 1, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 0, 1, 1, 1, 0, 1, 1],
 [1, 1, 0, 1, 1, 1, 0, 1, 1],
 [1, 1, 1, 0, 0, 0, 1, 1, 1]
], dtype=np.float32)


# cria matriz 8x9x3 nula
# Eu preciso criar uma matriz que vai receber todas as outras 3 matrizes criadas.
M = np.zeros((8,9,3), dtype=np.float32)
# atribui R à 1ª camada de M
M[:,:,0] = R
# atribui G à 2ª camada de M
M[:,:,1] = G
# atribui B à 3ª camada de M
M[:,:,2] = B

#Para mostrar o cogumelo no display:
# import matplotlib.pyplot as plt
# plt.figure(figsize=(4,4))
# im = plt.imshow(M, aspect='auto')
# plt.axis("off")
# plt.show()

# Desafio ( 14 colunas x 16 linhas ) - Mario Pixel Art
# Matriz R (Red) - Vermelho puro, vermelho médio para marrom e vermelho alto para bege
R = np.array([[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0.6, 0.8, 0.6, 0.8, 0.8, 0.8, 0.6, 0.8, 0.8, 0.8, 0, 0],
              [0, 0, 0.6, 0.8, 0.6, 0.8, 0.8, 0.8, 0.6, 0.8, 0.8, 0.8, 0.8, 0],
              [0, 0, 0.6, 0.8, 0.6, 0.6, 0.8, 0.8, 0.8, 0.6, 0.8, 0.8, 0.8, 0],
              [0, 0, 0.6, 0.6, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.6, 0.6, 0, 0],
              [0, 0, 0, 0, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0, 0, 0],
              [0, 0, 0, 0.6, 0.6, 1, 0.6, 0.6, 1, 0, 0, 0, 0, 0],
              [0, 0.6, 0.6, 0.6, 0.6, 1, 0.6, 0.6, 1, 0.6, 0.6, 0.6, 0, 0],
              [0, 0.6, 0.6, 0.6, 0.6, 1, 0.6, 1, 0, 1, 0.6, 0.6, 0.6, 0],
              [0, 0.8, 0.8, 0.6, 1, 0.8, 1, 1, 0.8, 1, 0.6, 0.8, 0.8, 0],
              [0, 0.8, 0.8, 0.8, 1, 1, 1, 1, 1, 1, 0.8, 0.8, 0.8, 0],
              [0, 0.8, 0.8, 1, 1, 1, 0, 0, 1, 1, 1, 0.8, 0.8, 0],
              [0, 0, 0.6, 0.6, 0.6, 0, 0, 0, 0, 0.6, 0.6, 0.6, 0, 0],
              [0, 0.6, 0.6, 0.6, 0.6, 0, 0, 0, 0, 0.6, 0.6, 0.6, 0.6, 0]], 
             dtype=np.float32)

# Matriz G (Green) - Componente verde para marrom, bege e outras cores (mas zero nas posições vermelhas puras)
G = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0.4, 0.6, 0.6, 0.6, 0.4, 0.6, 0, 0, 0, 0, 0],
              [0, 0, 0.3, 0.7, 0.3, 0.7, 0.7, 0.7, 0.3, 0.7, 0.7, 0.7, 0, 0],
              [0, 0, 0.3, 0.7, 0.3, 0.7, 0.7, 0.7, 0.3, 0.7, 0.7, 0.7, 0.7, 0],
              [0, 0, 0.3, 0.7, 0.3, 0.3, 0.7, 0.7, 0.7, 0.3, 0.7, 0.7, 0.7, 0],
              [0, 0, 0.3, 0.3, 0.7, 0.7, 0.7, 0.7, 0.3, 0.3, 0.3, 0.3, 0, 0],
              [0, 0, 0, 0.4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0, 0, 0],
              [0, 0, 0.4, 0.3, 0.3, 0, 0.3, 0.3, 0, 0.4, 0, 0, 0, 0],
              [0, 0.4, 0.3, 0.3, 0.3, 0, 0.3, 0.3, 0, 0.3, 0.3, 0.3, 0, 0],
              [0, 0.3, 0.3, 0.3, 0.3, 0, 0.3, 0, 0, 0, 0.3, 0.3, 0.3, 0],
              [0, 0.6, 0.6, 0.3, 0, 0.6, 0, 0, 0.6, 0, 0.3, 0.6, 0.6, 0],
              [0, 0.6, 0.6, 0.6, 0, 0, 0, 0, 0, 0, 0.6, 0.6, 0.6, 0],
              [0, 0.6, 0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 0.6, 0],
              [0, 0, 0.3, 0.3, 0.3, 0.8, 0.8, 0.8, 0.8, 0.3, 0.3, 0.3, 0, 0],
              [0, 0.3, 0.3, 0.3, 0.3, 0.8, 0.8, 0.8, 0.8, 0.3, 0.3, 0.3, 0.3, 0]], 
             dtype=np.float32)

# Matriz B (Blue) - Componente azul para marrom, bege e azul do macacão (mas zero nas posições vermelhas puras)
B = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0.3, 0.4, 0.4, 0.4, 0.3, 0.4, 0, 0, 0, 0, 0],
              [0, 0, 0.2, 0.5, 0.2, 0.5, 0.5, 0.5, 0.2, 0.5, 0.5, 0.5, 0, 0],
              [0, 0, 0.2, 0.5, 0.2, 0.5, 0.5, 0.5, 0.2, 0.5, 0.5, 0.5, 0.5, 0],
              [0, 0, 0.2, 0.5, 0.2, 0.2, 0.5, 0.5, 0.5, 0.2, 0.5, 0.5, 0.5, 0],
              [0, 0, 0.2, 0.2, 0.5, 0.5, 0.5, 0.5, 0.2, 0.2, 0.2, 0.2, 0, 0],
              [0, 0, 0, 0.3, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0, 0, 0],
              [0, 0, 0.3, 0.2, 0.2, 0, 0.2, 0.2, 0, 0.3, 0, 0, 0, 0],
              [0, 0.3, 0.2, 0.2, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0.2, 0, 0],
              [0, 0.2, 0.2, 0.2, 0.2, 0, 0.2, 0, 0, 0, 0.2, 0.2, 0.2, 0],
              [0, 0.4, 0.4, 0.2, 0, 0.4, 0, 0, 0.4, 0, 0.2, 0.4, 0.4, 0],
              [0, 0.4, 0.4, 0.4, 0, 0, 0, 0, 0, 0, 0.4, 0.4, 0.4, 0],
              [0, 0.4, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0.4, 0],
              [0, 0, 0.2, 0.2, 0.2, 1, 1, 1, 1, 0.2, 0.2, 0.2, 0, 0],
              [0, 0.2, 0.2, 0.2, 0.2, 1, 1, 1, 1, 0.2, 0.2, 0.2, 0.2, 0]], 
             dtype=np.float32)

L = np.zeros((16,14,3), dtype=np.float32)
# atribui R à 1ª camada de L (Red channel)
L[:,:,0] = R
# atribui G à 2ª camada de L (Green channel)
L[:,:,1] = G
# atribui B à 3ª camada de L (Blue channel)
L[:,:,2] = B

# Para mostrar o Mario no display:
plt.figure(figsize=(6,8))
im = plt.imshow(L, aspect='auto')
plt.axis("off")
plt.title("Mario Pixel Art - Vermelho nas coordenadas especificadas")
plt.show()