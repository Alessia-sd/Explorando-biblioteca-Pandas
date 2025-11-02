import pandas as pd

def main():
    ######### 1 - Importação e Verificação
    nome_do_arquivo = 'retail_2016_2017.csv'
    df_vendas = None
    try:
        # Importar o dataset para um DataFrame
        df_vendas = pd.read_csv(nome_do_arquivo)
        print("Dataset importado com sucesso! Primeiras 5 linhas:")
        print(df_vendas.head())
        print("\nInformações do DataFrame:")
        df_vendas.info()
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{nome_do_arquivo}' não foi encontrado.")
        return # Sair da função se o arquivo não for encontrado
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return

    # Certificar que df_vendas é um DataFrame válido antes de continuar
    if df_vendas is None:
        return

    ######### 2 - Contagem de Categorias Únicas
    numero_de_categorias = df_vendas['family'].nunique()
    print(f"\nO número de categorias de produtos ('family') existentes no DataFrame é: {numero_de_categorias}")

    ######### 3 - Filtragem de 'SEAFOOD'
    condicao_filtro = df_vendas['family'] == 'SEAFOOD'
    colunas_desejadas = ['family', 'sales']
    vendas_seafood = df_vendas.loc[condicao_filtro, colunas_desejadas]
    print("\nVendas da Categoria 'SEAFOOD' (apenas 'family' e 'sales'):")
    print(vendas_seafood.head())
    print(f"\nTotal de registros de vendas de SEAFOOD: {len(vendas_seafood)}")

    ######### 4 - Filtragem Condicional (AUTOMOTIVE OU BEAUTY com SALES > 85)
    condicao_categorias = (df_vendas['family'] == 'AUTOMOTIVE') | (df_vendas['family'] == 'BEAUTY')
    condicao_vendas = df_vendas['sales'] > 85
    filtro_final_4 = condicao_categorias & condicao_vendas
    vendas_filtradas = df_vendas[filtro_final_4]
    print("\nVendas filtradas (AUTOMOTIVE OU BEAUTY) com SALES > 85:")
    print(vendas_filtradas.head(10))
    print(f"\nTotal de registros que satisfazem o filtro: {len(vendas_filtradas)}")

    ######### 5 - Filtro Temporal e Soma Condicional
    df_vendas['date'] = pd.to_datetime(df_vendas['date'])
    df_vendas['month'] = df_vendas['date'].dt.month
    condicao_lojas = df_vendas['store_nbr'].isin([25, 31])
    condicao_meses = df_vendas['month'].isin([5, 6])
    condicao_vendas_baixas = df_vendas['sales'] < 2000
    filtro_final_5 = condicao_lojas & condicao_meses & condicao_vendas_baixas
    df_filtrado = df_vendas[filtro_final_5]
    soma_total_vendas = df_filtrado['sales'].sum()
    print("\n--- Resultado da Soma das Vendas Filtradas ---")
    print(f"Soma total das vendas filtradas: {soma_total_vendas:.2f}")

    ######### 6 - Cálculo do Mínimo de Vendas (> 0)
    vendas_sem_zero = df_vendas[df_vendas['sales'] > 0]['sales']
    minimo_sem_zero = vendas_sem_zero.min()
    print("\n--- Cálculo do Mínimo ---")
    print(f"O valor mínimo de 'sales' (excluindo 0) é: {minimo_sem_zero:.2f}")

    ######### 7 - Vendas por Categoria (Top 8 Menores)
    vendas_por_familia = df_vendas.groupby('family')['sales'].sum()
    vendas_por_familia = vendas_por_familia.astype(int)
    vendas_ordenadas = vendas_por_familia.sort_values(ascending=True)
    primeiras_oito_linhas = vendas_ordenadas.head(8)
    print("\n--- Total de Vendas por Categoria (Top 8 Menores Vendas) ---")
    print(primeiras_oito_linhas)

    ######### 8 - Adicionar Imposto
    df_vendas['tax'] = 0.23
    df_vendas['total_sales_with_tax'] = df_vendas['sales'] * (1 + df_vendas['tax'])
    print("\n--- DataFrame com Imposto Adicionado e Total Calculado (Primeiras 5 Linhas) ---")
    print(df_vendas[['sales', 'tax', 'total_sales_with_tax']].head())

    ######### 9 - Filtrar e Concatenar 'SEAFOOD' e 'BEVERAGES'
    df_seafood = df_vendas[df_vendas['family'] == 'SEAFOOD'].copy()
    df_beverages = df_vendas[df_vendas['family'] == 'BEVERAGES'].copy()
    df_combinado = pd.concat([df_seafood, df_beverages], ignore_index=True)
    print("\n--- DataFrame Combinado (SEAFOOD e BEVERAGES) ---")
    print(df_combinado.head())
    print(f"\nTotal de registros no DataFrame Combinado: {len(df_combinado)}")

    ######### 10 - Eliminar a Coluna 'onpromotion'
    df_combinado.drop('onpromotion', axis=1, inplace=True)
    print("\n--- DataFrame Combinado Atualizado (Primeiras 5 Linhas) ---")
    print(df_combinado.head())
    print("\n--- Colunas do DataFrame Após a Remoção ---")
    print(df_combinado.columns)

#Executar a função main() quando o script for iniciado
if __name__ == "__main__":
    main()