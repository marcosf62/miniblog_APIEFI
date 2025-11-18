# API REST - MiniBlog (Flask)

Esta es la documentación del backend desarrollado con *Flask*
- Cómo levantar el proyecto
- Dependencias necesarias
- Endpoints disponibles
- Parámetros que recibe cada endpoint
- Formatos de respuesta

---

## 1. Cómo levantar el proyecto

### Requisitos previos
- Python 3.10 o superior
- pip
- Virtualenv

--

###*Paso 2: Crear un entorno virtual*
bash
python3 -m venv venv
source venv/bin/activate  


### *Paso 3: Instalar dependencias*
bash
pip install -r requirements.txt


###  *Paso 4: Ejecutar la API*
bash
flask run --debug

La API por defecto se levanta en:

http://127.0.0.1:5000




## 2. Autenticación
La API usa *JWT (JSON Web Tokens)*.

Se tiene que enviar el token en los endpoints protegidos usando:

Authorization: Bearer <token>



##  3. Endpoints disponibles

### *POST /api/register*
Registra un nuevo usuario.

#### Body JSON
json
{
  "username": "marcos",
  "email": "marcos@mail.com",
  "password": "12345678"
}


#### Respuesta
json
{
  "msg": "Usuario creado exitosamente"
}



### *POST /api/login*
Realiza el login y devuelve un *access_token*.

#### Body JSON
json
{
  "email": "marcos@mail.com",
  "password": "12345678"
}


#### Respuesta
json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}



##  Posts

### *GET /api/posts*  (Público)
Devuelve la lista de posts.

#### Respuesta ejemplo
json
[
  {
    "id": 1,
    "title": "Primer post",
    "content": "Hola mundo",
    "author_id": 7,
    "created_at": "2025-11-15"
  }
]



### *POST /api/posts* (Requiere token)
Crea un nuevo post.

#### Body JSON
json
{
  "title": "Nuevo post",
  "content": "Contenido del post"
}


#### Respuesta
json
{
  "msg": "Post creado",
  "post": {
    "id": 3,
    "title": "Nuevo post",
    "content": "Contenido del post",
    "author_id": 7
  }
}



### *PUT /api/posts/<id>* (Requiere token y ser autor)
Edita un post existente.

#### Body JSON (cualquiera de los dos campos)
json
{
  "title": "Título actualizado",
  "content": "Nuevo contenido"
}


#### Respuesta
json
{
  "msg": "Post actualizado"
}



### *DELETE /api/posts/<id>* (Requiere token y ser autor)
Borra un post.

####  Respuesta
json
{
  "msg": "Post eliminado"
}



## Comentarios (Reviews)

### *GET /api/posts/<id>/reviews* (Público)
Devuelve los comentarios del post.

#### Respuesta
json
[
  {
    "id": 1,
    "content": "Muy bueno!",
    "user_id": 7,
    "created_at": "2025-11-16"
  }
]



### *POST /api/posts/<id>/reviews* (Requiere token)
Agrega un comentario.

#### Body JSON
json
{
  "content": "Excelente post"
}


#### Respuesta
json
{
  "msg": "Comentario creado",
  "review": {
    "id": 5,
    "content": "Excelente post",
    "user_id": 7
  }
}



## Errores

###  401 - Token inválido
json
{ "msg": "Token inválido o expirado" }


### 403 - No autorizado
json
{ "msg": "No tenés permisos para esta acción" }