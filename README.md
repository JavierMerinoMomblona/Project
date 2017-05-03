# Django y MySQL. -Ubuntu16.10-

Este repositorio contiene la base para crear una pagina web / blog en un entorno virtual utilizando Django y una Base de Datos de MySQL.



## Requisitos / Especificaciones:

- Sistema operativo: Ubuntu 16.10
- Python 3.5



## Comandos a tener en cuenta:

 
**Activar el entorno virtual:** 

`source myvenv/bin/activate`  

> Debes estar en la carpeta 'Project' para que este comando surta efecto.

**Revisa la version de python que estas usando:** 

`python --version`  

> Dependiendo de en donde ejecutes el comando te devolvera la version de python en el sitio especifico en el que te encuentres. Esto puede sernos de utilidad si se dan casos de incompatibilidad.  

**Muestra los modelos de la Base de Datos que se este usando:**
  
  `python manage.py inspectdb`
  
> La Base de Datos que se esta usando viene especificada en el archivo  ***settings.py***  dentro de la carpeta  ***Project/mysite/*** :

```
DATABASES = {  
  'default': {  
    'ENGINE': 'django.db.backends.mysql',  
    'NAME': 'project',  
    'USER':  'usuario_con_privilegios_SQL',  
    'PASSWORD': 'password_de_usuario_SQL',  
    'HOST': '127.0.0.1',  
    'PORT': '',  
  }  
}
```

**Copia los modelos obtenidos en terminal al archivo *models.py* :** 

`python manage.py inspectdb > models.py`  

> Si la Base de Datos que se esta usando esta vacia, es decir, no contiene tablas, no se copiara mas que una serie de *imports* necesarios para el buen funcionanmiento de los modelos, en el caso de que existieran estos.

**Genera un archivo en el que se almacenaran las especificaciones de las migraciones:**

`python manage.py makemigrations`  

> Para este comando es necesario tener modelos ya creados.

**Genera la Base de Datos con lo especificado en las migraciones:**

`python manage.py migrate`  

> No se ejecutaran las migraciones si el archivo que las contiene no existe. Recomiendo hacer un *makemigrations* antes.
  
**Crea un superusuario el cual podra interactuar con la interfaz de administrador de Django:**

`python manage.py createsuperuser`  

> Recomiendo crear un superusuario sencillo y facil de recordar, ya que esto es en local y sirve para hacer pruebas. *Por ejemplo: nombre=**admin**, email=**'admin'@'admin.com'**, pass=**root1234**.* 

**Activar servidor local de Django:**

`python manage.py runserver`  

> Para acceder al servidor deberemos hacerlo a traves de nuestro navegador web y acceder a *http://127.0.0.1:8000* , si todo sale bien obtendremos un mensaje satisfactorio, de lo contrario tendremos que estar atentos a los errores y corregirlos. Para poder ver nuestra Base de Datos accederemos a *http://127.0.0.1/admin*. Ahi deberemos acceder con nuestros datos de superusuario y si todo sale bien podremos interactuar con nuestra Base de Datos.

> **NOTA:** Para acceder a *http://127.0.0.1:8000/admin* es necesario configurar el archivo ***admin.py*** en la carpeta ***Project/app***. Deberemos añadir tantos ***admin.site.register(nombre_modelo)*** como modelos haya. De manera que obtengamos algo parecido a esto:

```[python]
from django.contrib import admin
from .models import *

admin.site.register(nombre_modelo)
admin.site.register(nombre_modelo)
admin.site.register(nombre_modelo)
...
...
...
```
-----------------------------------------------------------------------









