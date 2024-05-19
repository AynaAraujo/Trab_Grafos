from collections import deque
import graphviz


def bfs(graph, start):

    queue = deque([start]) # Gerencia a ordem de visitação

    visited = set([start]) #Guarda os vértices visitados

    visit_order = [] #Guarda a ordem dos vértices visitados

    dot = graphviz.Digraph(comment='Grafo de BFS') #Produz o png

    while queue:

        node = queue.popleft()  # Tira vértice da fila
        dot.node(node, node) #Add o nó retirado ao gráfico
        visit_order.append(node) #Add a ordem de sua visita

        for neighbor in graph[node]:    # Pega todos os vizinhos não visitados ainda
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
            dot.edge(node, neighbor)    # Add a aresta ao gráfico

    visit_order_str = " -> ".join(visit_order)

    return dot, visit_order_str #retorna o png e a string com a ordem de visitação


# Exemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

dot, visit_order_str = bfs(graph, 'A')
print("Ordem de visitação dos vértices:", visit_order_str)
dot.render('output/bfs_graph', format='png', view=True)
