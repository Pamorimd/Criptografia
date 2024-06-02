import numpy as np

T = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

NOME = input("ENTRE COM O VETOR DA PALAVRA A SER CRIPTOGRAFADA: ").upper()  # Converter para maiúsculas

# Encontra os índices correspondentes na matriz T
I = [T.index(c) + 1 for c in NOME if c in T]
print(I)

# Se o comprimento da lista de índices for ímpar, adiciona um índice extra (0) no final
if len(I) % 2 != 0:
    I.append(0)

# Organiza os índices em pares, mas agrupa por coluna
# I[i:i+num_cols]: Dentro do loop, isso faz uma fatia de I começando em i e indo até i + num_cols. 
# Isso basicamente cria uma sublista de I com num_cols elementos, começando na posição i.

num_cols = 2
P = [I[i:i+num_cols] for i in range(0, len(I), num_cols)]

#cria uma matriz
A = np.array([[11, 13], [2, 3]])
#multiplica a matriz chave pela transposta
C = np.dot(A, np.transpose(P)) % 26

# Mapeia os índices resultantes de volta para letras do alfabeto
TC = []
for col in C.T:
    for c in col:
        if c == 0:
            c = 26
        TC.append(T[c-1])

print("TEXTO CRIPTOGRAFADO:", ''.join(TC))