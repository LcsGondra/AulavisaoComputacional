# Modulo 06: Pontos-Chave, Descritores e Homografia

Deteccao de pontos de interesse (SIFT, ORB, AKAZE), casamento de descritores e calculo de Homografia com RANSAC.

## Conteudo dos Scripts
- `00_validar_ambiente.py`: Verificacao do OpenCV Contrib e suporte a descritores.
- `01_gerar_imagens_teste.py`: Criacao de imagens de teste com transformacoes sinteticas.
- `02_keypoints_sift.py`: Deteccao e extracao de descritores SIFT (invariante a escala e rotacao).
- `03_keypoints_orb.py`: Deteccao rapida com ORB (binario).
- `04_keypoints_akaze.py`: Deteccao e extracao com AKAZE.
- `05_item_a_comparar_descritores.py`: Comparativo de numero de pontos e tempo entre SIFT, ORB e AKAZE.
- `06_bfmatcher_crosscheck.py`: Casamento por Forca Bruta com verificacao cruzada.
- `07_flann_lowe.py`: Casamento rapido FLANN com teste de razao de Lowe.
- `08_homografia_ransac.py`: Estimativa da matriz de Homografia usando RANSAC.
- `09_item_b_completo.py`: Pipeline integrado de busca e projecao de objeto na cena.
- `10_comparar_matching_tres_metodos.py`: Comparacao de precisao dos matchers.
- `11_robustez_rotacao_escala_luz.py`: Testes de estresse com rotacao, escala e ruido luminoso.
- `12_localizacao_visual_video.py`: Rastreamento e localizacao do objeto no feed de video.
