# Projeto

Crawler para extração de dados da URL https://revistaautoesporte.globo.com/rss/ultimas/feed.xml conforme solicitado no desafio da infoblogo na url https://github.com/Infoglobo/desafio-back-end.

# Configuração

* Pré-requisitos
  * Python3
  * Docker
  
Execute os comando abaixo para execução do projeto.

```
# git clone https://github.com/claytonsands/infoglobo
# cd infoglobo
# docker-compose up
# pip install -r requirements.txt
# python manage.py runserver
```
Com isso já será possivel acessar a URL http://127.0.0.1:8000 é ver a interface de manipulação REST conforme imagem abaixo.

![alt text](https://i.ibb.co/NLjtnSq/api-infoglobo.jpg)

Para acesso a api é necessário que seja realizada a criação de um usuário, execute o comando abaixo no seu terminal para criação de um superuser.
```
# python manage.py createsuperuser
```

# Crawler

Para extrair o json do crawler execute o comando abaixo. Ele criará um arquivo com o nome infoglobo.jsonlines contendo os dados extraidos. 
```
scrapy runspider infoglobo\crawling\crawler.py -o infoglobo.jsonlines
```
Além da criação do arquivo, o script **crawler.py** realiza a inserção dos dados extraidos no banco de dados do mongoDB (crawler.feed) anteriormente criado via docker-compose, tornando viavel a manipulação dele atrávez da API REST citada acima.


