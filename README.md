# Tutorial e-commerce com Django

# Importante

- Vamos tocar esse projeto juntos? Dúvidas, sugestões e correções serão sempre bem vindas.

- Cada branch desse repositório é uma parte do tutorial, assim é possível ver como o projeto foi evoluindo.

# Como rodar o projeto

- No terminal, execute o comando
```
docker-compose up --build
```

- Para rodar os testes:
```
docker-compose exec web pytest
# algumas opções:
docker-compose exec web pytest -x --cov --cov-report=html
```

- Não esqueça de rodar as migrations:
```
docker-compose exec web python manage.py migrate
```

- Se você não quiser procurar/criar fotos para os seus produtos, utilize a fixture `products.json`. As imagens também estão nesse repositório, na pasta media. Para inserir os produtos no banco de dados execute:
```
docker-compose exec web python manage.py loaddata products
```

- Não esqueça de criar um superuser para acessar a interface de admin:
```
docker-compose exec web python manage.py createsuperuser
```

- Uma outra opção interessante é executar esse comando para acessar o container:
```
docker-compose exec web bash
```

E a partir daí rodar os comandos normalmente, sem acrescentar `docker-compose exec web` na frente.

Por fim, acesse o site neste link: [http://localhost:8000/](http://localhost:8000/)

Qualquer dúvida é só me procurar.

# Referências

- [Livro Django for Professionals](https://djangoforprofessionals.com/)
- [Livro Django 3 By Example](https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952)
- [Livro Two Scoops of Django](https://www.feldroy.com/collections/two-scoops-press/products/two-scoops-of-django-3-x)
- [Livro A Wedge of Django](https://www.feldroy.com/collections/two-scoops-press/products/a-wedge-of-django)
- [Repostitório Cookiecutter Django](https://github.com/pydanny/cookiecutter-django)