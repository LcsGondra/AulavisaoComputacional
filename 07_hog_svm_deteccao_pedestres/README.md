# Modulo 07: HOG + SVM para Deteccao de Pedestres

Extracao de Histogram of Oriented Gradients (HOG) combinada com Support Vector Machines (SVM).

## Conteudo
- `item_a_hog_pedestres.py`: Deteccao de pedestres utilizando o HOGDescriptor padrao do OpenCV.
- `gerar_dataset_sintetico_demo.py`: Geracao de amostras sinteticas positivas e negativas.
- `item_b_preparar_dataset.py`: Extracao de vetores de features HOG para treino.
- `item_b_treinar_svm.py`: Treinamento do classificador SVM e exportacao para `.joblib`.
- `item_b_janela_deslizante.py`: Deteccao em novas imagens com Sliding Window e Non-Maximum Suppression.
- `modelo_hog_svm.joblib`: Modelo SVM treinado pronto para inferencia.
