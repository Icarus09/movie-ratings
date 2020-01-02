# Title-Ratings
API que contém títulos (filmes e séries) e os usuários cadastrados podem classificá-los dando uma nota e escrevendo uma resenha, se quiser, parecido com o [IMDB](https://www.imdb.com). Projeto desenvolvido para avaliação da disciplina de Programação para a Internet II. Antes de clonar/baixar o repositório, veja os requisitos.

### Requisitos
* [Python 3.7.4](https://www.python.org);
* Django 2.2.8;
* Django Rest Framework 3.10.3;
* Django Filter 2.2.0;
* Django Crispy Forms;
* Django Rest Framework Simple JWT 4.3.0.

#### Todos são instaláveis via "pip install..."
```
  python -m pip install Django
  pip install djangorestframework
  pip install django-crispy-forms
  pip install django-filter
  pip install djangorestframework-simplejwt
```

### Modelagem do projeto

![ex_prog_int_II](https://user-images.githubusercontent.com/16518399/70394739-8a2b2300-19d6-11ea-8b64-7e66a1189bd4.png)

### Endpoints

| url                         | Funcionalidade                                                       |
|-----------------------------|----------------------------------------------------------------------|
| servidor/users              | Listagem e cadastro de usuários                                      |
| servidor/users/1            | Informações de um usuário específico                                 |
| servidor/starrings          | Listagem e cadastro de atores/atrizes que "estrelam" um título       |
| servidor/starrings/1        | Informações de um ator/atriz específico                              |
| servidor/titles             | Listagem e cadastro de títulos (filme/série) específicos             |
| servidor/titles/1           | Informações de um título específico                                  |
| servidor/genders            | Listagem e cadastro de gêneros para os títulos                       |
| servidor/genders/1          | Informações de um gênero específico                                  |
| servidor/starring-titles    | Listagem de atores e os filmes em que os mesmos                      |
| servidor/profile-list       | Listagem e cadastro de perfis                                        |
| servidor/profile-list/1     | Informações de um perfil específico                                  |
| servidor/ratings            | Listagem e cadastro de classificações/avaliações dos perfis do banco |
| servidor/ratings/1          | Informações de uma classificação/avaliação específica                |
| servidor/api/token/         | Login com token JWT (JSON Web Token)                                 |
| servidor/api/token/refresh/ | Atualização do token JWT                                             |

### Importante:
Por questões de segurança e organização, apenas o superusuário tem permissão para cadastrar gêneros, atores/atrizes e títulos. Um usuário comum cadastrado no banco pode apenas classificações/avaliações sobre os filmes. 

### [Vídeo demonstrativo](https://photos.app.goo.gl/Xe1HycFJHEsJz4CB8)
