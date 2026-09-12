from pathlib import Path

import cv2


def main() -> None:
    """Carrega uma imagem, inspeciona seus arrays e monta um painel."""

    pasta = Path(__file__).resolve().parent
    caminho_imagem = pasta / "teste_ambiente.png"

    # Carrega a imagem em cores. O OpenCV usa a ordem BGR por padrao.
    colorida = cv2.imread(str(caminho_imagem), cv2.IMREAD_COLOR)

    # Sempre valide o retorno de imread: None indica falha de leitura.
    if colorida is None:
        raise FileNotFoundError(
            f"Imagem nao encontrada em {caminho_imagem}. "
            "Execute primeiro 00_verificar_ambiente.py."
        )
