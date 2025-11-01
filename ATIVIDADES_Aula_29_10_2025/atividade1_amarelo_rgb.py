"""
ATIVIDADE 1 - Identificação de Regiões Amarelas (APENAS RGB)

Objetivo: Identificar e destacar regiões amarelas em uma imagem
Conceitos: Manipulação de canais RGB, máscaras booleanas, thresholding
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ============================================================================
# CONFIGURAÇÃO: Defina o caminho da sua imagem aqui
# ============================================================================
fname = "trafficsign.jpg"  # Usando caminho relativo - você pode trocar por outra imagem

# ------------------- PARÂMETROS DE LIMIAR -------------------
# Critérios simples para "amarelo" em RGB:
# - R alto e G alto; B baixo.
# - R e G de magnitude semelhante (amarelo é mistura R+G).
R_MIN = 180    # mínimo pra canal R ser considerado "alto"
G_MIN = 140    # mínimo pra canal G ser considerado "alto"
B_MAX = 80     # máximo pra canal B ser considerado "baixo"

# Consistência R~G: quão próximos R e G devem ser (em valor absoluto)
RG_DIFF_MAX = 50   # quanto menor, mais estrito

# ============================================================================
# PROCESSAMENTO
# ============================================================================

print(f"Carregando imagem: {fname}")
img = Image.open(fname).convert("RGB")
arr = np.array(img, dtype=np.uint8)     # (H, W, 3)
R, G, B = arr[...,0], arr[...,1], arr[...,2]

# Máscara de amarelo (booleana)
mask = (
    (R >= R_MIN) &
    (G >= G_MIN) &
    (B <= B_MAX) &
    (np.abs(R - G) <= RG_DIFF_MAX)
)

# Cria uma sobreposição: destaca o amarelo e "apaga" o restante
overlay = arr.copy()
dim_factor = 0.25  # quanto escurecer o que NÃO é amarelo (0=preto, 1=sem escurecer)
overlay[~mask] = (overlay[~mask] * dim_factor).astype(np.uint8)

# ============================================================================
# VISUALIZAÇÃO
# ============================================================================

plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Imagem original")
plt.axis("off")
plt.imshow(arr)

plt.subplot(1,3,2)
plt.title("Máscara (amarelo)")
plt.axis("off")
plt.imshow(mask, cmap="gray")

plt.subplot(1,3,3)
plt.title("Amarelo destacado")
plt.axis("off")
plt.imshow(overlay)

plt.tight_layout()
plt.show()

print("✅ Processamento concluído!")
