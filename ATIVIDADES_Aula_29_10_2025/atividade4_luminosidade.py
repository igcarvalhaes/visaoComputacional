"""
ATIVIDADE 4 - Ajuste de Luminosidade

Objetivo: Modificar o brilho de imagens
Conceitos: Transformação linear de pixels, convertScaleAbs
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# CONFIGURAÇÃO: Defina o caminho da sua imagem aqui
# ============================================================================
fname = "coloredpencils.jpg"  # Usando caminho relativo para evitar problemas com caracteres especiais

# ------------------- PARÂMETROS DE LUMINOSIDADE -------------------
# Fator de luminosidade: valores positivos clareiam, negativos escurecem
FATOR = 50  # Tente variar: -100 (mais escuro) até +100 (mais claro)

# ============================================================================
# PROCESSAMENTO
# ============================================================================

print(f"Carregando imagem: {fname}")

# Carregar a imagem
img = cv2.imread(fname)

if img is None:
    print(f"❌ Erro: Não foi possível carregar a imagem '{fname}'")
    print("   Verifique se o caminho está correto e se o arquivo existe.")
    exit(1)

# Converter de BGR (OpenCV) para RGB (matplotlib)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Alterar luminosidade
# cv2.convertScaleAbs aplica: novo_pixel = alpha*pixel + beta
# alpha = 1 (não muda contraste), beta = fator (mudança de brilho)
print(f"Aplicando ajuste de luminosidade (beta={FATOR})...")
img_lum = cv2.convertScaleAbs(img_rgb, alpha=1, beta=FATOR)

# ============================================================================
# VISUALIZAÇÃO
# ============================================================================

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.title("Imagem Original")
plt.imshow(img_rgb)
plt.axis("off")

plt.subplot(1,2,2)
plt.title(f"Luminosidade ajustada (beta={FATOR})")
plt.imshow(img_lum)
plt.axis("off")

plt.tight_layout()
plt.show()

print("✅ Ajuste de luminosidade concluído!")
print(f"   Fator aplicado: {FATOR}")
if FATOR > 0:
    print(f"   Imagem ficou mais CLARA (+{FATOR})")
elif FATOR < 0:
    print(f"   Imagem ficou mais ESCURA ({FATOR})")
else:
    print(f"   Sem mudanças (fator = 0)")
