# Distant Dream

Autor: GreenBoots  
Licença: GNU AGPLv3  
Copyright (C) 2026 GreenBoots

## Introdução

`distantdream` é um jogo do tipo [CLI](<https://en.wikipedia.org/wiki/Command-line_interface>) de experiência psicológica projetado para ser open-source, *hackável*, portátil (depende somente de funções próprias e embutidas em Python) e multiplataforma, desde que este dispositivo rode Python. Ou seja, você precisa usar a própria imaginação para compreender e, praticamente, *sentir* o jogo ao invés de consumir o conteúdo através de quaisquer algum outro meio como o visual e auditivo em si.

Por isto, intencionalmente, o jogo não possui gráficos (2D e nem 3D), músicas, sons e nem nada; somente texto, tal como um livro.  

### Fator Psicológico

O jogo toca justamente no desconforto do jogador, isto é, jogos sem materiais como músicas, sons e quaisquer outros meios que componham o ambiente do jogo tendem a causar mais desconforto por si devido ao costume de outros meios para compor um contexto/cenário e o cérebro humano não estar acostumado com o silêncio absoluto (nem todos vão sentir este desconforto).

Além disso, é possível que o jogo possa soar desconfortável para alguns públicos, porém, um desconforto leve é comum devido a experiência incomum e a expectativa. **Isto é para ser esperado**.

Portanto, se ao jogar o jogo, você sentir  **quaisquer sintomas psicológicos de forma intensas e fora do esperado como ansiedade intensa, estresse, angústia e/ou desconforto intenso, favor fechar o jogo imediatamente e evitar a visualização o material**.

## Hacking

Por conta do projeto ser open-source, você pode usar, reutilizar, acrescentar, modificar, recriar suas próprias histórias (não é o foco, mas pode ser muito interessante para você)... e uma infinidade de coisas.

O próprio design do projeto permite isto. Pois funciona da seguinte maneira:

```
distantdream (root dir)
├── distantdream.py
├── modules
│   ├── engine.py
│   └── utils.py
├── scenes (folder)
│   └── intro.py (start file)
└── settings.json
```

Como é observado, por padrão, o projeto vem com algumas pastas e arquivos. Darei-lhes uma explicação bem breve do que esperar e os propósitos de cada pasta e arquivo.

#### `distantdream.py`

É somente o "main" do projeto. É por onde o jogo chama os módulos e faz a execução de todo o projeto. Você pode executá-lo usando Python com:

- Windows

`py distantdream.py` ou `python distantdream.py`

- Linux/MacOS

`python distantdream.py` ou `./distantdream.py`

Depois o jogo abre-se normalmente, executando os módulos e fazendo todo o jogo funcionar.

#### `modules`

É a pasta onde os módulos do projeto ficam. Serve para justamente guardar tudo o que jogo precisa para funcionar. Por exemplo:

- `engine.py` é o motor do jogo. É ele quem lê o todo o conteúdo JSON da pasta `scenes`
- `utils.py` serve para armazenar funções como: "limpar tela", "efeito de digitação", etc. Praticamente utilitários internos mesmo.
