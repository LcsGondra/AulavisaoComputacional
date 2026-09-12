import cv2
from pathlib import Path

path = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"
print("Arquivo Haar Cascade:", path)
print("Existe?", path.exists())
