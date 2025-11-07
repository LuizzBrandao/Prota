import sys

def criar_grafo():
    """Cria e retorna um grafo vazio (lista de adjacência)."""
    grafo = {}
    vertices = []
    return grafo, vertices


def inserir_vertice(grafo, vertices, vertice):
    """Adiciona um novo vértice ao grafo."""
    if vertice not in vertices:
        vertices.append(vertice)
        grafo[vertice] = []
        print(f"Vértice '{vertice}' inserido com sucesso!")
    else:
        print(f"Vértice '{vertice}' já existe.")


def remover_vertice(grafo, vertices, vertice):
    """Remove um vértice e todas as arestas associadas."""
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return

    vertices.remove(vertice)
    grafo.pop(vertice, None)

    # Remove arestas de entrada que apontavam para o vértice removido
    for v in grafo:
        if vertice in grafo[v]:
            grafo[v].remove(vertice)

    print(f"Vértice '{vertice}' removido com sucesso!")


def inserir_aresta(grafo, vertices, origem, destino, nao_direcionado=False):
    """Adiciona uma aresta entre dois vértices."""
    # Garante que os vértices existam antes de criar a aresta
    if origem not in vertices:
        inserir_vertice(grafo, vertices, origem)
    if destino not in vertices:
        inserir_vertice(grafo, vertices, destino)

    # Adiciona a aresta de saída
    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    # Se não direcionado, adiciona a aresta de volta
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

    print(f"Aresta '{origem} -> {destino}' inserida com sucesso!")


def remover_aresta(grafo, vertices, origem, destino, nao_direcionado=False):
    """Remove uma aresta entre dois vértices."""
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
        print(f"Aresta '{origem} -> {destino}' removida com sucesso!")
    else:
        print(f"Aresta '{origem} -> {destino}' não existe.")
    
    # Se não direcionado, remove a aresta de volta
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)


def existe_aresta(grafo, vertices, origem, destino):
    """Verifica se existe uma aresta direta entre dois vértices."""
    if origem not in vertices or destino not in vertices:
        print("Um ou ambos os vértices não existem.")
        return False
    existe = destino in grafo[origem]
    print(f"Existe aresta '{origem} -> {destino}': {existe}")
    return existe


def vizinhos(grafo, vertices, vertice):
    """Retorna os vizinhos de um vértice."""
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return []
    return grafo[vertice]


def listar_vizinhos(grafo, vertices, vertice):
    """Lista e exibe os vizinhos de um vértice."""
    viz = vizinhos(grafo, vertices, vertice)
    print(f"Vizinhos de '{vertice}': {viz}")


def grau_vertices(grafo, vertices):
    """Calcula e exibe o grau de entrada, saída e total de cada vértice."""
    print("\n--- Graus dos Vértices ---")
    if not vertices:
        print("O grafo está vazio.")
        return
        
    for v in vertices:
        saida = len(grafo[v])
        # Calcula o grau de entrada
        entrada = 0
        for u in vertices:
            if v in grafo[u]:
                entrada += 1
        
        total = saida + entrada
        print(f"{v}: saída={saida}, entrada={entrada}, total={total}")
    print("--------------------------\n")


def percurso_valido(grafo, vertices, caminho):
    """Verifica se um percurso é possível no grafo."""
    if not caminho:
        print("Percurso vazio.")
        return False
        
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i + 1]
        # Verifica se ambos os vértices existem e se a aresta u -> v existe
        if not (u in vertices and v in vertices and v in grafo[u]):
            print(f"Percurso inválido: não existe aresta '{u} -> {v}'")
            return False
    print("Percurso é válido!")
    return True


def exibir_grafo(grafo, vertices):
    """Exibe o grafo em formato de lista de adjacência."""
    print("\n=== Grafo (Lista de Adjacência) ===")
    if not vertices:
        print("O grafo está vazio.")
    for v in vertices:
        print(f"{v} -> {grafo[v]}")
    print("==============================\n")

# --- NOVA FUNÇÃO ADICIONADA ---
def relatorio_completo_grafo(grafo, vertices):
    """Exibe um relatório completo do grafo, incluindo vizinhos e graus."""
    print("\n===== RELATÓRIO COMPLETO DO GRAFO =====")
    if not vertices:
        print("O grafo está vazio.")
        print("======================================\n")
        return

    print("\n--- Lista de Adjacência (Todos os Vizinhos) ---")
    for v in vertices:
        print(f"{v} -> {grafo[v]}") # Mostra cada vértice e seus vizinhos

    print("\n--- Graus dos Vértices ---")
    for v in vertices:
        saida = len(grafo[v])
        # Calcula o grau de entrada
        entrada = 0
        for u in vertices:
            if v in grafo[u]:
                entrada += 1
        
        total = saida + entrada
        print(f"{v}: saída={saida}, entrada={entrada}, total={total}")
    
    print("\n======================================\n")
# -------------------------------


# --- MENU ATUALIZADO ---
def menu():
    print("""
===== MENU GRAFO =====
1. Inserir vértice
2. Remover vértice
3. Inserir aresta
4. Remover aresta
5. Exibir grafo (lista de adjacência)
6. Calcular grau de cada vértice
7. Verificar existência de aresta
8. Listar vizinhos de um vértice (específico)
9. Verificar se um percurso é possível
10. Relatório completo do grafo (vizinhos e graus)
0. Sair
======================
""")
# -----------------------


def main():
    grafo, vertices = criar_grafo()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            v = input("Digite o nome do vértice: ").strip()
            if v:
                inserir_vertice(grafo, vertices, v)
            else:
                print("Nome do vértice não pode ser vazio.")

        elif opcao == "2":
            v = input("Digite o vértice a remover: ").strip()
            remover_vertice(grafo, vertices, v)

        elif opcao == "3":
            o = input("Origem: ").strip()
            d = input("Destino: ").strip()
            if not o or not d:
                print("Origem e destino não podem ser vazios.")
                continue
            tipo = input("É não direcionada? (s/n): ").strip().lower()
            nao_dir = tipo == "s"
            inserir_aresta(grafo, vertices, o, d, nao_dir)

        elif opcao == "4":
            o = input("Origem: ").strip()
            d = input("Destino: ").strip()
            tipo = input("É não direcionada? (s/n): ").strip().lower()
            nao_dir = tipo == "s"
            remover_aresta(grafo, vertices, o, d, nao_dir)

        elif opcao == "5":
            exibir_grafo(grafo, vertices)

        elif opcao == "6":
            grau_vertices(grafo, vertices)

        elif opcao == "7":
            o = input("Origem: ").strip()
            d = input("Destino: ").strip()
            existe_aresta(grafo, vertices, o, d)

        elif opcao == "8":
            v = input("Digite o vértice: ").strip()
            listar_vizinhos(grafo, vertices, v)

        elif opcao == "9":
            percurso_str = input("Digite o percurso separado por espaço (ex: A B C): ").strip()
            caminho = percurso_str.split()
            percurso_valido(grafo, vertices, caminho)
        
        # --- NOVA OPÇÃO ADICIONADA ---
        elif opcao == "10":
            relatorio_completo_grafo(grafo, vertices)
        # -------------------------------

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()