
"""
Funcoes utilitarias para a aula de classificacao de genero aparente e faixa etaria.

Observacao etica importante:
- Os exemplos classificam atributos aparentes a partir de imagens, nao identidade.
- Use somente imagens com consentimento e discuta vieses e limitacoes dos modelos.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple
import time

import cv2
import numpy as np

AGE_BUCKETS = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]
GENDER_LABELS = ["Masculino", "Feminino"]
MODEL_DIR = Path("models/opencv_age_gender")
MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

@dataclass
class Prediction:
    gender: str
    gender_conf: float
    age: str
    age_conf: float


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def load_image(path: str | Path):
    img = cv2.imread(str(path))
    if img is None:
        raise FileNotFoundError(f"Nao foi possivel abrir a imagem: {path}")
    return img


def get_haar_cascade():
    cascade_path = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(str(cascade_path))
    if cascade.empty():
        raise RuntimeError("Haar Cascade nao foi carregado. Verifique a instalacao do opencv-python.")
    return cascade


def detect_faces_haar(frame, scale_factor=1.1, min_neighbors=5, min_size=(60, 60)):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = get_haar_cascade().detectMultiScale(
        gray, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=min_size
    )
    return list(faces)


def crop_face(frame, box, padding=20):
    h, w = frame.shape[:2]
    x, y, bw, bh = box
    x1 = max(0, x - padding)
    y1 = max(0, y - padding)
    x2 = min(w, x + bw + padding)
    y2 = min(h, y + bh + padding)
    return frame[y1:y2, x1:x2].copy()


def make_age_gender_blob(face_bgr):
    return cv2.dnn.blobFromImage(
        face_bgr, scalefactor=1.0, size=(227, 227), mean=MEAN_VALUES, swapRB=False
    )


def required_caffe_files():
    return {
        "age_proto": MODEL_DIR / "age_deploy.prototxt",
        "age_model": MODEL_DIR / "age_net.caffemodel",
        "gender_proto": MODEL_DIR / "gender_deploy.prototxt",
        "gender_model": MODEL_DIR / "gender_net.caffemodel",
    }


def check_caffe_files():
    files = required_caffe_files()
    missing = [str(p) for p in files.values() if not p.exists()]
    if missing:
        msg = "\n".join(missing)
        raise FileNotFoundError(
            "Arquivos Caffe nao encontrados. Coloque estes arquivos em models/opencv_age_gender:\n"
            f"{msg}\n\n"
            "Arquivos esperados: age_deploy.prototxt, age_net.caffemodel, "
            "gender_deploy.prototxt, gender_net.caffemodel."
        )
    return files


def load_caffe_age_gender():
    files = check_caffe_files()
    age_net = cv2.dnn.readNet(str(files["age_model"]), str(files["age_proto"]))
    gender_net = cv2.dnn.readNet(str(files["gender_model"]), str(files["gender_proto"]))
    return age_net, gender_net


def predict_age_gender(face_bgr, age_net, gender_net):
    blob = make_age_gender_blob(face_bgr)
    gender_net.setInput(blob)
    gender_pred = gender_net.forward()[0]
    gender_idx = int(np.argmax(gender_pred))

    age_net.setInput(blob)
    age_pred = age_net.forward()[0]
    age_idx = int(np.argmax(age_pred))

    return Prediction(
        gender=GENDER_LABELS[gender_idx],
        gender_conf=float(gender_pred[gender_idx]),
        age=AGE_BUCKETS[age_idx],
        age_conf=float(age_pred[age_idx]),
    )


def draw_label(frame, box, text, color=(0, 255, 0)):
    x, y, w, h = box
    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
    y_text = max(25, y - 10)
    cv2.putText(frame, text, (x, y_text), cv2.FONT_HERSHEY_SIMPLEX, 0.65, color, 2)
    return frame


def list_images(folder: str | Path):
    folder = Path(folder)
    exts = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
    return sorted([p for p in folder.rglob("*") if p.suffix.lower() in exts])


def time_call(fn, *args, repeat=20, warmup=3, **kwargs):
    for _ in range(warmup):
        fn(*args, **kwargs)
    t0 = time.perf_counter()
    for _ in range(repeat):
        fn(*args, **kwargs)
    return (time.perf_counter() - t0) / repeat
