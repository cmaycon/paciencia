import sys
import random
from carta import Carta
from estruturas import Pilha, Fila, ListaLigada

sys.setrecursionlimit(1500)

class Paciencia:
    def __init__(self):
        # Criando quatro pilhas, uma fila e sete listas ligadas como variáveis globais da classe
        self.pilhas = [Pilha() for _ in range(4)]
        self.fila = Fila()
        self.listas_ligadas = [ListaLigada() for _ in range(7)]
        
        # Criar um vetor com as informações da carta de tamanho 52
        self.vetor_cartas = [None] * 52

    def gerar_baralho_ordenado(self, vetor):
        """
        Recebe o vetor vazio, armazena as 52 cartas de forma ordenada e retorna o vetor.
        """
        naipes = ['c', 'o', 'p', 'e'] # Copas, Ouros, Paus, Espadas
        index = 0
        for naipe in naipes:
            for numero in range(1, 14): # De 1 até 13
                vetor[index] = Carta(numero, naipe)
                index += 1
        return vetor

    def embaralhar_iterativo(self, vetor):
        """
        Recebe o vetor ordenado e o retorna embaralhado, trocando cartas 1000 vezes usando gerador aleatório.
        """
        # Clonando o vetor para não alterar o original diretamente
        vetor_embaralhado = vetor[:]
        for _ in range(1000):
            # Usando random.randint (equivalente ao Math.random do Java) para gerar índices aleatórios
            i = random.randint(0, 51)
            j = random.randint(0, 51)
            # Troca as cartas de posição
            vetor_embaralhado[i], vetor_embaralhado[j] = vetor_embaralhado[j], vetor_embaralhado[i]
        return vetor_embaralhado

    def embaralhar_recursivo(self, vetor, trocas=1000):
        """
        Embaralha o vetor de cartas recursivamente.
        """
        if trocas == 0:
            return vetor
            
        i = random.randint(0, len(vetor) - 1)
        j = random.randint(0, len(vetor) - 1)
        
        vetor[i], vetor[j] = vetor[j], vetor[i]
        
        # Chamada recursiva diminuindo o número de trocas
        return self.embaralhar_recursivo(vetor, trocas - 1)

    # --- ALGORITMOS DE ORDENAÇÃO ---
    # Copas(0) < Ouros(1) < Paus(2) < Espadas(3)
    def _obter_valor_ordenacao(self, carta):
        ordem_naipes = {'c': 0, 'o': 1, 'p': 2, 'e': 3}
        return ordem_naipes[carta.naipe] * 13 + carta.numero

    def ordenar_bubblesort(self, vetor):
        """Implementação do Bubble Sort."""
        arr = vetor[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self._obter_valor_ordenacao(arr[j]) > self._obter_valor_ordenacao(arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def ordenar_mergesort(self, vetor):
        """Implementação do Merge Sort."""
        if len(vetor) > 1:
            meio = len(vetor) // 2
            metade_esquerda = vetor[:meio]
            metade_direita = vetor[meio:]

            self.ordenar_mergesort(metade_esquerda)
            self.ordenar_mergesort(metade_direita)

            i = j = k = 0

            while i < len(metade_esquerda) and j < len(metade_direita):
                if self._obter_valor_ordenacao(metade_esquerda[i]) < self._obter_valor_ordenacao(metade_direita[j]):
                    vetor[k] = metade_esquerda[i]
                    i += 1
                else:
                    vetor[k] = metade_direita[j]
                    j += 1
                k += 1

            while i < len(metade_esquerda):
                vetor[k] = metade_esquerda[i]
                i += 1
                k += 1

            while j < len(metade_direita):
                vetor[k] = metade_direita[j]
                j += 1
                k += 1
        return vetor

    def ordenar_quicksort(self, vetor):
        """Implementação do Quick Sort."""
        if len(vetor) <= 1:
            return vetor
        else:
            pivo = vetor[0]
            menores = [c for c in vetor[1:] if self._obter_valor_ordenacao(c) <= self._obter_valor_ordenacao(pivo)]
            maiores = [c for c in vetor[1:] if self._obter_valor_ordenacao(c) > self._obter_valor_ordenacao(pivo)]
            return self.ordenar_quicksort(menores) + [pivo] + self.ordenar_quicksort(maiores)

    def menu_testes(self):
        """
        Módulo função menu que retornará uma opção que será escolhida pelo usuário. 
        Utilizar uma estrutura de swith/case. Em Python, usa-se match/case.
        """
        self.vetor_cartas = self.gerar_baralho_ordenado(self.vetor_cartas)
        baralho_atual = self.vetor_cartas[:]

        while True:
            print("\n=== MENU DE TESTES E ORDENAÇÃO ===")
            print("1. Ver Baralho Atual")
            print("2. Embaralhar Iterativo (1000 trocas)")
            print("3. Embaralhar Recursivamente")
            print("4. Ordenar com Bubble Sort")
            print("5. Ordenar com Merge Sort")
            print("6. Ordenar com Quick Sort")
            print("7. Jogar Paciência")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")

            match opcao:
                case '1':
                    print("\nBaralho:", baralho_atual)
                case '2':
                    baralho_atual = self.embaralhar_iterativo(baralho_atual)
                    print("\nBaralho embaralhado iterativamente!")
                case '3':
                    # Passando uma cópia para não mexer na referência da lista principal antes da hora
                    baralho_atual = self.embaralhar_recursivo(baralho_atual[:])
                    print("\nBaralho embaralhado recursivamente!")
                case '4':
                    baralho_atual = self.ordenar_bubblesort(baralho_atual)
                    print("\nBaralho ordenado com Bubble Sort!")
                case '5':
                    baralho_atual = self.ordenar_mergesort(baralho_atual)
                    print("\nBaralho ordenado com Merge Sort!")
                case '6':
                    baralho_atual = self.ordenar_quicksort(baralho_atual)
                    print("\nBaralho ordenado com Quick Sort!")
                case '7':
                    self.menu_jogar()
                case '0':
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida.")

    def iniciar_jogo(self):
        """
        Gera o baralho, embaralha e distribui as cartas nas estruturas conforme as regras do jogo.
        """
        # 1. Limpa as estruturas caso o jogador esteja reiniciando o jogo
        self.pilhas = [Pilha() for _ in range(4)]
        self.fila = Fila()
        self.listas_ligadas = [ListaLigada() for _ in range(7)]
        
        # 2. Gera e embaralha as cartas
        self.vetor_cartas = self.gerar_baralho_ordenado(self.vetor_cartas)
        baralho_embaralhado = self.embaralhar_iterativo(self.vetor_cartas)
        
        indice_carta = 0
        
        # 3. Distribui para as 7 Listas Ligadas
        for i in range(7):
            for j in range(i + 1):
                carta = baralho_embaralhado[indice_carta]
                # A última carta de cada coluna fica virada para cima (status = True)
                if j == i:
                    carta.status = True
                else:
                    carta.status = False
                    
                self.listas_ligadas[i].append(carta)
                indice_carta += 1
                
        # 4. As cartas restantes vão para a Fila
        while indice_carta < 52:
            carta_fila = baralho_embaralhado[indice_carta]
            carta_fila.status = False # Cartas na fila ficam viradas para baixo inicialmente
            self.fila.enqueue(carta_fila)
            indice_carta += 1

    # --- PRÁTICA PILHA 1 ---
    def verifica_pilha(self, pilha_destino, carta):
        """
        Recebe uma pilha e uma carta, verifica se pode ser empilhada e retorna verdadeiro ou falso.
        Regra: Crescente e mesmo naipe. Pilha vazia só aceita Ás (1).
        """
        if carta is None: 
            return False
        if pilha_destino.is_empty():
            return carta.numero == 1 # Apenas o Ás inicia a pilha
            
        topo = pilha_destino.peek()
        return (carta.numero == topo.numero + 1) and (carta.naipe == topo.naipe)

    # --- AUXILIAR PARA AS LISTAS LIGADAS ---
    def _cor_da_carta(self, carta):
        """Define se a carta é vermelha (copas/ouros) ou preta (paus/espadas)."""
        return "vermelho" if carta.naipe in ['c', 'o'] else "preto"

    def verifica_lista_base(self, lista_destino, carta):
        """Regra base da Lista Ligada: decrescente e cor alternada."""
        if carta is None: 
            return False
        if lista_destino.is_empty():
            return carta.numero == 13 # Apenas o Rei inicia uma coluna vazia
            
        ultima = lista_destino.get_last()
        if not ultima.status: # Não pode colocar em cima de carta virada para baixo
            return False
            
        cores_diferentes = self._cor_da_carta(ultima) != self._cor_da_carta(carta)
        numero_menor = carta.numero == ultima.numero - 1
        return cores_diferentes and numero_menor

    # --- PRÁTICA LISTA LIGADA 1 ---
    def verifica_M1(self, lista, fila):
        """M1: verifica se a carta do final da fila pode ser inserida na lista ligada."""
        return self.verifica_lista_base(lista, fila.peek())

    def verifica_M2(self, lista, pilha):
        """M2: verifica se a carta do topo da pilha pode ser inserida na lista ligada."""
        return self.verifica_lista_base(lista, pilha.peek())
    
    def verifica_M3(self, lista_destino, lista_origem, posicao):
        """
        M3: recebe uma lista ligada e outra lista com uma posição, 
        verifica se a carta pode ser inserida no final da primeira lista.
        """
        carta = lista_origem.get_carta_at(posicao)
        # Só permite mover se a carta alvo já estiver virada para cima (visível)
        if carta is None or not carta.status:
            return False
        return self.verifica_lista_base(lista_destino, carta)

    # --- PRÁTICA LISTA LIGADA 2 ---
    def mover_M1(self, lista, fila):
        """Procedimento: Fila -> Lista Ligada. Chama M1, remove da fila e insere na lista."""
        if self.verifica_M1(lista, fila):
            carta = fila.dequeue()
            carta.status = True # Vira a carta para cima ao colocar na mesa
            lista.append(carta)
            return True
        return False

    def mover_M2(self, lista, pilha):
        """Procedimento: Pilha -> Lista Ligada. Chama M2, remove da pilha e insere na lista."""
        if self.verifica_M2(lista, pilha):
            carta = pilha.pop()
            lista.append(carta)
            return True
        return False
    
    def mover_M3(self, lista_destino, lista_origem, posicao):
        """
        Procedimento: realiza a chamada do M3 e remove sublista ligada,
        inserindo na primeira lista ligada.
        """
        if self.verifica_M3(lista_destino, lista_origem, posicao):
            lista_origem.mover_sublista_para(lista_destino, posicao)
            lista_origem.virar_ultima_carta()
            return True
        return False
    

    def exibir_tela(self):
        """
        Desenvolvimento da tela: como as informações devem ser apresentadas ao usuário.
        """
        print("\n" + "="*60)
        print("Fila\tPilha 1\tPilha 2\tPilha 3\tPilha 4")
        
        # Pega a carta do topo da Fila (ou mostra [  ] se estiver vazia)
        fila_topo = str(self.fila.peek()) if not self.fila.is_empty() else "[  ]"
        
        # Pega a carta do topo de cada Pilha
        p1 = str(self.pilhas[0].peek()) if not self.pilhas[0].is_empty() else "[  ]"
        p2 = str(self.pilhas[1].peek()) if not self.pilhas[1].is_empty() else "[  ]"
        p3 = str(self.pilhas[2].peek()) if not self.pilhas[2].is_empty() else "[  ]"
        p4 = str(self.pilhas[3].peek()) if not self.pilhas[3].is_empty() else "[  ]"
        
        print(f"{fila_topo}\t{p1}\t{p2}\t{p3}\t{p4}")
        print("-" * 60)
        
        print("Listas Ligadas:")
        for i in range(7):
            cartas_lista = self.listas_ligadas[i].mostrar_cartas()
            if not cartas_lista:
                cartas_lista = "[  ]"
            print(f"Lista {i + 1}: {cartas_lista}")
        print("="*60)

    def menu_jogar(self):
        """
        Desenvolvimento de menu de opções de movimentação do paciência para o usuário.
        """
        print("\nEmbaralhando e distribuindo as cartas...")
        self.iniciar_jogo()
        while True:
            self.exibir_tela()
            print("\nOpções de movimentação. Digite:")
            print("1- da Fila para a Fila")
            print("2- da Fila para uma Pilha")
            print("3- da Fila para uma Lista Ligada")
            print("4- de uma Pilha para uma Lista Ligada")
            print("5- de uma Lista Ligada para uma Pilha")
            print("6- de uma Lista Ligada para outra Lista Ligada")
            print("0- Voltar")
            
            opcao = input("\nEscolha: ")
            
            match opcao:
                case '1':
                    # 1- da Fila para a Fila
                    # Simplesmente tira do começo e joga pro final
                    if not self.fila.is_empty():
                        carta = self.fila.dequeue()
                        self.fila.enqueue(carta)
                        print("\n-> Carta passada para o final da fila.")
                    else:
                        print("\n-> Fila vazia!")
                        
                case '2':
                    # 2- da Fila para uma Pilha
                    if self.fila.is_empty():
                        print("\n-> Fila vazia!")
                        continue
                    try:
                        p_idx = int(input("Para qual Pilha (1 a 4)? ")) - 1
                        if 0 <= p_idx <= 3:
                            # Usa a validação que foi criada
                            if self.verifica_pilha(self.pilhas[p_idx], self.fila.peek()):
                                carta = self.fila.dequeue()
                                carta.status = True # Vira para cima na pilha
                                self.pilhas[p_idx].push(carta)
                                print("\n-> Carta empilhada com sucesso!")
                            else:
                                print("\n-> Movimento inválido! A pilha exige mesma cor e sequência crescente (ou Ás na vazia).")
                        else:
                            print("\n-> Pilha inexistente.")
                    except ValueError:
                        print("\n-> Entrada inválida. Digite um número.")

                case '3':
                    # 3- da Fila para uma Lista Ligada
                    if self.fila.is_empty():
                        print("\n-> Fila vazia!")
                        continue
                    try:
                        l_idx = int(input("Para qual Lista Ligada (1 a 7)? ")) - 1
                        if 0 <= l_idx <= 6:
                            # Chama a função M1 que foi movida
                            if self.mover_M1(self.listas_ligadas[l_idx], self.fila):
                                print("\n-> Carta movida para a coluna com sucesso!")
                            else:
                                print("\n-> Movimento inválido! A lista exige cores alternadas e sequência decrescente (ou Rei na vazia).")
                        else:
                            print("\n-> Lista inexistente.")
                    except ValueError:
                        print("\n-> Entrada inválida.")
                        
                case '4':
                    # 4- de uma Pilha para uma Lista Ligada
                    try:
                        p_idx = int(input("De qual Pilha (1 a 4)? ")) - 1
                        l_idx = int(input("Para qual Lista Ligada (1 a 7)? ")) - 1
                        
                        if 0 <= p_idx <= 3 and 0 <= l_idx <= 6:
                            if self.mover_M2(self.listas_ligadas[l_idx], self.pilhas[p_idx]):
                                print("\n-> Carta movida da Pilha para a Coluna com sucesso!")
                            else:
                                print("\n-> Movimento inválido! (Cores alternadas, decrescente).")
                        else:
                            print("\n-> Índices inválidos.")
                    except ValueError:
                        print("\n-> Entrada inválida.")

                case '5':
                    # 5- de uma Lista Ligada para uma Pilha
                    try:
                        l_idx = int(input("De qual Lista Ligada (1 a 7)? ")) - 1
                        p_idx = int(input("Para qual Pilha (1 a 4)? ")) - 1
                        
                        if 0 <= l_idx <= 6 and 0 <= p_idx <= 3:
                            lista = self.listas_ligadas[l_idx]
                            pilha = self.pilhas[p_idx]
                            carta_alvo = lista.get_last()
                            
                            # Verifica se a última carta da lista pode entrar na pilha
                            if self.verifica_pilha(pilha, carta_alvo):
                                carta = lista.pop_last()
                                pilha.push(carta)
                                lista.virar_ultima_carta()
                                print("\n-> Carta movida para a Pilha (Fundação) com sucesso!")
                            else:
                                print("\n-> Movimento inválido para a Pilha.")
                        else:
                            print("\n-> Índices inválidos.")
                    except ValueError:
                        print("\n-> Entrada inválida.")

                case '6':
                    # 6- de uma Lista Ligada para outra Lista Ligada
                    try:
                        orig_idx = int(input("De qual Lista Ligada (Origem 1 a 7)? ")) - 1
                        dest_idx = int(input("Para qual Lista Ligada (Destino 1 a 7)? ")) - 1
                        posicao = int(input("Qual é a posição da carta na origem (0 é a primeira do topo da coluna)? "))
                        
                        if 0 <= orig_idx <= 6 and 0 <= dest_idx <= 6 and orig_idx != dest_idx:
                            # Chama o nosso novo método M3
                            if self.mover_M3(self.listas_ligadas[dest_idx], self.listas_ligadas[orig_idx], posicao):
                                print("\n-> Sublista movida com sucesso!")
                            else:
                                print("\n-> Movimento inválido! Verifique as regras e se a carta está virada.")
                        else:
                            print("\n-> Índices inválidos (ou origem igual a destino).")
                    except ValueError:
                        print("\n-> Entrada inválida.")
                case '0':
                    break
                case _:
                    print("\n-> Opção inválida!")

if __name__ == "__main__":
    jogo = Paciencia()
    jogo.menu_testes()