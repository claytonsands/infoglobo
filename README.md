# Projeto

Crawler para leitura da URL https://revistaautoesporte.globo.com/rss/ultimas/feed.xml conforme padrão exigido no desafio da infoblogo na url https://github.com/Infoglobo/desafio-back-end

# Configuração

## Pré-requisitos
- Python3
- Docker

Execute os comando abaixo para execução do projeto.

```
# git clone https://github.com/claytonsands/infoglobo
# cd infoglobo
# docker-compose up
# pip install -r requirements.txt
# python manage.py runserver
```

Para extrair o json do crawler execute o comando abaixo. Ele criará um arquivo com o nome infoglobo.jsonlines contendo a extração e também irá inserir os mesmo dados no banco do mongoDB.
```
scrapy runspider infoglobo\crawling\crawler.py -o infoglobo.jsonlines
```

Ao acessar a url http://127.0.0.1:8000 voce sera redirecionado para a pagina abaixo onde consegue manipular a API REST atraves de uma interface.

![alt text](https://ibb.co/Vgvb9CC)

Para acesso a api é necessário que reseja realizada a criação de um usuário, execute o comando abaixo no seu terminal para criação de um super user.
```
# python manage.py createsuperuser
```
