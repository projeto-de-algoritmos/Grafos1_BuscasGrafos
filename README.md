# Buscas em Grafos

## Sobre

Este repositório destinado ao primeiro projeto relacionado a grafos da disciplina de Projetos de Algoritmos da Universidade de Brasília - Campus Gama do período do 2º semestre de 2019.

## Contribuidores

|Matrícula|Nome|GitHub|
|---------|----|------|
|160006210| Francisco Heronildo|[@FranciscoHeronildo](github.com/FranciscoHeronildo)|
|160010195| João Vítor Morandi|[@joaovitorml](github.com/joaovitorml)|

## Buscas

Os arquivos `bfs.py` e `dfs.py`, realizam as buscas em largura e profundidade nos grafos por meio de dicionários, por fim foi analisado o tempo de execução fazendo a busca em diferentes grafos.

## Tempo de Execução

|Casos de Testes|BFS|DFS|
|---------------|---|---|
|1º|0.000317|0.000154|
|2º|0.000343|0.000055|
|3º|0.000133|0.000063|
|4º|0.000175|0.000018|
|5º|0.000129|0.000008|

### Gráfico de Execução - BFS

![graphbfs](https://i.imgur.com/Hpm2oxM.png)

### Gráfico de Execução - DFS

![graphdfs](https://i.imgur.com/kXMyxjS.png)

## Executando as Buscas

### Debian

#### Via Terminal

Clone o Repositório:

`$ git clone https://github.com/projeto-de-algoritmos/grafo_1_Francisco_Joao.git`

Acesse o diretório:

`$ cd grafo_1_Francisco_Joao/Trabalho1`

Busca em Largura:
`$ python3 bfs.py` 

Busca em Profundidade:
`$ python3 dfs.py`

Plotagem de um gráfico exemplo como imagem:
`$ python3 plotGraph.py`