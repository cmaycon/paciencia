# 🃏 Jogo de Paciência - Estruturas de Dados e Algoritmos

Este projeto é uma implementação interativa do clássico jogo de Paciência (Solitaire) executado diretamente no terminal utilizando Python. O foco principal é a aplicação prática e construída do zero de **Estruturas de Dados** e **Algoritmos Complexos**.

## 🚀 Funcionalidades e Conceitos Aplicados

O sistema foi desenvolvido para cobrir de forma robusta uma série de práticas acadêmicas e melhorias de usabilidade:
*   **Estruturas de Dados Base:** Implementação manual de **Pilha** (LIFO), **Fila** (FIFO) e **Lista Ligada** dinâmica.
*   **Algoritmos de Ordenação:** Módulos para ordenar o baralho inicial utilizando **Bubble Sort**, **Merge Sort** e **Quick Sort**.
*   **Recursão:** Embaralhamento de vetor implementado de forma iterativa e recursiva.
*   **Lógica de Movimentação (M1, M2, M3):** Algoritmos complexos para validar regras de jogo e transferir cartas e sublistas inteiras manipulando ponteiros.
*   **UX/UI no Terminal:** Sistema de limpeza de tela dinâmica (compatível com Windows/Linux/Mac) para fixar o tabuleiro, além de **Códigos ANSI** para colorir as cartas de Copas e Ouros de vermelho, facilitando a visualização.

## 📁 Estrutura do Projeto

O código está modularizado em três arquivos principais:

*   `carta.py`: Classe base da carta (número, naipe e status), incluindo a lógica de coloração no terminal.
*   `estruturas.py`: O núcleo de dados. Contém as classes `Pilha`, `Fila` e `ListaLigada`, além de lógicas avançadas para extrair sublistas e manipular os ponteiros dos nós.
*   `paciencia.py`: O motor central. Gerencia o baralho de 52 cartas, as 4 Pilhas, 1 Fila e 7 Listas Ligadas, e roda o laço principal de interação com o usuário.

## ⚙️ Como Executar

**Pré-requisitos:** Python 3.x instalado. O projeto utiliza apenas bibliotecas nativas (`os`, `sys`, `random`), portanto, **não é necessário** instalar dependências externas via `pip`.

1.  Abra o terminal ou Prompt de Comando.
2.  Navegue até a pasta do projeto.
3.  Execute o comando:
    ```bash
    python paciencia.py
    ```

## 🕹️ Como Jogar (Passo a Passo)

Ao rodar o programa, você verá o **Menu de Testes**, onde pode verificar o funcionamento interno dos algoritmos de ordenação e recursão. Para jogar, digite a opção **7**.

### 1. Entendendo o Tabuleiro
A tela será redesenhada a cada jogada e mostrará:
*   **Fila:** O seu monte de compra (mostra apenas a carta do topo).
*   **Pilha 1 a 4:** Suas "fundações" onde o jogo deve ser finalizado.
*   **Lista Ligada 1 a 7:** As colunas da mesa onde o jogo acontece. As cartas vermelhas (Copas/C e Ouros/O) aparecerão destacadas em vermelho no seu terminal.

### 2. Realizando Movimentos
O menu exibirá 6 opções numéricas. Digite o número correspondente à ação desejada e pressione `ENTER`. O sistema fará perguntas simples, como "Para qual Lista Ligada (1 a 7)?", baseadas na sua escolha.

*   **1- da Fila para a Fila:** Descarta a carta visível da compra e revela a próxima.
*   **2- da Fila para uma Pilha:** Tenta enviar a carta de compra direto para a fundação final.
*   **3- da Fila para uma Lista Ligada:** Pega a carta da compra e coloca em uma coluna da mesa.
*   **4- de uma Pilha para uma Lista Ligada:** Desfaz uma jogada, retornando a carta da fundação para a mesa.
*   **5- de uma Lista Ligada para uma Pilha:** Move a última carta disponível de uma coluna para a fundação.
*   **6- de uma Lista Ligada para outra (Mover Sublistas):** Esta é a jogada mais estratégica. O sistema pedirá a Lista de Origem, a Lista de Destino e a **Posição** da carta.
    *   *Nota sobre Posições:* O índice `0` representa a primeira carta do topo da coluna. Se você quiser mover as últimas 3 cartas de uma coluna que tem 5 cartas visíveis, digite a posição correspondente à carta mais alta que deseja arrastar.

### ⚠️ Regras Essenciais do Jogo
*   **Pilhas (Fundações):** Só aceitam cartas do **mesmo naipe** e em ordem **crescente** (do Ás/1 até o Rei/13). Uma pilha vazia só aceita um Ás (1).
*   **Listas Ligadas (Colunas):** Só aceitam cartas de **cores alternadas** (vermelho sobre preto, ou vice-versa) e em ordem **decrescente** (ex: um 5 preto só pode ser colocado em cima de um 6 vermelho). Uma coluna vazia só aceita um Rei (13).