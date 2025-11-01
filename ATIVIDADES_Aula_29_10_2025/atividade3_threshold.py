"""
ATIVIDADE 3 - Threshold (Limiarização) com OpenCV

Objetivo: Aprender diferentes técnicas de limiarização
Conceitos: 5 tipos de threshold (binary, binary_inv, trunc, tozero, tozero_inv)
"""

import cv2
import matplotlib.pyplot as plt

# ============================================================================
# CONFIGURAÇÃO: Defina o caminho da sua imagem aqui
# ============================================================================
fname = "bookpage.jpg"  # Usando caminho relativo para evitar problemas com caracteres especiais

# ------------------- PARÂMETROS DO THRESHOLD -------------------
LIMIAR = 127     # Valor de corte (0-255)
VALOR_MAX = 255  # Valor máximo atribuído (branco)

# ============================================================================
# PROCESSAMENTO
# ============================================================================

print(f"Carregando imagem: {fname}")

# Ler a imagem em escala de cinza
img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"❌ Erro: Não foi possível carregar a imagem '{fname}'")
    print("   Verifique se o caminho está correto e se o arquivo existe.")
    exit(1)

# Aplicar diferentes tipos de threshold
# cv2.threshold(imagem, limiar, valor_max, tipo)
# - limiar: valores abaixo dele são tratados de uma forma, acima de outra
# - valor_max: valor atribuído aos pixels (ex.: 255 -> branco)
# - tipo: define a forma de aplicação do limiar

print("Aplicando diferentes tipos de threshold...")

# THRESH_BINARY: pixels < limiar = 0, >= limiar = valor_max
_, th_bin = cv2.threshold(img, LIMIAR, VALOR_MAX, cv2.THRESH_BINARY)

# THRESH_BINARY_INV: inverso do binário
_, th_inv = cv2.threshold(img, LIMIAR, VALOR_MAX, cv2.THRESH_BINARY_INV)

# THRESH_TRUNC: pixels > limiar são truncados para o limiar
_, th_trunc = cv2.threshold(img, LIMIAR, VALOR_MAX, cv2.THRESH_TRUNC)

# THRESH_TOZERO: pixels < limiar = 0, >= limiar = mantém valor original
_, th_tozero = cv2.threshold(img, LIMIAR, VALOR_MAX, cv2.THRESH_TOZERO)

# THRESH_TOZERO_INV: inverso do tozero
_, th_tozero_inv = cv2.threshold(img, LIMIAR, VALOR_MAX, cv2.THRESH_TOZERO_INV)

# ============================================================================
# VISUALIZAÇÃO
# ============================================================================

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.title("Original")
plt.axis("off")
plt.imshow(img, cmap="gray")

plt.subplot(2,3,2)
plt.title("THRESH_BINARY")
plt.axis("off")
plt.imshow(th_bin, cmap="gray")

plt.subplot(2,3,3)
plt.title("THRESH_BINARY_INV")
plt.axis("off")
plt.imshow(th_inv, cmap="gray")

plt.subplot(2,3,4)
plt.title("THRESH_TRUNC")
plt.axis("off")
plt.imshow(th_trunc, cmap="gray")

plt.subplot(2,3,5)
plt.title("THRESH_TOZERO")
plt.axis("off")
plt.imshow(th_tozero, cmap="gray")

plt.subplot(2,3,6)
plt.title("THRESH_TOZERO_INV")
plt.axis("off")
plt.imshow(th_tozero_inv, cmap="gray")

plt.tight_layout()
plt.show()

print("✅ Threshold aplicado!")
print(f"   Limiar usado: {LIMIAR}")
print(f"   Valor máximo: {VALOR_MAX}")
