### Atividade Analise de dados: Explorar Pandas

1. Importe o dataset 'retail_2016_2017.csv' que contém dados sobre as vendas de uma loja de retalho.  
#####
2. Quantas categorias de produtos ('family') existem no DataFrame?  
######
3. Filtre o DataFrame para mostrar apenas as vendas da categoria SEA-FOOD e as colunas 'family' e 'sales'.
######  
4. Agora filtre o DataFrame para mostrar apenas as vendas das categorias AUTOMOTIVE e BEAUTY com valores superiores a 85 unidades de venda. 
###### 
5. Some as vendas para as lojas ('store_nbr') 25 e 31 que ocorreram em maio e junho e que tiveram menos de 2000 vendas ('sales'). Comece por criar uma nova coluna chamada 'month' e apresente o resultado com duas casas decimais. 
######
6. Calcule o valor mínimo da coluna 'sales', excluindo os valores iguais a 0. 
######
7. Determine o número de vendas ('sales') por categoria ('family'). Converta a coluna 'sales' para o tipo inteiro, ordene os valores de forma crescente e imprima apenas as primeiras oito8 linhas.
######
8. Adicione uma nova coluna chamada 'tax' com o valor constante de 0.23 e calcule o total das vendas com impostos incluídos. 
######
9. Crie um DataFrame que contenha apenas as vendas da categoria SEA-FOOD e outro DataFrame com as vendas da categoria BEVERAGES. Concatene os dois DataFrames. 
######
10. Elimine do DataFrame concatenado a coluna 'onpromotion'.