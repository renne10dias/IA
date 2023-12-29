import pandas as pd

# Ler o arquivo JSON
dados = pd.read_json('./database/sorteio.json')

# Acessar os dados
sequencias = dados['sequencias']

# Imprimir as sequências
for sequencia in sequencias:
    print(sequencia)
