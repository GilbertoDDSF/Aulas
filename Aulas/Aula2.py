# Abrindo Chrome com Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By  # Localiza elementos
from selenium.webdriver.common.keys import Keys  # Permite clicar teclas no teclado

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/") #Abrindo o Google
navegador.find_element(By.XPATH,
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar") #Encontrando o Elemento via XPATH e escrevendo

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
    Keys.ENTER) #Dando Enter

cotacao_dolar = navegador.find_element(By.XPATH,
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute(
    'data-value') #Buscando o valor

print("Cotacao dolar:", cotacao_dolar)

navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
    Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH,
                                      '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute(
    'data-value')

print("Cotacao Euro:", cotacao_euro)

navegador.get('https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,em%20R%24%20299%2C71./')

cotacao_ouro = navegador.find_element(By.XPATH,
                                      '//*[@id="comercial"]').get_attribute('value')

cotacao_ouro = cotacao_ouro.replace(",", ".")
print("Cotacao Ouro", cotacao_ouro)

navegador.quit() #Fechando o navegador

import pandas as pd

tabela = pd.read_excel(r"C:\Users\Gilberto\OneDrive\Área de Trabalho\Aula\Aula3\Produtos.xlsx") # Importando tabela excel
print(tabela)

#Atualizando a cotacao de acordo com a moeda correspondente
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_dolar)

print(tabela)

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)

#Exportando nova tabela
tabela.to_excel(r"C:\Users\Gilberto\OneDrive\Área de Trabalho\Aula\Aula3\Produtos Novos.xlsx", index=False)
