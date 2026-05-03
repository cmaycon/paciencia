class No:
    """Classe auxiliar para a Lista Ligada. Cada nó guarda uma carta e aponta para a próxima."""
    def __init__(self, carta):
        self.carta = carta
        self.proximo = None

class Pilha:
    """Estrutura LIFO (Last In, First Out) - O último a entrar é o primeiro a sair."""
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, carta):
        """Empilha uma carta."""
        self.itens.append(carta)

    def pop(self):
        """Remove e retorna a carta do topo."""
        if not self.is_empty():
            return self.itens.pop()
        return None

    def peek(self):
        """Apenas olha a carta do topo sem remover."""
        if not self.is_empty():
            return self.itens[-1]
        return None

class Fila:
    """Estrutura FIFO (First In, First Out) - O primeiro a entrar é o primeiro a sair."""
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, carta):
        """Enfileira uma carta no final."""
        self.itens.append(carta)

    def dequeue(self):
        """Remove e retorna a carta do início da fila."""
        if not self.is_empty():
            return self.itens.pop(0)
        return None

    def peek(self):
        """Apenas olha a carta do início da fila."""
        if not self.is_empty():
            return self.itens[0]
        return None

class ListaLigada:
    """Estrutura de dados dinâmica onde os elementos estão ligados por ponteiros."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, carta):
        """Insere uma carta no final da lista ligada."""
        novo_no = No(carta)
        if self.is_empty():
            self.head = novo_no
            return
        
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def get_last(self):
        """Retorna a carta do final da lista ligada sem removê-la."""
        if self.is_empty():
            return None
            
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        return atual.carta
        
    def mostrar_cartas(self):
        """Método auxiliar para imprimir as cartas da lista na tela, escondendo as viradas para baixo."""
        cartas = []
        atual = self.head
        while atual:
            if atual.carta.status:
                # Se a carta estiver virada para cima, mostra a carta normal
                cartas.append(str(atual.carta))
            else:
                # Se estiver virada para baixo, mostra um mistério
                cartas.append("[?]")
            atual = atual.proximo
        return " -> ".join(cartas)

    def pop_last(self):
        """Remove e retorna a carta do final da lista ligada."""
        if self.is_empty():
            return None
            
        # Se só tem um elemento
        if self.head.proximo is None:
            carta = self.head.carta
            self.head = None
            return carta

        # Vai até o PENÚLTIMO elemento
        atual = self.head
        while atual.proximo.proximo is not None:
            atual = atual.proximo

        # Salva a carta do último, e desconecta ele da lista
        carta = atual.proximo.carta
        atual.proximo = None
        return carta

    def get_carta_at(self, index):
        """Retorna a carta em uma posição específica (0 é a primeira)."""
        atual = self.head
        count = 0
        while atual:
            if count == index:
                return atual.carta
            count += 1
            atual = atual.proximo
        return None

    def mover_sublista_para(self, destino_lista, index):
        """
        Corta a lista atual a partir do 'index' e gruda no final da 'destino_lista'.
        Isso atende ao requisito de remover a sublista e inserir na primeira lista.
        """
        if self.is_empty():
            return False

        # Se for para mover a lista inteira (índice 0)
        if index == 0:
            sublista_head = self.head
            self.head = None # Esvazia a origem
        else:
            # Vai até o nó ANTERIOR ao corte
            atual = self.head
            count = 0
            while atual and count < index - 1:
                atual = atual.proximo
                count += 1

            if atual is None or atual.proximo is None:
                return False # Índice inválido

            # Corta a lista
            sublista_head = atual.proximo
            atual.proximo = None

        # Agora gruda a sublista no final do destino
        if destino_lista.is_empty():
            destino_lista.head = sublista_head
        else:
            atual_destino = destino_lista.head
            while atual_destino.proximo:
                atual_destino = atual_destino.proximo
            atual_destino.proximo = sublista_head

        return True

    def virar_ultima_carta(self):
        """Garante que a carta que sobrou no final da coluna fique virada para cima."""
        if self.is_empty():
            return
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.carta.status = True