import pandas as pd


print('Empresas ativas do Recife')


# Leitura do arquivo das empresas Ativas e listando as 10 primeiras linhas
empresas_ativas = pd.read_csv('empresasAtivas.csv', sep=',')
print(empresas_ativas.head(10))

# Colunas com pelo menos 1 valor NaN (Not A Number):
colunas_com_nan = empresas_ativas.columns[empresas_ativas.isna().any()].tolist()

print("Colunas com pelo menos 1 valor NaN (Not A Number):")
for coluna in colunas_com_nan:
    print(coluna)

# Printar "True" para campos preenchidos e "False" para campos em brancos/nulos
print(empresas_ativas.isnull())

# Soma dos valores total nulos por coluna:
print(empresas_ativas.isnull().sum())

# Renomeando a coluna original de nome: "_id" para: "ID" e listando as 10 primeiras linhas
empresas_ativas.rename(columns={'_id': 'ID'}, inplace=True)
print(empresas_ativas.head(10))


print('Empresas inativas do Recife')



# Leitura do arquivo das empresas inativas e listando as 15 primeiras linhas
empresas_inativas = pd.read_csv('empresasInativas.csv', sep=',')
print(empresas_inativas.head(15))

# Colunas com pelo menos 1 valor NaN (Not A Number):
colunas_com_nan2 = empresas_inativas.columns[empresas_inativas.isna().any()].tolist()

print("Colunas com pelo menos 1 valor NaN (Not A Number):")
for coluna in colunas_com_nan2:
    print(coluna)

# Printar "True" para os 15 primeiros campos preenchidos e "False" para campos em brancos/nulos
print(empresas_inativas.head(15).isnull())

# Soma dos valores total nulos por coluna:
print(empresas_inativas.isnull().sum())

# Renomeando a coluna original de nome: "cod_logradouro" para: "Código de Logradouro" e listando as 15 primeiras linhas
empresas_inativas.rename(columns={'cod_logradouro': 'Código de Logradouro'}, inplace=True)
#print(empresas_inativas.head(15))
# Chamando a soma dos campos nulos para melhor visualização do novo nome da coluna alterada
print(empresas_inativas.isnull().sum())