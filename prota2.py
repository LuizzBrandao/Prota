import sys
from collections import deque

def criar_grafo():
    grafo = {}
    vertices = []
    return grafo, vertices

def inserir_vertice(grafo, vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        grafo[vertice] = []
        print(f"Vértice '{vertice}' inserido com sucesso!")
    else:
        print(f"Vértice '{vertice}' já existe.")

def remover_vertice(grafo, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return
    vertices.remove(vertice)
    grafo.pop(vertice, None)
    for v in grafo:
        if vertice in grafo[v]:
            grafo[v].remove(vertice)
    print(f"Vértice '{vertice}' removido com sucesso!")

def inserir_aresta(grafo, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(grafo, vertices, origem)
    if destino not in vertices:
        inserir_vertice(grafo, vertices, destino)
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)
    print(f"Aresta '{origem} -> {destino}' inserida com sucesso!")

def remover_aresta(grafo, vertices, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
        print(f"Aresta '{origem} -> {destino}' removida com sucesso!")
    else:
        print(f"Aresta '{origem} -> {destino}' não existe.")
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)

def existe_aresta(grafo, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        print("Um ou ambos os vértices não existem.")
        return False
    existe = destino in grafo[origem]
    print(f"Existe aresta '{origem} -> {destino}': {existe}")
    return existe

def vizinhos(grafo, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return []
    return grafo[vertice]

def listar_vizinhos(grafo, vertices, vertice):
    viz = vizinhos(grafo, vertices, vertice)
    print(f"Vizinhos de '{vertice}': {viz}")

def grau_vertices(grafo, vertices):
    print("\n--- Graus dos Vértices ---")
    if not vertices:
        print("O grafo está vazio.")
        return
    for v in vertices:
        saida = len(grafo[v])
        entrada = sum(1 for u in vertices if v in grafo[u])
        total = saida + entrada
        print(f"{v}: saída={saida}, entrada={entrada}, total={total}")
    print("--------------------------\n")

def percurso_valido(grafo, vertices, caminho):
    if not caminho:
        print("Percurso vazio.")
        return False
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i + 1]
        if not (u in vertices and v in vertices and v in grafo[u]):
            print(f"Percurso inválido: não existe aresta '{u} -> {v}'")
            return False
    print("Percurso é válido!")
    return True

def exibir_grafo(grafo, vertices):
    print("\n=== Grafo (Lista de Adjacência) ===")
    if not vertices:
        print("O grafo está vazio.")
    for v in vertices:
        print(f"{v} -> {grafo[v]}")
    print("==============================\n")

def relatorio_completo_grafo(grafo, vertices):
    print("\n===== RELATÓRIO COMPLETO DO GRAFO =====")
    if not vertices:
        print("O grafo está vazio.")
        print("======================================\n")
        return
    print("\n--- Lista de Adjacência (Todos os Vizinhos) ---")
    for v in vertices:
        print(f"{v} -> {grafo[v]}")
    print("\n--- Graus dos Vértices ---")
    for v in vertices:
        saida = len(grafo[v])
        entrada = sum(1 for u in vertices if v in grafo[u])
        total = saida + entrada
        print(f"{v}: saída={saida}, entrada={entrada}, total={total}")
    print("\n======================================\n")



def busca_em_largura(grafo, vertices, inicio):
    if inicio not in vertices:
        print(f"Vértice '{inicio}' não existe.")
        return
    visitados = set()
    fila = deque([inicio])
    print("\n--- Busca em Largura (BFS) ---")
    passo = 1
    while fila:
        print(f"Passo {passo}:")
        print(f"Fila atual: {list(fila)}")
        atual = fila.popleft()
        if atual not in visitados:
            print(f"Visitando: {atual}")
            visitados.add(atual)
            for viz in grafo[atual]:
                if viz not in visitados and viz not in fila:
                    fila.append(viz)
        print(f"Visitados até agora: {list(visitados)}\n")
        passo += 1
    print("--- BFS finalizada ---\n")

def menor_caminho_bfs(grafo, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        print("Um ou ambos os vértices não existem.")
        return
    fila = deque([origem])
    visitados = {origem}
    antecessor = {origem: None}
    while fila:
        atual = fila.popleft()
        if atual == destino:
            break
        for viz in grafo[atual]:
            if viz not in visitados:
                visitados.add(viz)
                antecessor[viz] = atual
                fila.append(viz)
    if destino not in antecessor:
        print(f"Não existe caminho entre '{origem}' e '{destino}'.")
        return
    caminho = []
    v = destino
    while v is not None:
        caminho.append(v)
        v = antecessor[v]
    caminho.reverse()
    print(f"Menor caminho entre '{origem}' e '{destino}': {caminho}")
    print(f"Tamanho do caminho: {len(caminho) - 1} arestas\n")


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
10. Relatório completo do grafo
11. Busca em Largura (BFS)
12. Menor Caminho (BFS)
0. Sair
======================
""")

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
        elif opcao == "10":
            relatorio_completo_grafo(grafo, vertices)
        elif opcao == "11":
            inicio = input("Digite o vértice inicial: ").strip()
            busca_em_largura(grafo, vertices, inicio)
        elif opcao == "12":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            menor_caminho_bfs(grafo, vertices, origem, destino)
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
