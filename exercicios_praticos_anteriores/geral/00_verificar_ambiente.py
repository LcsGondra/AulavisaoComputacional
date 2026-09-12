from pathlib import Path

import cv2
import numpy as np


def main() -> None:
    """Executa uma verificacao minima do ambiente."""

    # Exibe as versoes para facilitar a reproducao e o diagnostico.
    print(f"Versao do OpenCV: {cv2.__version__}")
    print(f"Versao do NumPy:  {np.__version__}")

    # Cria uma imagem preta com 240 linhas, 320 colunas e 3 canais BGR.
    # O dtype uint8 representa cada canal com valores inteiros de 0 a 255.
    imagem = np.zeros((240, 320, 3), dtype=np.uint8)

    # Desenha elementos simples para confirmar que o modulo imgproc funciona.
    cv2.rectangle(imagem, (20, 20), (300, 220), (0, 180, 0), thickness=3)
    cv2.circle(imagem, (160, 120), 55, (255, 0, 0), thickness=-1)
    cv2.p
