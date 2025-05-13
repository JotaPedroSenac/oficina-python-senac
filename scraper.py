import requests
from bs4 import BeautifulSoup
import csv

url = 'https://books.toscrape.com/'

resposta = requests.get(url)
resposta.encoding = 'UTF-8'

# print(resposta.status_code)

soup = BeautifulSoup(resposta.text, 'html.parser')
livros = soup.find_all('article', class_='product_pod')

# print(livros)


with open('relatorio.csv', 'w' , newline = '', encoding='UTF-8') as csvfile:
    escritor = csv.writer(csvfile)

    escritor.writerow(['Título', 'Preco', 'link']) 
    
    for livro in livros:
        titulo = livro.h3.a['title']
        link = livro.h3.a['href']
        preco = livro.find('p', class_='price_color').text
        # print('--------------------------------------------')
        # print(titulo)
        # print(url+link)
        # print(preco)
        # print('--------------------------------------------')
        escritor.writerow([titulo, preco, url+link])
    