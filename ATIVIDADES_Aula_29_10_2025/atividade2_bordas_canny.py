"""
ATIVIDADE 2 - Detecção de Bordas com OpenCV (Algoritmo Canny)

Objetivo: Detectar bordas em imagens usando o algoritmo Canny
Conceitos: Conversão para escala de cinza, detecção de bordas, limiares
"""

import cv2
import matplotlib.pyplot as plt

# ============================================================================
# CONFIGURAÇÃO: Defina o caminho da sua imagem aqui
# ============================================================================
fname = "bicicles.jpg"  # Usando caminho relativo para evitar problemas com caracteres especiais

# ------------------- PARÂMETROS DO CANNY -------------------
LIMIAR_INFERIOR = 50   # Valores de gradiente abaixo disso são descartados (era 100)
LIMIAR_SUPERIOR = 150  # Valores acima disso são considerados bordas (era 100)

# ============================================================================
# PROCESSAMENTO
# ============================================================================

print(f"Carregando imagem: {fname}")

# cv2.imread: lê a imagem do arquivo
# cv2.IMREAD_GRAYSCALE converte diretamente para tons de cinza
# Isso é importante, pois a maioria dos detectores de bordas trabalha melhor em escala de cinza
img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"❌ Erro: Não foi possível carregar a imagem '{fname}'")
    print("   Verifique se o caminho está correto e se o arquivo existe.")
    exit(1)

# Aplicar detecção de bordas (Canny)
# cv2.Canny(imagem, limiar_inferior, limiar_superior)
# - limiar_inferior: valores de gradiente abaixo disso são descartados
# - limiar_superior: valores acima disso são considerados bordas
# - valores intermediários dependem da conectividade
# Ajustar os limiares muda a sensibilidade da detecção
bordas = cv2.Canny(img, LIMIAR_INFERIOR, LIMIAR_SUPERIOR)

# ============================================================================
# VISUALIZAÇÃO
# ============================================================================

plt.figure(figsize=(10,5))

# Mostrar a imagem original em cinza
plt.subplot(1,2,1)
plt.title("Imagem Original (Cinza)")
plt.axis("off")
plt.imshow(img, cmap="gray")

# Mostrar o resultado da detecção de bordas
plt.subplot(1,2,2)
plt.title("Bordas (Canny)")
plt.axis("off")
plt.imshow(bordas, cmap="gray")

plt.tight_layout()
plt.show()

print("✅ Detecção de bordas concluída!")
print(f"   Limiares usados: inferior={LIMIAR_INFERIOR}, superior={LIMIAR_SUPERIOR}")
