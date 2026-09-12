# Modulo 04: Visao Estereo e Segmentacao HSV

Calculo de profundidade estereoscopica e segmentacao por cor no espaco HSV.

## Conteudo dos Scripts
- `01_inspecionar_par_estereo.py`: Carregamento e visualizacao das imagens esquerda e direita.
- `02_disparidade_bm.py`: Calculo do mapa de disparidade com `cv2.StereoBM`.
- `03_disparidade_sgbm.py`: Calculo do mapa de disparidade refinado com `cv2.StereoSGBM`.
- `04_item_a_completo.py`: Solucao integrada de inspecao e disparidade estereo.
- `05_explorar_hsv.py`: Exploracao interativa de faixas no espaco HSV.
- `06_segmentacao_hsv_imagem.py`: Aplicacao de mascara binaria por intervalo de cor.
- `07_morfologia_mascara.py`: Limpeza da mascara com operacoes morfologicas.
- `08_extrair_roi_imagem.py`: Obtencao de bounding boxes e recorte da Regiao de Interesse.
- `09_item_b_video.py`: Segmentacao e rastreamento em video continuo.
- `10_item_b_avancado.py`: Rastreamento com filtros avancados e metricas.
- `11_integrar_roi_e_disparidade.py`: Fusao da segmentacao com o mapa de profundidade estereo.
