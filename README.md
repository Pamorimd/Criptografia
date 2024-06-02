# Criptografia com NumPy

## Introdução

Este é um programa em Python que demonstra um método simples de criptografia de palavras inseridas pelo usuário. Utilizando a biblioteca NumPy, o programa realiza operações matriciais para embaralhar as letras da palavra, oferecendo uma forma básica de proteger informações sensíveis.

Ao explorar os conceitos de matrizes e operações matriciais, este programa fornece uma introdução prática à criptografia e ao uso da biblioteca NumPy em Python.

---
## Índice

1. [Funcionamento](#funcionamento)
2. [Como Usar](#como-usar)

## Funcionamento <a name="funcionamento"></a>

O programa funciona da seguinte maneira:

1. Recebe uma palavra inserida pelo usuário.
2. Converte a palavra para letras maiúsculas.
3. Encontra os índices correspondentes a cada letra na matriz de letras do alfabeto.
4. Organiza os índices em pares de duas letras, agrupando por coluna.
5. Cria uma matriz de criptografia.
6. Multiplica a matriz de criptografia pela transposta dos pares de índices.
7. Mapeia os índices resultantes de volta para letras do alfabeto.
8. Imprime o texto criptografado.

## Como Usar <a name="como-usar"></a>

1. Clone o repositório para a sua máquina local.
2. Certifique-se de ter Python e NumPy instalados.
3. Execute o arquivo `criptografia.py`.
4. Insira a palavra que deseja criptografar quando solicitado.
5. O programa irá gerar e imprimir o texto criptografado.


---
