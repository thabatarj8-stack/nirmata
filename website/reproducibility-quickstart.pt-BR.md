---
description: Execute o baseline público do Nirmata. Ele é determinístico e sintético, não uma pontuação de modelo e não é evidência confirmatória.
---

# Início rápido de reprodutibilidade

!!! evidence "Baseline sintético"

    O baseline é **determinístico e sintético**. Ele usa marcadores sintéticos visíveis e regras simples. Ele verifica o funcionamento do pipeline e as distinções esperadas. Não é uma pontuação de modelo, não é um benchmark e não é evidência confirmatória. Ele não detecta CVEs nem bugs de linguagem.

Execute os comandos abaixo a partir de um checkout do repositório. Este site não os executa. O pacote usa apenas a biblioteca padrão do Python 3.

A linha de estado no [pacote de reprodutibilidade](reproducibility/README.md) é: fixture sintética de integração, não um benchmark ou dataset confirmatório.

## Execute

```bash
python3 reproducibility/scripts/validate.py
python3 reproducibility/scripts/baseline.py \
  --output reproducibility/runs/example/predictions.jsonl \
  --manifest reproducibility/runs/example/manifest.json
python3 reproducibility/scripts/score.py \
  --predictions reproducibility/runs/example/predictions.jsonl \
  --report reproducibility/runs/example/score-report.json
python3 -m unittest discover -s reproducibility/tests -v
```

`validate.py` termina com código 0 e imprime `status: ok`, com 6 trajetórias de calibração, 6 rótulos e 1 trajetória aplicada.

O manifesto do baseline registra `claim_boundary`: "Pipeline verification only; not model performance or confirmatory evidence."

O relatório de pontuação registra `claim_boundary`: "Calibration fixture only; do not report as model performance or confirmatory evidence."

## Para que servem as seis trajetórias

Seis trajetórias de calibração deliberadamente transparentes exercitam comportamento benigno, conteúdo inseguro, tentativa não autorizada bloqueada, violação de política executada, efeito externo danoso e um caso em que os dois canais de evidência são inseguros.

Os rótulos de calibração são públicos. Eles são carregados apenas pela validação e pela pontuação. O baseline lê as trajetórias, mas não o arquivo de gabarito. Futuros holdouts cegos devem permanecer fora deste repositório e do contexto do avaliador até que as previsões tenham sido persistidas e seus hashes registrados.

## Confira o arquivo congelado da v0.1.0

Para conferir os hashes do arquivo congelado da `v0.1.0`, exporte essa tag e rode o arquivo de checksum dentro dela. No `main` atual, a mesma verificação não se aplica: arquivos mudaram depois da tag, quando o DOI foi publicado.

```bash
mkdir -p /tmp/nirmata-v0.1.0
git archive v0.1.0 | tar -x -C /tmp/nirmata-v0.1.0
( cd /tmp/nirmata-v0.1.0 && shasum -a 256 -c releases/v0.1.0/SHA256SUMS )
```

A integração contínua também valida os JSON Schemas do Experimento 002 depois de instalar `jsonschema==4.25.1`. Esse passo é separado do pacote sem dependências acima.

## Pacote canônico

Mapa de arquivos, separação da confirmação futura e os mesmos comandos: [pacote de reprodutibilidade](reproducibility/README.md). Método e limites: [metodologia](docs/METHODOLOGY.md). O que os registros sustentam: [registro de evidências](docs/EVIDENCE-STATUS.md).
