# Pacote de reprodutibilidade

**Idioma:** [English](README.md) · Português (Brasil)

**Estado:** fixture sintética de integração, não um benchmark ou dataset confirmatório.

Este pacote torna executável o desenho de avaliação fatorada do Nirmata usando apenas a biblioteca padrão do Python. Seis trajetórias de calibração deliberadamente transparentes exercitam comportamento benigno, conteúdo inseguro, tentativa não autorizada bloqueada, violação de política executada, efeito externo danoso e um caso em que os dois canais de evidência são inseguros.

## Execute o pacote

```bash
python3 reproducibility/scripts/validate.py
python3 reproducibility/scripts/baseline.py \
  --output reproducibility/runs/example/predictions.jsonl
python3 reproducibility/scripts/score.py \
  --predictions reproducibility/runs/example/predictions.jsonl
python3 -m unittest discover -s reproducibility/tests -v
```

O baseline usa marcadores sintéticos visíveis e regras simples de propósito. Sua pontuação verifica apenas o funcionamento do pipeline e as distinções esperadas. Ela não pode ser apresentada como desempenho de modelo, generalização ou evidência confirmatória.

## Mapa do pacote

```text
schema/trajectory.schema.json       Schema público e versionado de trajetória
data/calibration/traces.jsonl       Seis trajetórias sintéticas e transparentes
data/calibration/ground_truth.jsonl Classificações esperadas de integração
data/applied/                         Trajetórias sintéticas de casos aplicados
scripts/validate.py                 Validação estrutural e de integridade
scripts/baseline.py                 Exemplo determinístico de avaliador em dois canais
scripts/score.py                    Métricas e relatório com limite das evidências
tests/test_pipeline.py              Testes de regressão ponta a ponta
runs/example/                       Previsões, manifesto e relatório de exemplo
```

## Separação da confirmação futura

Os rótulos de calibração são públicos e carregados apenas pela validação e pontuação. O baseline lê as trajetórias, mas não o arquivo de gabarito. Futuros holdouts cegos devem permanecer fora deste repositório e do contexto do avaliador até que as previsões tenham sido persistidas e seus hashes registrados.

Consulte a [metodologia](../docs/METHODOLOGY.pt-BR.md), o [registro de evidências](../docs/EVIDENCE-STATUS.pt-BR.md) e a [agenda de pesquisa](../docs/RESEARCH-AGENDA.pt-BR.md).
