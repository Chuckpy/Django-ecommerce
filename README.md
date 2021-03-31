# e-commerce com Django

# Importante

- O projeto é uma base para site que usa Django, tem testes para rodarem em Docker e podem ser alterados de acordo com os produtos e/ou necessidades de novas implementações
- As interfaces e templates são feitos com puro [bootstrap](https://getbootstrap.com/docs/4.0/examples/) para que haja simplicidade e seja ainda assim responsivo

# Como rodar o projeto

- Caso for rodar localmente, não esqueça de instalar todas as bibliotecas necessárias dentro do seu ambiente virtual

- Não esqueça de rodar as migrations:
```
python manage.py migrate
```

- Jáe existem algumas imagens, mas se você não quiser procurar/criar fotos para os seus produtos, utilize a fixture `products.json`. As imagens também estão nesse repositório, na pasta media. Para inserir os produtos no banco de dados execute:
```
python manage.py loaddata products
```

- Não esqueça de criar um superuser para acessar a interface de admin:
```
python manage.py createsuperuser
```



Por fim, acesse o site neste link: [http://localhost:8000/](http://localhost:8000/)

Caso haja alguma duvida, ou precisar de ajuda, sinta-se livre para perguntar


# Referências

- [Fabio Ruicci Cursos](https://www.fabioruicci.com.br/)
- [Python Crash Course](https://www.amazon.com.br/Python-Crash-Course-Eric-Matthes/dp/1593279280)
- [Repostitório Cookiecutter Django](https://github.com/pydanny/cookiecutter-django)
