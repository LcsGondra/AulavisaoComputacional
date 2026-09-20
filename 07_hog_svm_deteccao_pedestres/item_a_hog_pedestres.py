"""Exemplo 07 — Detecção de Pedestres com HOG em Vídeo Real do YouTube.

Suporta:
- Arquivo local de vídeo (ex: ../data/pedestres.mp4 ou dados/pedestres.mp4)
- Streaming direto do YouTube via yt-dlp
- Download automático sob demanda
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

# Configura codificação UTF-8 no terminal Windows para evitar erro em caracteres acentuados
if sys.platform == "win32":
    try:
        os.system("chcp 65001 > nul 2>&1")
    except Exception:
        pass

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import cv2
import numpy as np


def obter_fonte_video(caminho_video: str | None, url_yt: str, stream: bool) -> str:
    # 1. Se informou caminho direto que existe
    if caminho_video and Path(caminho_video).exists():
        return caminho_video

    # 2. Verifica locais padrão do repositório
    for padrao in [
        Path(__file__).resolve().parent.parent / "data" / "pedestres.mp4",
        Path(__file__).resolve().parent.parent.parent / "VisaoComputacional" / "tp3" / "dados" / "pedestres.mp4",
    ]:
        if padrao.exists() and padrao.stat().st_size > 1000:
            return str(padrao)

    # 3. Stream direto ou download com yt-dlp
    try:
        import yt_dlp

        if stream:
            print(f"[+] Obtendo stream direto do YouTube: {url_yt}...")
            with yt_dlp.YoutubeDL({"format": "134/135/bestvideo", "quiet": True}) as ydl:
                info = ydl.extract_info(url_yt, download=False)
                return info["url"]
        else:
            dest = Path(__file__).resolve().parent.parent / "data" / "pedestres.mp4"
            dest.parent.mkdir(parents=True, exist_ok=True)
            print(f"[+] Baixando vídeo de pedestres do YouTube para {dest}...")
            with yt_dlp.YoutubeDL({"format": "134/135/bestvideo", "outtmpl": str(dest), "quiet": False}) as ydl:
                ydl.download([url_yt])
            return str(dest)
    except Exception as e:
        print(f"[!] Erro ao obter vídeo do YouTube ({e}).")
        return caminho_video or "pedestres.mp4"


def main():
    p = argparse.ArgumentParser(description="Detecção de Pedestres com HOG em Vídeo")
    p.add_argument("--video", type=str, default=None, help="Caminho do arquivo local de vídeo")
    p.add_argument("--stream", action="store_true", help="Faz streaming direto do YouTube")
    p.add_argument("--url", type=str, default="https://www.youtube.com/watch?v=YzcawvDGe4Y", help="URL do YouTube")
    p.add_argument("--frames", type=int, default=100, help="Quantidade máxima de frames a processar")
    p.add_argument("--visualizar", action="store_true", help="Abre janela de visualização ao vivo com cv2.imshow")
    a = p.parse_args()

    video_src = obter_fonte_video(a.video, a.url, a.stream)
    print(f"[+] Processando vídeo: {video_src[:75]}...")

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cenarios = {
        "rapido": dict(winStride=(12, 12), padding=(8, 8), scale=1.10),
        "preciso": dict(winStride=(4, 4), padding=(8, 8), scale=1.03),
    }

    def roda(nome: str):
        cap = cv2.VideoCapture(video_src)
        ts = []
        total = frames = 0
        c = cenarios[nome]

        while frames < a.frames:
            ok, f = cap.read()
            if not ok:
                break
            t = time.perf_counter()
            rects, w = hog.detectMultiScale(f, winStride=c["winStride"], padding=c["padding"], scale=c["scale"])
            ms = (time.perf_counter() - t) * 1000
            ts.append(ms)
            total += len(rects)
            frames += 1

            if a.visualizar:
                for x, y, ww, hh in rects:
                    cv2.rectangle(f, (x, y), (x + ww, y + hh), (0, 255, 0), 2)
                cv2.putText(f, f"{nome} det={len(rects)} {ms:.1f} ms", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
                cv2.imshow("HOG People Detector", f)
                if cv2.waitKey(1) & 0xFF == 27:
                    break

            if frames % 25 == 0 or frames == 1:
                print(f"[{nome}] frame={frames:04d} det={len(rects):2d} inferencia={ms:7.2f} ms")

        cap.release()
        if a.visualizar:
            cv2.destroyAllWindows()
        media = float(np.mean(ts)) if ts else 0
        return nome, frames, total / frames if frames else 0, media, 1000 / media if media else 0

    r = [roda("rapido"), roda("preciso")]
    print("\n" + "=" * 72)
    print(f"{'Cenario':<12}{'Frames':>10}{'Det/frame':>14}{'ms/frame':>14}{'FPS':>12}")
    print("-" * 72)
    for n, f, d, m, fps in r:
        print(f"{n:<12}{f:>10d}{d:>14.2f}{m:>14.2f}{fps:>12.2f}")
    print("=" * 72)


if __name__ == "__main__":
    main()
