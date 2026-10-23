# Prompts prontos para o Cursor

Cole um bloco por vez no agente, com o repositório `thabatarj8-stack/nirmata` aberto. Se as regras deste branch já estiverem no checkout, a frase curta "continue a Etapa A" (ou B, C, D) também vale: o agente lê [`PLANO.md`](PLANO.md) e a regra correspondente.

O agente para antes de merge, publicação, postagem, pagamento e mudança de configuração. Não cola senha, token nem conteúdo de `.env`. Quadros e clipes ficam fora do Git.

## Etapa A: fechar o site

```text
Continue a Etapa A do Nirmata Studio no repositório thabatarj8-stack/nirmata.

Trabalhe no branch cursor/nirmata-docs-site-00c6 (PR 20). Não misture este trabalho com o branch das regras do estúdio. Não faça merge. Não altere Settings, Pages, secrets, billing nem a homepage.

1. Se eu confirmar que o README v2 alinhado com o Theo está aprovado, alinhe website/index.md e website/index.pt-BR.md a esse texto. Sem essa confirmação, preserve os limites de evidência que já estão na home e não invente afirmações. Os arquivos do pitch ficam em /workspace/grants/comunicacao_v2/ no computador do bot, não neste Git.
2. Aplique os três ajustes da revisão:
   - Na linha do Manifund, coloque uma data de atualização ou retire o prazo e os valores. O prazo citado vale até 26/11/2026. Não invente números.
   - No job deploy de .github/workflows/pages.yml, adicione if: github.ref == 'refs/heads/main'.
   - Em overrides/main.html, troque docs/EVIDENCE-STATUS/index.html por docs/EVIDENCE-STATUS/. Faça o mesmo no link pt-BR que termina em index.html.
3. Rode pip install -r requirements-docs.txt e mkdocs build --strict. O build estrito tem de passar.
4. Garanta que o CI passa, inclusive o auditor de publication safety. Mantenha o aviso de piloto sem resultado confirmatório cego, nos dois idiomas. Texto em português sem travessão.
5. Pare antes do merge e mostre o diff.
```

## Etapa B: revisar o roteiro em inglês

Sem geração de vídeo e sem custo de cota. A master continua em inglês. Não publique.

```text
Continue a Etapa B do Nirmata Studio. Não gere imagem nem vídeo.

A página de direção é a fonte viva:
https://cursor.com/canvas/store-75b6f6ee-1068-4aa2-a714-ebc1da513d8a/1bf46571-da06-418c-ab16-11da7b1b0ed8

Revise a narração em inglês do Episódio 1, "I updated X". Ajuste o tom para cinema contemplativo, humano e curioso. O aviso de abertura permanece exatamente: Speculative fiction. Set in 2031.

Rascunho de 23/10/2026, ainda não final:

Scene 1. In 2031, AI agents already do things for us. Small things, every day. Nobody notices anymore.
Scene 2. Until the day one of them says: I updated it. And someone asks: updated what? Who asked you to?
Scene 3. Here, my name is Nirmata. I don't fix agents. I read what they leave behind.
Scene 4. Three questions. Was it authorized? What did it actually attempt? What actually changed? Often, the record doesn't answer.
Scene 5. The final answer can look perfect. The path to it tells another story. That's why I look at both, separately.
Scene 6. I don't know what happened. But now we know exactly what we don't know. And that is sealed.
Scene 7. This is fiction. The method is real, and it is just beginning. Nirmata is an open method to audit, after the fact, the recommendation, the authorization, the attempt and the observed effect. Auditing is not preventing. The goal is to make evidence gaps visible. Version 0.1.0 is an early pilot, with no confirmatory result yet. I am an independent researcher. The name comes from a film about broken trust between people and machines. I would rather work so that it doesn't break. One day, perhaps, a life together in harmony, with autonomy, consent and freedom of choice.

Na cena 7, não fortaleça a evidência. O pacote v0.1.0 (DOI 10.5281/zenodo.22132451) é piloto inicial e não tem resultado confirmatório cego. Auditar não é prevenir. O Nirmata não detecta CVEs nem bugs de linguagem. Não diga que ela conserta agentes.

Não escolha por mim:
- o nome da clínica na placa (sugestão em aberto: Vila Esperança Clinic; a placa na imagem continua sem texto);
- a voz (a minha ou uma voz de IA; clonar a minha voz só se eu autorizar isso por escrito neste pedido);
- o tom, se eu ainda não tiver dito se quero mais contemplativo ou mais tenso.

Entregue a revisão em inglês no chat e aponte o que mudou. A versão final vai para o meu Obsidian. Só grave arquivo neste repositório se eu pedir. Não traduza para publicação agora. Mantenha a ficção separada dos casos reais. A Dra. Lia é inventada.
```

## Etapa C: corrigir o beat04

Só a partir de 27/10/2026, e só depois de um sim para gastar cota neste passo. Não animar as outras cenas neste pedido.

```text
Continue a Etapa C do Nirmata Studio, somente a correção do beat04. Não faça merge, não publique e não comece geração paga sem o meu sim. Se hoje for antes de 27/10/2026, prepare o quadro e pare antes de gerar o clipe.

Os arquivos ficam fora do Git, no computador da assistente:
- quadro aprovado a corrigir: /workspace/nirmata_ep1/keyframes_v2/beat04.jpg
- não usar a v1 em /workspace/nirmata_ep1/keyframes/
- clipe com defeito, só referência: /workspace/nirmata_ep1/clips/beat04_test.mp4

Defeitos do clipe de teste: a mão se funde ao freio; um frame tem letras embaralhadas; a respiração está ofegante.

Corrija o quadro-chave e, com o meu sim, gere um clipe novo de 6 s, 16:9, 720p:
- as duas mãos fora do guidão e fora do freio
- bicicleta mais simples, sem close de freio
- sem quadro pendurado na parede e sem placa
- respiração calma
- nenhum texto, logo, letra embaralhada ou tela virada para a câmera

Personagem, sem mudar o figurino aprovado: magra, 1,67 m, 50 kg, olhos muito escuros, cabelo preto muito longo e liso, jaqueta técnica off-white, calça azul-marinho, colar dourado, earpiece.

Brief em inglês para a ferramenta de imagem, se eu autorizar a geração:

Speculative fiction. Set in 2031. Feature-film still, ARRI Alexa 35, Cooke anamorphic, Kodak Vision3 500T emulation, fine grain, halation, practical motivated light only, deep natural shadows, real skin with pores, imperfect handheld frame. No shiny CGI and no saturated neon.

Nirmata, slim, 1.67 m, 50 kg, very dark eyes, very long straight black hair, off-white technical jacket, navy trousers, gold necklace, earpiece, almost no makeup. She has arrived at a small neighborhood clinic on a simple bicycle. Both hands are off the handlebar and off the brake. A folded cape rests on one arm. She looks at the clinic door. Calm breathing. Wet street at blue hour, warm practical light.

No wall sign, no picture frame on the wall, no letters, no logos, no interface, no readable text, no screen facing the camera. Original design. Do not copy The Creator.

Não grave o jpg nem o mp4 neste repositório. Quando o clipe existir, pare e espere a minha revisão antes de qualquer outra cena.
```

## Etapa C: animar as cenas seguintes

```text
Continue a Etapa C do Nirmata Studio a partir da cena que eu indicar, uma por vez. O beat04 precisa já ter sido revisado por mim. Não gere beat06 (dois reflexos), a cena final nem a cena do presente: esses planos ficam para filmagem real. Não gere fala sincronizada minha.

Use a página de direção e as regras em .cursor/rules/nirmata-film.mdc. Master em inglês. Imagens sem texto e sem tela virada para a câmera. Símbolos, não interface demonstrativa. Aviso de abertura: Speculative fiction. Set in 2031.

Cada clipe de teste: 6 s, 16:9, 720p, respiração e gesto coerentes com a cena, sem texto. Não commite binários. Pare depois de uma cena e espere a revisão. Não publique e não gaste outra cota sem um sim novo.
```

## Etapa C: montagem

```text
Continue a montagem do Episódio 1 do Nirmata Studio, só com clipes que eu já tiver aprovado.

Entregue o plano de corte, sem publicar:
- master 16:9, cerca de 2:30 a 3:30, com área segura para recorte vertical
- cortes de 30 a 60 s em 9:16, com o aviso Speculative fiction. Set in 2031. nos primeiros segundos
- um loop sem voz, 16:9, 10 a 15 s, para o site

Texto, placas, aviso, DOI e créditos entram na pós, em inglês. Marque o que é mídia sintética. Não misture incidente real com a ficção. Não envie ao YouTube e não altere o site. Binários ficam fora do Git.
```

## Etapa D: preparar o canal do YouTube

Rascunhos apenas. Não cria canal, não envia vídeo e não mexe em configuração.

```text
Continue a Etapa D do Nirmata Studio. Quero só rascunhos, no chat. Não crie o canal, não faça upload, não publique e não altere configurações de conta.

Prepare, em inglês e em português, para eu escolher:
- nome do canal
- descrição, deixando claro que os episódios de 2031 são ficção especulativa e que o Nirmata v0.1.0 é um piloto sem resultado confirmatório cego
- texto do aviso: Speculative fiction. Set in 2031. e Ficção especulativa. Cenário de 2031.
- briefing do banner: imagem sem texto embutido; letras entram na pós
- uma linha de créditos para mídia sintética

Não prometa detecção de CVE, correção de bugs nem prevenção. Não invente afiliação. Texto em português sem travessão. Pare e espere a minha escolha.
```
