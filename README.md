# Python Algorithms Lab

Coleção de algoritmos clássicos de ordenação e busca, com implementação em Python, interface de linha de comando e testes automatizados.

## Funcionalidades
- Bubble Sort com parada antecipada, Selection Sort, Insertion Sort, Merge Sort e Quick Sort.
- Busca linear e busca binária (esta exige uma coleção ordenada).
- CLI para executar algoritmos sem editar o código.
- Testes com `unittest`, incluindo lista vazia, valores repetidos e entradas negativas.

## Requisitos
Python 3.10 ou superior. Nenhuma dependência externa.

## Executar
```bash
python -m src.main sort --algorithm merge --numbers 8 3 5 1 9
python -m src.main search --algorithm binary --target 5 --numbers 1 3 5 8 9
python -m unittest discover -s tests -v
```

## Estrutura
```text
src/algorithms.py  # implementações reutilizáveis
src/main.py        # interface de linha de comando
tests/             # testes automatizados
```

## Conceitos demonstrados
Complexidade de algoritmos, decomposição de problemas, type hints, funções puras, CLI e testes unitários.
