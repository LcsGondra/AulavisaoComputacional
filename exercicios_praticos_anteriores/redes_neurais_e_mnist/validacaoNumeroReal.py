import argparse
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from mnist_utils import annotate_prediction, build_cnn, load_mnist, predict_real_digit

parser = argparse.ArgumentParser()
parser.add_argument("--imagem", default="dados/real_digits/9.png")
parser.add_argument("--modelo", default="resultados/cnn_mnist.keras")
args = parser.parse_args()

if Path(args.modelo).exists():
    model = tf.keras.models.load_model(args.modelo)
else:
    (x_train, y_train), _ = load_mnist(flatten=False)
    model = build_cnn()
    model.fit(x_train, y_train, validation_split=0.1, epochs=3, batch_size=128)
    Path(args.modelo).parent.mkdir(exist_ok=True)
    model.save(args.modelo)

result = predict_real_digit(model, args.imagem)
annotated = annotate_prediction(
    result["original"], result["prediction"], result["confidence"]
)

plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("Predição sobre imagem real")
plt.show()

print(f"Dígito predito: {result['prediction']} | confiança: {result['confidence']:.2%}")
