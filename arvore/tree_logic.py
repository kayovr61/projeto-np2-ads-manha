class Node:
    def __init__(self, question, yes=None, no=None):
        """
        Se 'yes' e 'no' forem None, este nó é uma FOLHA e 'question' guarda a decisão final (string).
        Caso contrário, 'question' é o texto da pergunta e 'yes'/'no' são seus filhos.
        """
        self.question = question
        self.yes = yes
        self.no = no

def is_leaf(node):
    return node is not None and node.yes is None and node.no is None

def navigate_tree(node, answers):
    """
    Percorre a árvore a partir de 'node' seguindo a sequência de respostas (lista de strings).
    """
    current_node = node
    idx = 0  # Índice para acompanhar qual resposta estamos lendo

    # Enquanto não chegarmos em uma folha (decisão final)
    while not is_leaf(current_node):
        # Verificação de segurança: Se acabaram as respostas mas ainda não é folha
        if idx >= len(answers):
            raise ValueError("Faltam respostas para concluir a decisão.")

        # Pega a resposta atual e avança o índice
        user_response = answers[idx].lower() 
        idx += 1

        if user_response == 'sim':
            current_node = current_node.yes
        elif user_response in ('não', 'nao'):
            current_node = current_node.no
        else:
            # Se o usuário digitou algo que não é sim/não (ex: "talvez")
            raise ValueError(f"Resposta inválida: '{user_response}'. Use apenas 'sim' ou 'não'.")

    # Se o loop acabou, significa que current_node é uma folha
    return current_node.question