
# Avaliação Final — Algoritmos Avançados em Python (UNIPLAN)

Bem-vindo(a)! Este repositório contém o projeto da **Avaliação Final** da disciplina **Algoritmos Avançados em Python** (Curso: **Análise e Desenvolvimento de Sistemas**, 1º e 2º semestres).  
**Professor:** Breno Abreu — **Instituição:** UNIPLAN.

> 🧭 **Contexto realista:** esta atividade simula o **onboarding de um desenvolvedor(a) júnior** em um projeto de software. Você deverá entender o código-base, implementar funções pontuais e contribuir via **GitHub Pull Request**, deixando registro individual da sua participação.

---

## 📦 Estrutura do projeto

```
prova_intro_arvores_grafos/
  arvore/
    app_tree.py         # UI Tkinter travada (não altere)
    tree_logic.py       # implemente a função navigate_tree()
  grafo/
    app_graph.py        # UI Tkinter travada (não altere)
    graph_logic.py      # implemente a função connected()
  run_tree.bat          # atalho Windows
  run_graph.bat         # atalho Windows
  README.md             # instruções da prova (estudante)
```

> **Você deve editar apenas:** `arvore/tree_logic.py` e `grafo/graph_logic.py`.

---

## ⚙️ Requisitos

- **Python 3.10+** (Windows, macOS ou Linux).  
- Não use bibliotecas externas (apenas biblioteca padrão).  
- Tkinter já vem com Python no Windows.

---

## ▶️ Como executar localmente (Windows)

1. Baixe/clone o repositório para sua máquina.  
2. Dê um duplo clique em **`run_tree.bat`** e **`run_graph.bat`** (ou use o terminal: `python arvore/app_tree.py` e `python grafo/app_graph.py`).  
3. Valide seus resultados antes de abrir o PR.

---

## 🎯 O que implementar

### 1) Árvore de Decisão (arquivo `arvore/tree_logic.py`)
- Função **`navigate_tree(node, answers)`**: navega na árvore com respostas `["sim", "não", ...]` até chegar a uma folha e retornar a decisão.  
- Trate respostas inválidas com `ValueError` e mensagens claras.

### 2) Conectividade em Grafo (arquivo `grafo/graph_logic.py`)
- Função **`connected(graph, a, b)`**: retorne `True` se houver qualquer caminho entre `a` e `b` (grafo não direcionado).  
- **Use apenas listas** (sem `deque`). BFS com `list.pop(0)` é suficiente para este exercício.

---

## 🤖 Uso de Inteligência Artificial (autorizado)

O uso de IA (ChatGPT, Copilot, etc.) é **permitido e incentivado** como apoio ao aprendizado. **Explique** no seu PR:
- Onde e como a IA ajudou.
- O que você entendeu de fato (não apenas o código final).

### Prompts sugeridos (foco no raciocínio)
- “Explique passo a passo como um grafo armazena conexões entre nós em Python.”  
- “Qual a diferença prática entre lista e matriz de adjacência?”  
- “Como a recursão funciona em percorrimentos de árvores binárias?”  
- “Analise este trecho e explique linha por linha.”  
- “Mostre duas formas de representar um grafo apenas com listas e discuta legibilidade.”

---

## 🔀 Fluxo de trabalho (Git & Pull Request)

1. **Fork** deste repositório para a sua conta.  
2. **Clone** o fork localmente.  
3. Crie uma **branch** com seu nome:  
   ```bash
   git checkout -b avaliacao-final-seu-nome
   ```
4. Implemente as funções nos arquivos `tree_logic.py` e `graph_logic.py`.  
5. Rode localmente. Adicione e faça commit:
   ```bash
   git add arvore/tree_logic.py grafo/graph_logic.py
   git commit -m "feat: implementa navigate_tree e connected (Avaliação Final)"
   git push origin avaliacao-final-seu-nome
   ```
6. Abra um **Pull Request** para o repositório original com o título:
   > `Avaliação Final – Seu Nome Completo`

### Corpo do PR (obrigatório)
- O que foi implementado (resumo).  
- Dificuldades e como solucionou.  
- Onde/como a IA ajudou e o que você entendeu.  
- Prints da execução (opcional, mas recomendado).

> **Somente PRs que modificarem exclusivamente os arquivos indicados serão aceitos.**

---

## 🗂️ Entrega acadêmica no Teams (obrigatória)

Anexe um **PDF** contendo:
- Nome e matrícula;
- Link direto do seu PR;
- Texto do seu Relato de Aprendizagem;
- Capturas de tela dos programas em execução.

> A nota só será registrada se **GitHub (PR)** e **Teams (PDF)** forem entregues.

---

## 🧮 Avaliação (0–10 pontos)

- **Árvore (5,0 pts):** navegação correta, tratamento de erros, clareza do código.  
- **Grafo (4,0 pts):** busca de conectividade correta usando listas, tratamento de erros.  
- **Relato (1,0 pt):** clareza, reflexão crítica e ética no uso de IA.

---

## ❓FAQ rápido

**Posso usar `deque`?** Não. Nesta atividade, use listas (`list.pop(0)` é suficiente para os grafos propostos).  
**Posso alterar as UIs?** Não. Elas estão “travadas” de propósito.  
**Posso trabalhar em dupla?** A entrega é **individual** por PR.  
**Dica:** comente seu código como se estivesse ajudando um colega.

---

## 📜 Licença

Sugerimos **MIT License** para permitir livre uso educacional. Consulte o arquivo `LICENSE`.
