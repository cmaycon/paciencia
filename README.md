# 🃏 Jogo de Paciência - Estruturas de Dados e Algoritmos

Este projeto é uma implementação do clássico jogo de Paciência (Solitaire) desenvolvido inteiramente em Python. O objetivo principal do sistema é aplicar na prática os conceitos fundamentais de **Estruturas de Dados** e **Algoritmos**, construindo todas as estruturas do zero sem depender de bibliotecas externas complexas.

## 🚀 Funcionalidades e Conceitos Aplicados

O sistema foi desenvolvido para cobrir uma série de práticas acadêmicas, incluindo:
*   **Estruturas de Dados Base:** Implementação do zero de **Pilha** (LIFO), **Fila** (FIFO) e **Lista Ligada** dinâmica.
*   **Algoritmos de Ordenação:** Módulos para ordenar o baralho utilizando **Bubble Sort**, **Merge Sort** e **Quick Sort**.
*   **Recursão:** Algoritmo de embaralhamento implementado tanto de forma iterativa quanto recursiva.
*   **Lógica de Movimentação (M1, M2, M3):** Algoritmos complexos para validar e transferir cartas e sublistas inteiras entre as diferentes estruturas de dados.

## 📁 Estrutura do Projeto

O código está modularizado em três arquivos principais:

*   `carta.py`: Contém a classe base da carta, definindo seu número (1 a 13), naipe (c, o, p, e) e status (virada para cima/baixo).
*   `estruturas.py`: Implementação manual das classes `Pilha`, `Fila`, `ListaLigada` e `No`, contendo lógicas avançadas de remoção e inserção de sublistas.
*   `paciencia.py`: O motor do jogo. Gerencia as 4 Pilhas, 1 Fila e 7 Listas Ligadas, distribui o vetor de 52 cartas e processa a interface interativa (GUI de terminal).

## ⚙️ Como Executar

**Pré-requisitos:** Python 3.x instalado. Nenhuma biblioteca externa é necessária.

1.  Abra o terminal e navegue até a pasta do projeto.
2.  Execute o comando:
    
```bash
    python paciencia.py
    ```

## 🕹️ Como Utilizar o Sistema

Ao rodar o programa, você terá acesso a um **Menu de Testes**, onde poderá validar as ordenações e os algoritmos de embaralhamento. Ao escolher a opção **7. Jogar Paciência**, o jogo principal iniciará.

### Opções de Movimentação do Jogo:
A tela apresentará o estado atual da Fila (compra), das 4 Pilhas (fundações) e das 7 Listas Ligadas (colunas da mesa).

Você poderá escolher entre as seguintes ações:
1.  **Da Fila para a Fila:** Passa a carta do topo para o final do monte de compra.
2.  **Da Fila para uma Pilha:** Tenta enviar a carta de compra para a fundação.
3.  **Da Fila para uma Lista Ligada:** Tenta posicionar a carta de compra na mesa.
4.  **De uma Pilha para uma Lista Ligada:** Retorna uma carta da fundação para a mesa.
5.  **De uma Lista Ligada para uma Pilha:** Envia a última carta de uma coluna para a fundação.
6.  **De uma Lista Ligada para outra Lista Ligada (Sublistas):** Move uma ou mais cartas de uma coluna para outra.

### ⚠️ Regras do Jogo:
*   **Pilhas (Fundações):** Aceitam cartas em ordem **Crescente** (do Ás/1 ao Rei/13) e obrigatoriamente do **Mesmo Naipe**. (Pilhas vazias só aceitam Ás).
*   **Listas Ligadas (Colunas):** Aceitam cartas em ordem **Decrescente** e com **Cores Alternadas** (Vermelho sobre Preto, Preto sobre Vermelho). (Colunas vazias só aceitam Reis/13).
*   **Índices:** Ao interagir com o jogo, lembre-se que para mover uma sublista (opção 6), a posição `0` representa a carta mais alta (topo) daquela coluna visível.