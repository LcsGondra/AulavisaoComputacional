# Modulo 08: Rastreamento de Objetos em Video

Algoritmos classicos de rastreamento visual, subtracao de fundo e fusao com Filtro de Kalman.

## Conteudo
- `00_check_environment.py`: Checagem das dependencias.
- `01_webcam_viewer_metadata.py`: Visualizador de webcam com exibicao de metadados.
- `02_background_mog2_basic.py`: Subtracao de fundo com Gaussian Mixture Models (MOG2).
- `03_background_knn_basic.py`: Subtracao de fundo com K-Nearest Neighbors (KNN).
- `04_compare_mog2_knn.py`: Comparativo lado a lado de MOG2 vs KNN.
- `05_camshift_roi.py`: Rastreamento de objeto por densidade de cor com CamShift.
- `06_camshift_kalman.py`: CamShift integrado com Filtro de Kalman para predicao linear de estados.
- `07_parameter_sweep_background.py`: Varredura de parametros de limiarizacao de fundo.
- `08_logging_to_csv.py`: Registro de metricas e coordenadas de rastreamento em CSV.
- `09_plot_trajectories_csv.py`: Plotagem das trajetorias e velocidades a partir do CSV gerado.
- `10_full_lab_pipeline.py`: Pipeline laboratorial completo integrando todas as etapas.
- `generate_synthetic_video.py`: Script para geracao do video de teste `synthetic_motion.mp4`.
- `data/synthetic_motion.mp4`: Video de teste pre-gerado.
