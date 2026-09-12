from pathlib import Path

import cv2
import numpy as np


def main() -> None:
    """Gera um video curto com formas geometricas em movimento."""

    # Parametros do video de teste.
    largura = 640
    altura = 360
    fps = 30.0
    duracao_segundos = 8
    total_frames = int(fps * duracao_segundos)

    pasta = Path(__file__).resolve().parent
    caminho_saida = pasta / "video_teste.mp4"

    # Define o codec MP4V, geralmente disponivel em instalacoes comuns.
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    # Cria o objeto escritor de video.
    writer = cv2.VideoWriter(
        str(caminho_saida),
        fourcc,
        fps,
        (largura, altura),
    )

