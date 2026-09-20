
"""Utilitarios para o Item B: MobileNetV2, UTKFace e metricas."""
from __future__ import annotations
from pathlib import Path
import time
import numpy as np


def parse_utkface_filename(path):
    """
    Formato comum do UTKFace: idade_genero_etnia_data.jpg.
    genero: 0 = masculino, 1 = feminino segundo a convencao do dataset.
    """
    stem = Path(path).stem
    parts = stem.split("_")
    if len(parts) < 2:
        raise ValueError(f"Nome nao segue o padrao UTKFace: {path}")
    age = int(parts[0])
    gender = int(parts[1])
    return age, gender


def collect_utkface_paths(root, limit=1000):
    root = Path(root)
    imgs = []
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        imgs.extend(root.rglob(ext))
    valid = []
    for p in sorted(imgs):
        try:
            parse_utkface_filename(p)
            valid.append(p)
        except Exception:
            pass
    if limit:
        valid = valid[:limit]
    return valid


def model_size_mb(path):
    return Path(path).stat().st_size / (1024 * 1024)


def measure_keras_latency_ms(model, sample, repeat=50, warmup=5):
    import numpy as np
    sample = np.asarray(sample)
    if sample.ndim == 3:
        sample = sample[None, ...]
    for _ in range(warmup):
        model.predict(sample, verbose=0)
    t0 = time.perf_counter()
    for _ in range(repeat):
        model.predict(sample, verbose=0)
    return (time.perf_counter() - t0) * 1000 / repeat


def build_mobilenetv2_gender(input_shape=(160, 160, 3), dropout=0.3):
    import tensorflow as tf
    base = tf.keras.applications.MobileNetV2(
        input_shape=input_shape, include_top=False, weights="imagenet"
    )
    base.trainable = False
    inputs = tf.keras.Input(shape=input_shape)
    x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
    x = base(x, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(dropout)(x)
    x = tf.keras.layers.Dense(128, activation="relu")(x)
    x = tf.keras.layers.Dropout(dropout)(x)
    outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
    model = tf.keras.Model(inputs, outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model
