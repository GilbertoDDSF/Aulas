import pandas as pd

tabela = pd.read_excel(r"C:\Users\Gilberto\OneDrive\Área de Trabalho\Aula\Vendas - Dez.xlsx")
print(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

print("O valor de faturamento é de ", faturamento)
print("A quantidade é ", quantidade)
