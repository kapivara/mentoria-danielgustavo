# Exercícios de Lógica
## Contexto
Exercícios de lógica para fixação do mentorando **Daniel Gustavo**

## Como adicionar exercicios?
Olhe a issue no github e identifique o "milestone" dela, pode ser "EstuturaCondicional", "EstruturaRepeticao" etc...

Crie seus arquivos como mostrado na estrutura abaixo:

```
├── src
│   ├── estrutura_condicional
│   │   ├── __init__.py
│   │   ├── exercicio_um.py
│   │   ├── exercicio_dois.py
│   │   └── exercicio_tres.py
|   |
│   ├── estrutura_repeticao
│   |   ├── __init__.py
│   |   ├── exercicio_um.py
│   |   ├── exercicio_dois.py
│   |   └── ...
|   |
│   └── [nome do milestone/topico]
│       ├── __init__.py
│       ├── exercicio_um.py
│       ├── exercicio_dois.py
│       └── ...
|
└── test
    └── estrutura_condicional
        ├── __init__.py
        ├── exercicio_um_test.py
        ├── exercicio_dois_test.py
        └── ...
```

## Como rodar os testes?
Execute o comando dentro do diretório do projeto

```sh
python3 -m unittest discover -s test -p "*_test.py" --verbose
```
