from data_processing import Data

path_json:str = 'data-raw/A_company_data.json'
path_csv:str = 'data-raw/B_company_data.csv'

A_company_data:Data = Data(path_json, 'json')
print(A_company_data.data_path, A_company_data.type)
print(A_company_data.get_columns())
print(A_company_data.counter)

B_company_data:Data = Data(path_csv, 'csv')
print(B_company_data.data_path, B_company_data.type)
print(B_company_data.get_columns())
print(B_company_data.counter)

key_mapping = {
    'Nome do Item':'Nome do Produto',
    'Classificação do Produto':'Categoria do Produto',
    'Valor em Reais (R$)':'Preço do Produto (R$)',
    'Quantidade em Estoque':'Quantidade em Estoque',
    'Nome da Loja':'Filial',
    'Data da Venda':'Data da Venda'
}

print(B_company_data.column_names)
B_company_data.rename_columns(key_mapping=key_mapping)
print(B_company_data.column_names)

# Transformer Step
funsion_data = Data.join(A_company_data, B_company_data)
print(funsion_data.column_names)
print(funsion_data.counter)

# Save step
processed_data_path = 'data-processed/combined_datas.csv'
funsion_data.saving_data(processed_data_path)
