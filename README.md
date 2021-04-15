# e-commerce com Django

# Importante

- O projeto é um site feito com o web framework Django, tem testes para rodarem em Docker (que não estão compostos no repositório) e podem ser alterados de acordo com os produtos e/ou necessidades de novas implementações
- O site é um ecommercee um blog, sendo possivel haver implementação para ambos os projetos no mesmo site e usando as mesmas ferramentas
- As interfaces e templates são feitos com [bootstrap](https://getbootstrap.com/docs/4.0/examples/) para que haja simplicidade e seja ainda assim responsivo.
- É um site colaborativo e que tem intuito de divulgar tanto ciencia e filosofia, como técnologia (visto que todo código do site vai ser ensinado passo a passo por mim mesmo futuramente).


# Como rodar o projeto

- Clone o projeto, para isso você pode simplesmente baixar o arquivo ou usar o git, para clonar diretamente do repositório remoto :
```
git clone https://github.com/Chuckpy/Django-ecommerce.git
```
- Dentro do repositório, agora local, você precisa criar um novo ambiente virtual. Seja ele qual for, o próximo passo é acessa-lo e partir para a próxima etapa

- Caso for rodar localmente, não deixe de, dentro do seu ambiente virtual, instalar todas as bibliotecas necessárias :
```
pip install -r requirements.txt
```

- Não esqueça de rodar as migrations:
```
python manage.py makemigrations
```
E então :
```
python manage.py migrate
```

- Se você não quiser procurar/criar fotos para os seus produtos, utilize a fixture `products.json`. As imagens também estão nesse repositório, na pasta media. Para inserir os produtos no banco de dados execute:
```
python manage.py loaddata products
```
- Você pode iniciar a qualquer momento com : 
```
python manage.py runserver
```

- Para usar a interface de administrador do Django, use :
```
python manage.py createsuperuser
```



Por fim, acesse o site neste link: [http://localhost:8000/](http://localhost:8000/)

Caso haja alguma duvida, ou precisar de ajuda, sinta-se livre para perguntar :

- [Marcus Vinicius](https://twitter.com/MarcusV92211788)

Ps : Posso demorar um pouco para responder
 

# Referências

- [Fabio Ruicci Cursos](https://www.fabioruicci.com.br/)
- [Python Crash Course](https://www.amazon.com.br/Python-Crash-Course-Eric-Matthes/dp/1593279280)
- [Repostitório Cookiecutter Django](https://github.com/pydanny/cookiecutter-django)