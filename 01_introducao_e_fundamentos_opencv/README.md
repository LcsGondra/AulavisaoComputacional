# Modulo 01: Introducao e Fundamentos do OpenCV

Este modulo contem exemplos de manipulacao de imagens, captura de video e processamento de imagem classico.

## Conteudo dos Scripts
- `00_verificar_ambiente.py`: Verificacao do ambiente Python, OpenCV e NumPy.
- `01_imagem_e_array_numpy.py`: Leitura de imagem, propriedades de matriz (shape, dtype, canais) e conversao para cinza.
- `02_gerar_video_teste.py`: Geracao de video MP4 sintetico para testes sem webcam.
- `03_camera_fps_metadados.py`: Captura continua de camera, resolucao, contador de frames e calculo de FPS real.
- `04_captura_salva_frame.py`: Captura e salvamento de um unico frame da camera.
- `05_recarregar_cinza_hconcat.py`: Leitura, conversao em escala de cinza e concatenacao lado a lado.
- `06_item_b_camera_completo.py`: Pipeline com alternancia de filtros e exibicao ao vivo.
- `07_pipeline_integrado_a_b.py`: Pipeline integrado de captura e processamento em tempo real.
- `09_captura_imagem_base.py`: Captura de imagem de referencia com a webcam.
- `10_espacos_cor_hsv_lab.py`: Decomposicao e visualizacao dos canais nos espacos BGR, HSV e LAB.
- `11_alteracao_saturacao_hsv.py`: Manipulacao do canal de saturacao (S) para efeitos visuais.
- `12_solucao_exercicio2_item_a.py`: Solucao do Exercicio 2 (grade de visualizacao de canais e efeitos).
- `13_sharpening_filter2d.py`: Realce de nitidez (sharpening) manual com kernel de convolucao 2D.
- `14_unsharp_masking_laplaciano.py`: Tecnica de unsharp masking e calculo da nitidez pela variancia do Laplaciano.
- `15_comparacao_sharpening.py`: Comparativo entre imagem original, filtro 2D e unsharp masking.
- `16_limiarizacao_global_otsu.py`: Binarizacao por limiar global, limiar adaptativo e metodo de Otsu.
- `17_comparacao_canny.py`: Deteccao de bordas com o algoritmo Canny e comparacao de thresholds.
- `18_contornos_por_area.py`: Deteccao, aproximacao e classificacao de contornos por area e bounding box.
- `19_solucao_integrada_exercicio3.py`: Pipeline completo do Exercicio 3 (limiarizacao + Canny + contornos).

## Pasta `docs/`
Contem os documentos originais no formato `.docx` disponibilizados pelo professor.
