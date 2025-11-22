def connected(graph, a, b):
    """
    Retorna True se existe um caminho (qualquer) entre 'a' e 'b' no grafo não direcionado.
    Usa BFS (Busca em Largura) apenas com listas.
    """
    # 1. Validação básica: se os nós nem existem no grafo, não podem estar conectados
    if a not in graph or b not in graph:
        return False

    # 2. Estruturas de controle
    # 'fila' armazena os nós que precisamos visitar. Começa pelo ponto de partida 'a'.
    fila = [a]
    
    # 'visitados' evita loops infinitos (ex: A vai pra B, que volta pra A...)
    visitados = [a]

    # 3. Loop principal (enquanto houver lugares para visitar)
    while len(fila) > 0:
        # Pega o primeiro da fila (comportamento FIFO - First In, First Out)
        atual = fila.pop(0) 

        # Verificamos se chegamos ao destino
        if atual == b:
            return True

        # Se não chegamos, olhamos os vizinhos desse nó
        # graph.get(atual, []) garante que não quebre se o nó não tiver lista de vizinhos
        vizinhos = graph.get(atual, [])
        
        for vizinho in vizinhos:
            if vizinho not in visitados:
                visitados.append(vizinho) # Marca como visto
                fila.append(vizinho)      # Adiciona na fila para visitar depois

    # Se a fila esvaziar e não acharmos 'b', não existe conexão.
    return False