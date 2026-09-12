from pathlib import Path

for p in [
    "data/faces_teste",
    "data/utkface_sample",
    "models/opencv_age_gender",
    "resultados",
]:
    Path(p).mkdir(parents=True, exist_ok=True)
    print("OK:", p)
print(
    "Coloque imagens de teste em data/faces_teste e os modelos Caffe em models/opencv_age_gender."
)
