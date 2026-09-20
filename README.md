# 👁️ Aulas e Práticas de Visão Computacional

Repositório estruturado contendo todos os materiais de aula, códigos de exemplo, atividades práticas e pipelines completos da disciplina de Visão Computacional.

---

## 🗂️ Estrutura do Repositório

O conteúdo está organizado sequencialmente em módulos temáticos, abrangendo desde os fundamentos de processamento de imagens até Deep Learning avançado:

| Módulo | Tema Principal | Descrição Resumida | Qtd. Scripts |
| :--- | :--- | :--- | :---: |
| **[`01_introducao_e_fundamentos_opencv`](01_introducao_e_fundamentos_opencv/)** | Fundamentos OpenCV & Câmera | Captura de vídeo/webcam, FPS, espaços de cor (HSV/LAB), filtros (Sharpen, Unsharp), limiarização Otsu e contornos Canny. Inclui `.docx` originais e `.py` extraídos. | 19 scripts |
| **[`02_fundamentos_convolucao`](02_fundamentos_convolucao/)** | Convolução & Filtros Manuais | Matriz como imagem, canais RGB, convolução manual passo a passo, Sobel, Blur, Sharpen, Stride, Padding, Múltiplos Filtros, ReLU e Max Pooling. | 14 scripts |
| **[`03_tensores_tensorflow`](03_tensores_tensorflow/)** | Tensores com TensorFlow | Manipulação de tensores (escalar, vetor, matriz), pixels RGB, batches/lotes, normalização, redimensionamento, convolução com Keras e pipeline `tf.data`. | 12 scripts |
| **[`04_visao_estereo_e_segmentacao_hsv`](04_visao_estereo_e_segmentacao_hsv/)** | Visão Estéreo & HSV | Inspeção de pares estéreo, mapas de disparidade (StereoBM e StereoSGBM), segmentação por cor HSV, operações morfológicas e integração ROI + profundidade. | 11 scripts |
| **[`05_deteccao_haar_e_reconhecimento_facial`](05_deteccao_haar_e_reconhecimento_facial/)** | Haar Cascade & Face | Detecção facial com Haar Cascades, extração de ROI 48x48, cadastro de identidades, reconhecimento em tempo real, varredura de tolerância e benchmark embarcado. | 11 scripts |
| **[`06_pontos_chave_e_homografia`](06_pontos_chave_e_homografia/)** | Keypoints & Homografia | Detectores/Descritores SIFT, ORB e AKAZE, matching com BFMatcher e FLANN (Lowe's Ratio Test), estimativa de Homografia com RANSAC e rastreamento visual. | 13 scripts |
| **[`07_hog_svm_deteccao_pedestres`](07_hog_svm_deteccao_pedestres/)** | HOG + SVM | Extração de features HOG (Histogram of Oriented Gradients), treinamento de classificador SVM linear, dataset sintético, janela deslizante e modelo treinado (.joblib). | 5 scripts + modelo |
| **[`08_rastreamento_de_objetos`](08_rastreamento_de_objetos/)** | Rastreamento em Vídeo | Subtração de fundo (MOG2 e KNN), CamShift com histograma de cor, Filtro de Kalman para previsão de trajetória, exportação de métricas em CSV e plots de trajetória. | 11 scripts + vídeo |
| **[`09_redes_neurais_e_cnn_basica`](09_redes_neurais_e_cnn_basica/)** | Redes Neurais & CNNs | CNN básica para MNIST, visualização de kernels aprendidos e feature maps, classificação CIFAR-10, Transfer Learning com MobileNet e conceitos de detecção. | 6 scripts |
| **[`10_analise_facial_caffe_utkface`](10_analise_facial_caffe_utkface/)** | Caffe, UTKFace & MobileNetV2 | Pipeline completo de análise facial: modelos Caffe pré-treinados (idade e gênero), dataset UTKFace, fine-tuning com MobileNetV2, matriz de confusão e conversão para TFLite. | 35 scripts |
| **[`11_visao_computacional_coletanea_geral`](11_visao_computacional_coletanea_geral/)** | Coletânea Abrangente | 28 exemplos ponta a ponta integrando processamento clássico, estereoscopia, LBPH, embeddings faciais, SIFT/ORB, CNNs, Data Augmentation e pipeline webcam em tempo real. | 28 scripts |
| **[`12_opencv_dnn_e_pipeline_integrativo`](12_opencv_dnn_e_pipeline_integrativo/)** | OpenCV DNN & Pipeline Integrativo | Classificação com OpenCV DNN (MobileNetV2, GoogLeNet, SqueezeNet), comparação com Keras, latência/memória, calibração/undistort, HSV, ORB, HOG/Haar e pipeline completo encadeado. | 32 scripts |
| **[`13_yolo_ssd_e_rastreamento`](13_yolo_ssd_e_rastreamento/)** | YOLO, SSD & Rastreamento com ID | Detecção em tempo real com YOLOv4-tiny, YOLOv8n e SSD MobileNetV2 via OpenCV DNN/Ultralytics, NMS, tracking por IoU, linhas virtuais de contagem, switches de ID e ética. | 38 scripts |
| **[`14_exemplo4_classificacao_facial`](14_exemplo4_classificacao_facial/)** | Módulo Complementar Faces | Exemplos e utilitários complementares de verificação de ambiente, localização de Haar Cascades e funções para análise facial (`face_utils.py`, `tf_utils.py`). | 7 scripts/utils |
| **[`exercicios_praticos_anteriores`](exercicios_praticos_anteriores/)** | Atividades Práticas & Fixação | Exercícios resolvidos e scripts de apoio organizados por categoria (Pré-processamento, Contornos, Redes Neurais/MNIST, Haar/Faces). | 53 scripts |

---

## 🚀 Instalação do Ambiente

Recomenda-se utilizar um ambiente virtual Python (versão 3.10, 3.11 ou 3.12):

```bash
# 1. Crie e ative o ambiente virtual
python -m venv venv
# No Windows PowerShell:
.\venv\Scripts\Activate.ps1
# No Linux/macOS:
source venv/bin/activate

# 2. Instale as dependências
pip install -r requirements.txt
```

---

## 📋 Detalhamento dos Módulos

### 1. `01_introducao_e_fundamentos_opencv`
- **00 a 07**: Verificação do ambiente, leitura/exibição com NumPy, geração de vídeo sintético, captura com webcam, cálculo de FPS com `cv2.getTickCount()`, conversão em escala de cinza e pipeline de frame.
- **09 a 19**: Espaços de cor HSV e LAB, saturação programática, filtros de sharpening manual via `cv2.filter2D`, unsharp masking com variância do Laplaciano, binarização global e de Otsu, detecção de bordas Canny e contornos classificados por área.
- **`docs/`**: Documentos originais fornecidos pelo professor em `.docx`.

### 2. `02_fundamentos_convolucao`
- Convolução 2D implementada do zero: percorrendo pixels com loops para entender a matemática matricial.
- Filtros clássicos de borda vertical, horizontal e Sobel.
- Efeitos de Blur (média) e Sharpen.
- Hiperparâmetros de convolução: `stride` (passo) e `padding` (preenchimento).
- Aplicação de múltiplos filtros simultâneos, ativação não linear **ReLU** e operação de redução **Max Pooling**.

### 3. `03_tensores_tensorflow`
- Estruturas fundamentais de tensores no TensorFlow.
- Manipulação de canais e dimensões de lote (`batch dimension`).
- Pré-processamento: normalização para `[0, 1]`, redimensionamento e conversão de cores.
- Convoluções 2D utilizando `tf.keras.layers.Conv2D`.
- Pipelines assíncronos e performáticos com `tf.data.Dataset`.

### 4. `04_visao_estereo_e_segmentacao_hsv`
- Cálculo de mapa de disparidade a partir de par estéreo (câmera esquerda e direita) usando `StereoBM` e `StereoSGBM`.
- Segmentação cromática no espaço HSV com limiares interativos.
- Filtros morfológicos (abertura e fechamento) para eliminação de ruídos.
- Extração de ROIs e integração da profundidade estéreo sobre objetos segmentados.

### 5. `05_deteccao_haar_e_reconhecimento_facial`
- Carregamento de classificadores em cascata XML (`haarcascade_frontalface_default.xml`).
- Ajuste e comparação de parâmetros: `scaleFactor` e `minNeighbors`.
- Detecção em fotos estáticas e fluxo contínuo de webcam.
- Normalização de recortes faciais para resolução padrão (ex: 48x48).
- Cadastro de banco de faces e reconhecimento em tempo real com teste de benchmark de latência.

### 6. `06_pontos_chave_e_homografia`
- Extração de pontos-chave e descritores invariantes com **SIFT**, **ORB** e **AKAZE**.
- Comparação de performance e robustez contra rotação, escala e iluminação.
- Estratégias de casamento de descritores: Força Bruta (`cv2.BFMatcher`) com cross-check e indexação rápida com `cv2.FlannBasedMatcher` aplicando o teste de razão de Lowe.
- Cálculo da matriz de **Homografia** com eliminação de outliers via **RANSAC**.
- Localização e projeção da caixa delimitadora do objeto em tempo real.

### 7. `07_hog_svm_deteccao_pedestres`
- Extração de características HOG (`cv2.HOGDescriptor`).
- Detecção de pessoas com o detector padrão pré-treinado do OpenCV.
- Pipeline de treinamento customizado: preparação de dataset (positivo e negativo), treino de classificador linear SVM com `scikit-learn` e exportação do modelo `.joblib`.
- Aplicação de Janela Deslizante (`Sliding Window`) e Supressão de Não-Máximos (NMS).

### 8. `08_rastreamento_de_objetos`
- Subtração de fundo adaptativa utilizando Gaussian Mixture Models (`MOG2`) e K-Nearest Neighbors (`KNN`).
- Rastreamento por cor e densidade de probabilidade com o algoritmo **CamShift**.
- Fusão sensorial e predição linear de estados com o **Filtro de Kalman**.
- Geração de vídeo sintético de testes, telemetria e exportação das trajetórias em arquivos CSV para geração de gráficos.

### 9. `09_redes_neurais_e_cnn_basica`
- Criação e treinamento de CNN clássica para o dataset MNIST de dígitos manuscritos.
- Técnicas de interpretabilidade: visualização dos pesos dos filtros convolucionais e extração dos mapas de ativação (feature maps).
- Classificação multiclasse de imagens no dataset CIFAR-10.
- Transfer Learning básico utilizando a arquitetura MobileNet.

### 10. `10_analise_facial_caffe_utkface`
- Inferência com redes pré-treinadas em formato Caffe (`deploy.prototxt` + `.caffemodel`) para estimativa de idade e gênero.
- Leitura, parse e organização das anotações do dataset **UTKFace**.
- Construção de pipeline com `tf.data` e Transfer Learning com **MobileNetV2** (treinamento de cabeça densa).
- Avaliação de métricas, curvas de perda/acurácia, matriz de confusão e benchmark de inferência (FPS/latência).
- Conversão e quantização do modelo treinado para **TensorFlow Lite (.tflite)** voltado a sistemas embarcados.

### 11. `11_visao_computacional_coletanea_geral`
- Coleção didática completa de 28 scripts cobrindo todo o pipeline de visão computacional:
  - Criação de cenários sintéticos e ROIs;
  - Segmentação HSV, Otsu e morfologia matemática;
  - Algoritmo GrabCut;
  - Estereoscopia e conversão para profundidade métrica ($Z = \frac{f \cdot B}{d}$);
  - Reconhecimento facial com **LBPH** (`cv2.face.LBPHFaceRecognizer`) e embeddings profundos;
  - Descritores locais, matching e recuperação de imagens (CBIR);
  - Comparação MLP vs CNN no Fashion-MNIST, Data Augmentation e Callbacks;
  - Extração de features com projeção 2D (PCA);
  - Pipeline integrado em tempo real combinando segmentação OpenCV com classificação CNN Keras.

### 12. `12_opencv_dnn_e_pipeline_integrativo`
- 32 scripts cobrindo o uso do módulo `cv2.dnn` e integração completa:
  - Criação de frames sintéticos e testes de `cv2.dnn.blobFromImage`;
  - Download de labels ImageNet e inferência com MobileNetV2, GoogLeNet e SqueezeNet;
  - Conversão de Keras para TFLite e carregamento no OpenCV DNN;
  - Extração e sobreposição de top-3 classes com barra de confiança;
  - Medição rigorosa de latência (ms), consumo de memória (MB) e acurácia Top-1 (OpenCV vs Keras);
  - Pipeline integrativo ponta a ponta: calibração/undistort → segmentação por cor HSV → extração de features ORB → detector HOG/Haar → classificação da ROI com OpenCV DNN.

### 13. `13_yolo_ssd_e_rastreamento`
- 38 scripts cobrindo detecção em tempo real e tracking com persistência:
  - Leitura de vídeo, anotação de bounding boxes e medição de FPS/latência;
  - Aplicação de Non-Maximum Suppression (NMS) e filtragem por limiares de confiança;
  - Detecção com **YOLOv8** (Ultralytics e OpenCV ONNX), **YOLOv4-tiny** e **SSD MobileNetV2** via OpenCV DNN;
  - Comparação de tamanho de arquivos em disco, estimativa de parâmetros e tabelas de benchmark;
  - Rastreamento de objetos por **IoU (Intersection over Union)** com IDs persistentes;
  - Desenho de trilhas temporais (últimos 30 frames), linha virtual de entrada/saída para contagem cumulativa e medição de taxa de ID switches por minuto;
  - Relatório técnico sobre ética e impactos de sistemas de contagem e vigilância urbana com drones.

### 14. `14_exemplo4_classificacao_facial`
- Módulo complementar com utilitários e exemplos de verificação de ambiente, localização de cascatas Haar e funções utilitárias para manipulação do dataset UTKFace e redes MobileNetV2 (`face_utils.py` e `tf_utils.py`).

---

## 📁 Pastas de Apoio
- **`data/`**: Imagens e amostras de teste (ex: `pessoa.jpg`, etc.).
- **`modelos/`**: Modelos treinados salvos (`lbph.yml`, `lbph_rotulos.json`, etc.).
- **`resultados/`**: Gráficos de treinamento gerados, matrizes de confusão e arquivos de saída.
- **`utils/`**: Módulos utilitários compartilhados (`face_utils.py`, `tf_utils.py`).
