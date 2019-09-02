import time

inicio = time.time()

# Caso 1
# lista = {'1':['2'],'3':['4'],'2':['3'],'4':['1']}
# Caso 2
# lista = {'1':['4','5'],'2':['1','4','6'],'3':['7'],'4':['1','2','5'],'5':['1','4'],'6':['2'],'7':['3']}
# Caso 3
#lista = {'1':['2','3','4','5'],'2':['1','3','4','5'],'3':['1','2','4','5'],'4':['1','2','3','5'],'5':['1','2','3','4']}

lista = {'1':['2'],'3':['4'],'2':['3'],'4':['1']}

arvore = []
explorados = []

def dfs(lista):
    for v in lista:
        if v not in explorados:
            dfs_visit(lista,v)


def dfs_visit(lista,v):
    explorados.append(v)
    for w in lista[v]:
        if w not in explorados:
            temp = [v,':[',w,']']
            arvore.append(temp)
            dfs_visit(lista,w)

dfs(lista)

print('explorados: ', explorados)
print('arvore: ', arvore)

fim = time.time()

print('tempo de execução:'fim - inicio)