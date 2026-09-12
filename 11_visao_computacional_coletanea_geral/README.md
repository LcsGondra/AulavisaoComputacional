# Modulo 11: Coletanea Geral de Visao Computacional

Colecao abrangente de 28 scripts estruturados cobrindo desde a visao computacional tradicional ate Deep Learning.

## Conteudo dos Scripts
- **00 a 06**: Ambiente, imagens sinteticas, ROIs, segmentacao HSV, limiarizacao de Otsu, contornos morfologicos e segmentacao com GrabCut.
- **07 a 09**: Par estereo sintetico, mapa de disparidade com StereoSGBM e conversao de disparidade em profundidade metrica (Z = f * B / d).
- **10 a 15**: Deteccao facial Haar (imagem e webcam), coleta de faces para treino, reconhecimento facial com algoritmo LBPH (`cv2.face.LBPHFaceRecognizer`) e reconhecimento por embeddings faciais (`face_recognition`).
- **16 a 21**: Pontos-chave SIFT/ORB, ratio test de Lowe, Homografia com RANSAC, demonstracao de SURF e recuperacao de imagens por similaridade de conteudo (CBIR).
- **22 a 27**: Comparacao MLP vs CNN no Fashion-MNIST, aumento de dados (Data Augmentation) e Callbacks, extracao de features e projecao 2D com PCA, Transfer Learning com MobileNetV2 e pipeline integrado em tempo real combinando OpenCV e Keras na webcam.
