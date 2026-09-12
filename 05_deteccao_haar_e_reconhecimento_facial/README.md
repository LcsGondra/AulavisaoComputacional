# Modulo 05: Deteccao Haar e Reconhecimento Facial

Deteccao facial classica baseada em caracteristicas de Haar e reconhecimento facial.

## Conteudo dos Scripts
- `00_validar_ambiente.py`: Teste de integridade do ambiente e arquivos Haar.
- `01_carregar_haar.py`: Carregamento de classificadores Haar em XML.
- `02_detectar_imagem.py`: Deteccao de faces em imagem estatica.
- `03_extrair_roi_48x48.py`: Recorte e padronizacao das faces para 48x48 pixels.
- `04_item_a_tempo_real.py`: Deteccao facial em fluxo continuo de webcam com FPS.
- `05_comparar_parametros.py`: Comparacao de `scaleFactor` e `minNeighbors`.
- `06_cadastrar_identidades.py`: Coleta e cadastro de identidades para reconhecimento.
- `07_reconhecer_imagem.py`: Reconhecimento de identidades cadastradas em imagem.
- `08_item_b_video.py`: Reconhecimento facial em tempo real via webcam.
- `09_benchmark_embarcado.py`: Medicao de latencia e consumo de recursos.
- `10_varrer_tolerancia.py`: Analise de sensibilidade e taxa de acerto por limiar.
