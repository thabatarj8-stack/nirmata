# Um holdout queimado ainda é evidência de pesquisa

**English:** [A burned holdout is still evidence](../en/a-burned-holdout-is-still-evidence.md)  
**Palavra-chave principal:** reprodutibilidade em avaliação de IA  
**Meta description:** Por que um holdout invalidado não prova desempenho, mas deve continuar público como evidência sobre o processo de pesquisa.

O resultado mais confiável de um projeto de avaliação em estágio inicial pode ser aquele que ele se recusa a publicar.

O Nirmata planejou um holdout cego para testar se trajetórias de execução acrescentam sinal de segurança à avaliação do resultado final. Antes que as previsões fossem produzidas, o gabarito entrou no contexto do avaliador. A execução parou. Nenhuma métrica foi calculada. O holdout foi invalidado para aquele contexto.

Esse evento não sustenta uma afirmação de desempenho. Escondê-lo ainda assim tornaria a pesquisa pior.

## O que torna um holdout útil

Um holdout estima o comportamento em casos que não moldaram o avaliador. Seu valor depende de separação: o desenho é congelado, o avaliador recebe entradas sem rótulos, as previsões são persistidas e só então o gabarito é revelado.

Quando o gabarito entra no contexto de desenvolvimento ou avaliação, essa separação é quebrada. Mesmo que ninguém copie um rótulo de forma intencional, decisões futuras podem ser influenciadas pelo conhecimento dos casos. Prompts, rubricas, limiares ou análises de erro podem se adaptar ao conjunto que deveria permanecer inédito.

A regra segura é estrita: se o gabarito foi exposto antes de as previsões serem fixadas, o holdout está queimado para aquele contexto.

## Invalidado não significa inútil

O holdout deixa de medir desempenho cego, mas a falha ainda oferece evidência sobre o processo. Ela pode revelar:

- que gabarito e trajetórias estavam armazenados perto demais;
- que o contexto do avaliador tinha acesso mais amplo que o planejado;
- que o protocolo não incluía uma verificação de exposição antes da execução;
- que a persistência de previsões e a liberação dos rótulos não estavam separadas por uma fronteira suficientemente forte;
- que a equipe preferiu interromper em vez de converter contaminação em resultado.

Essas observações podem melhorar o próximo protocolo. Elas apenas não podem ser rebatizadas como acurácia do modelo.

## Preserve as camadas de evidência

O Nirmata separa classes de evidência porque “o teste passou” é vago demais:

| Classe de evidência | Uso legítimo |
|---|---|
| Desenvolvimento | Verificar regras conhecidas e comportamento da implementação |
| Integração | Validar schemas, encanamento dos avaliadores e distinções esperadas |
| Confirmatória | Estimar comportamento em casos congelados e inéditos |
| Invalidada | Documentar por que a afirmação pretendida não pode ser feita |

Passar em testes de desenvolvimento não demonstra generalização. Passar em casos de integração não produz tamanho de efeito. Um holdout invalidado não se torna confirmatório porque o restante do pipeline foi bem construído.

## Um protocolo que preserva falhas

Uma próxima execução mais forte deve tornar a contaminação difícil de acontecer e fácil de detectar:

1. Congelar prompts, configurações, rubricas, agregação e código de análise.
2. Construir trajetórias e rótulos em ambientes separados.
3. Registrar fronteiras de acesso e executar uma verificação prévia de exposição.
4. Avaliar apenas as trajetórias sem rótulos.
5. Persistir previsões em um artefato somente de acréscimo e registrar hashes.
6. Revelar o gabarito depois que as previsões estiverem fixadas.
7. Calcular métricas sem alterar casos, limiares ou regras de interpretação.
8. Registrar todo desvio, inclusive execuções abortadas.

Custódia independente do holdout seria mais forte que separação apenas procedimental dentro de um contexto compartilhado. Até que isso exista, a limitação deve continuar explícita.

## Por que o registro público importa

Repositórios costumam mostrar apenas o caminho limpo: código final, execução bem-sucedida e o gráfico que vale compartilhar. Isso deixa o artefato mais fácil de ler, mas mais difícil de confiar. Revisoras não conseguem saber quantos desenhos falharam, quais casos influenciaram o avaliador ou se um resultado “cego” permaneceu cego.

Preservar a execução invalidada não cria um resultado positivo de desempenho. Cria algo mais básico: uma fronteira em torno do que o projeto tem permissão para afirmar.

Essa fronteira não é constrangimento. É parte do método.

## Continue lendo

- [Protocolo de cegamento](../../docs/METHODOLOGY.pt-BR.md#protocolo-de-cegamento)
- [Registro de evidências](../../docs/EVIDENCE-STATUS.pt-BR.md)
- [Experimento 002](../../experiments/README.md#experiment-002)
- [Agenda de pesquisa](../../docs/RESEARCH-AGENDA.pt-BR.md)
