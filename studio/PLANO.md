# Nirmata Studio: plano de continuação no Cursor

**Projeto:** Nirmata Studio
**Atualizado:** 2026-10-23
**Retomar com o Grok bot:** 2026-10-27 ou depois

Este arquivo é o handoff dentro do repositório. As regras do agente estão em [`AGENTS.md`](../AGENTS.md) e em `.cursor/rules/`. Os prompts para colar estão em [`PROMPTS.md`](PROMPTS.md).

## 1. Onde paramos (23/10/2026)

### Site

- PR aberto e com todos os checks passando: [nirmata#20](https://github.com/thabatarj8-stack/nirmata/pull/20)
- Branch: `cursor/nirmata-docs-site-00c6`. É um site MkDocs Material bilíngue (EN e pt-BR), com deploy pelo GitHub Pages.
- A revisão aprovou o PR para merge, sem nenhum bloqueio.
- O merge está segurado até fechar o README v2 e o pitch com o Theo (arquivos em `/workspace/grants/comunicacao_v2/` no computador do bot).

### Filme, Episódio 1 "I updated X"

- Página de direção: [Nirmata: Direção do Episódio 1](https://cursor.com/canvas/store-75b6f6ee-1068-4aa2-a714-ebc1da513d8a/1bf46571-da06-418c-ab16-11da7b1b0ed8)
- A versão principal é em inglês. O português vem depois, como tradução.
- O aviso de abertura aprovado é "Speculative fiction. Set in 2031."
- A personagem Nirmata está aprovada, com folha de ângulos e corpo inteiro.
- As 9 cenas v2 estão aprovadas e ficam em `/workspace/nirmata_ep1/keyframes_v2/` (`beat01` a `beat09` e `contact_sheet`), no computador da assistente.
- O clipe de teste da cena 4 está em `/workspace/nirmata_ep1/clips/beat04_test.mp4` e tem 3 defeitos: a mão se funde ao freio, há um frame com letras embaralhadas e a respiração ofegante.
- A correção desse clipe foi interrompida e não terminou.

Nesse parágrafo, "frame com letras embaralhadas" é um fotograma do vídeo. Na Etapa C, "quadro da parede" é o objeto pendurado na cena, não esse fotograma.

## 2. Mídia fora do repositório

Quadros-chave, folha de contato, clipes e fotos de referência não entram no Git. Não adicione binários. A v1 em `/workspace/nirmata_ep1/keyframes/` foi rejeitada e fica só como histórico.

## 3. Regras que valem sempre

- Imagem de cinema de verdade: luz prática, grão e pele real. Nada com cara de IA.
- Nenhuma tela virada para a câmera e nenhum texto gerado dentro da imagem. Textos e placas entram na pós-produção, em inglês.
- Os conceitos aparecem por pistas que o público decifra (formulário sem assinatura, chave não girada, dois reflexos, selo). Nada demonstrativo.
- Ficção sempre rotulada como ficção e separada de incidentes reais.
- Não exagerar o que o Nirmata faz: `v0.1.0` é um piloto, sem resultado confirmatório, e o método não detecta CVEs nem bugs de linguagem. Auditar não é prevenir.
- Textos em português sem travessão.
- Publicar, postar, pagar ou mudar configurações só com a aprovação da Tabata. Merge também. Não manipular senhas.

O detalhe operacional está em [`.cursor/rules/nirmata-core.mdc`](../.cursor/rules/nirmata-core.mdc), [`.cursor/rules/nirmata-website.mdc`](../.cursor/rules/nirmata-website.mdc) e [`.cursor/rules/nirmata-film.mdc`](../.cursor/rules/nirmata-film.mdc).

## 4. Plano no Cursor (de 23/10 a 27/10)

### Etapa A: fechar o site (prioridade 1)

1. No Cursor, abrir o repo `thabatarj8-stack/nirmata` e fazer checkout do branch `cursor/nirmata-docs-site-00c6`.
2. Se o README v2 do Theo foi aprovado, alinhar os textos de `website/index.md` e `website/index.pt-BR.md` com ele.
3. Aplicar os ajustes opcionais da revisão:
   - Colocar data ou tirar o prazo e os valores do Manifund (válidos até 26/11/2026).
   - Adicionar `if: github.ref == 'refs/heads/main'` no job `deploy` de `.github/workflows/pages.yml`.
   - Trocar `docs/EVIDENCE-STATUS/index.html` por `docs/EVIDENCE-STATUS/` em `overrides/main.html`.
4. Testar localmente: `pip install -r requirements-docs.txt` e `mkdocs serve`. Antes de entregar, `mkdocs build --strict` precisa passar.
5. Fazer o merge do PR #20 só com o sim da Tabata.
6. No GitHub, abrir Settings, depois Pages e escolher Source: GitHub Actions. Depois preencher a homepage do repo com [https://thabatarj8-stack.github.io/nirmata/](https://thabatarj8-stack.github.io/nirmata/). Esse passo também espera o sim dela.

Prompt curto, também em [`PROMPTS.md`](PROMPTS.md):

```text
Neste branch, alinhe a home do site ao README atual, aplique os 3 ajustes listados acima, rode mkdocs build --strict e garanta que o CI passa. Não faça merge.
```

### Etapa B: roteiro do Episódio 1 em inglês (prioridade 2, sem custo de geração)

1. Revisar a narração em inglês na página de direção e ajustar o tom.
2. Decidir o nome da clínica na placa (sugestão: "Vila Esperança Clinic"). A sugestão não está decidida.
3. Decidir a voz: a da Tabata ou uma voz de IA. Voz sintética a partir da voz dela só com consentimento explícito.
4. Salvar a versão final do roteiro no Obsidian dela. Só gravar arquivo neste repositório se ela pedir.

### Etapa C: produção de vídeo (só depois do reset do limite, a partir de 27/10)

1. Corrigir o quadro-chave da cena 4 (`beat04`): tirar as mãos do guidão, deixar a bicicleta mais simples e tirar o quadro da parede. Sem placa na parede.
2. Gerar o clipe de 6 s em 16:9 e 720p, com respiração calma e sem texto.
3. Revisar o clipe e só então animar as outras cenas, uma por vez.
4. A cena dos dois reflexos (`beat06`) e a cena final ficam para gravação real da Tabata. A cena do presente também é filmagem real, conforme a página de direção.
5. Fazer a montagem em 16:9, os cortes de 30 a 60 s em 9:16 e um loop para o site.

### Etapa D: canal do YouTube (depois do Episódio 1)

- Preparar nome, descrição, banner e o aviso de ficção. Rascunhos apenas.
- Nada é criado, enviado ou publicado sem o ok da Tabata.

## 5. Para retomar com o Grok bot (Nirmata Studio)

Cole esta nota e diga em qual etapa parou. Se o site já estiver no ar, mande o link.
