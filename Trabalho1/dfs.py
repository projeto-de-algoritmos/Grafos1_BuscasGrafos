import time

inicio = time.time()

lista = ['1:[2]','2:[3]','3:[4]','4:[1]']
arvore = []
explorados = []

def dfs(lista):
    for v in lista[1]:
        if v not in explorados:
            dfs_visit(lista,v)


def dfs_visit(lista,v):
    explorados.append(v)
    for w in lista[2]:
        if w  not in explorados:
            temp = [v,':[',w,']']
            arvore.append(temp)
            dfs_visit(lista,w)

dfs(lista)

print(explorados)


fim = time.time()

print(fim - inicio)