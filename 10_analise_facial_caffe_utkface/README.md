# Modulo 10: Analise Facial Avancada (Caffe, UTKFace e MobileNetV2)

Pipeline completo para estimativa de idade, genero, fine-tuning e exportacao para TFLite.

## Estrutura dos Scripts (35 scripts)
- **01 a 07**: Preparacao de ambiente, estrutura de diretorios, deteccao facial Haar, recorte de ROIs e anotacao grafica.
- **08 a 17**: Modelos Caffe pre-treinados para idade e genero, geracao de blobs, inferencia em imagem, webcam e arquivos de video, medicao de FPS e logs em CSV.
- **18 a 23**: Dataset **UTKFace** (leitura de nomes de arquivos, dataframes pandas, divisao treino/validacao, pipeline `tf.data` e visualizacao de lotes).
- **24 a 31**: Fine-tuning da arquitetura MobileNetV2 (construcao da cabeca densa, treinamento por 10 epocas, plotagem de curvas de aprendizado, matriz de confusao e comparacao com o modelo Caffe).
- **32 a 35**: Pipelines integrados finais (Item A e Item B), analise de aspectos eticos em visao computacional e conversao quantizada para TensorFlow Lite (`.tflite`).
