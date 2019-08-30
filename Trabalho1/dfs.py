import time

inicio = time.time()

lista = {'1':['2'],'2':['3'],'3':['4'],'4':['1']}
arvore = []
explorados = []

def dfs(lista):
    for v in lista:
        if v not in explorados:
            print(v)
            dfs_visit(lista,v)


def dfs_visit(lista,v):
    explorados.append(v)
    for w in lista:
        if w  not in explorados:
            print(w)
            temp = [v,':[',w,']']
            arvore.append(temp)
            dfs_visit(lista,w)

dfs(lista)

print('explorados: ', explorados)
print('arvore: ', arvore)

fim = time.time()

print(fim - inicio)