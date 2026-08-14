

"""Exemplo — Captura de foto via webcam.

Uso:
    python capturar_foto.py
"""

from __future__ import annotations

from pathlib import Path
import cv2


def main() -> None:
    # 0 é o índice da webcam padrão (integrada ao notebook ou USB)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return

    print("--- INSTRUÇÕES ---")
    print("Pressione 'ESPAÇO' para tirar e salvar a foto.")
    print("Pressione 'Q' ou 'ESC' para sair sem tirar foto.")

    while True:
        # Captura quadro a quadro da câmera
        sucesso, frame = cap.read()

        if not sucesso:
            print("Erro ao ler imagem da webcam.")
            break

        # Exibe o fluxo de vídeo ao vivo
        cv2.imshow("Webcam - Pressione ESPAÇO para capturar", frame)

        # Captura a tecla pressionada a cada frame (1 ms)
        tecla = cv2.waitKey(1) & 0xFF

        # Tecla ESPAÇO (código ASCII 32) -> Salva a foto
        if tecla == 32:
            pasta_saida = Path("dados/gerados")
            pasta_saida.mkdir(parents=True, exist_ok=True)
            caminho_foto = pasta_saida / "sua_foto.jpg"

            # Salva o frame atual no arquivo de imagem
            cv2.imwrite(str(caminho_foto), frame)
            print(f"✅ Foto salva com sucesso em: {caminho_foto.resolve()}")
            break

        # Teclas 'q' ou 'ESC' -> Cancela e sai
        elif tecla in (ord("q"), 27):
            print("Captura cancelada pelo usuário.")
            break

    # Libera o controle da webcam e fecha a janela
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
