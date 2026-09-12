# Modulo 03: Tensores e Pipelines no TensorFlow

Fundamentos de manipulacao de dados visuais com tensores, tensores de lote e o modulo `tf.data`.

## Conteudo dos Scripts
- `01_compare_escalar_vetor_e_matriz.py`: Definicao e comparacao de escalares, vetores e matrizes de tensores.
- `02_represente_um_pixel_rgb.py`: Representacao de pixels em tensores uint8.
- `03_crie_uma_imagem_sintetica.py`: Construcao sintetica de matrizes de imagem com tensores.
- `04_carregue_uma_imagem_real.py`: Leitura e decodificacao de PNG/JPG com `tf.io`.
- `05_inspecione_shape_dtype_e_faixa.py`: Analise de dimensoes, tipo de dados e faixa dinamica.
- `06_acrescente_a_dimensao_de_lote.py`: Adicao de dimensao de batch (`[B, H, W, C]`).
- `07_converta_rgb_para_escala_de_cinza.py`: Conversao de espaco de cor com TensorFlow.
- `08_separe_e_recombine_os_canais.py`: Decomposicao e recombinacao de canais tensores.
- `09_normalize_os_pixels_para_0_1.py`: Normalizacao para float no intervalo `[0, 1]`.
- `10_redimensione_a_imagem.py`: Redimensionamento com interpolacao via `tf.image.resize`.
- `11_aplique_uma_convolucao.py`: Aplicacao de camadas `tf.keras.layers.Conv2D`.
- `12_monte_um_pipeline_tf_data.py`: Criacao de pipelines performaticos com `tf.data.Dataset`.
