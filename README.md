# CRM Project

Este es un sistema de CRM (Customer Relationship Management) desarrollado en Django, diseñado para gestionar relaciones con clientes, seguimiento de ventas y gestión de usuarios, roles y permisos.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [API Endpoints](#api-endpoints)
- [Dependencias](#dependencias)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción

Este CRM permite a las empresas gestionar la información de sus clientes, realizar un seguimiento de sus ventas y gestionar la autenticación de usuarios con roles y permisos. El proyecto utiliza Django y Django REST Framework para la creación de la API y está diseñado para ser extensible y seguro.

## Instalación

Para ejecutar este proyecto localmente, sigue estos pasos:

1. Clona este repositorio:

   ```bash
   git clone https://github.com/usuario/nombre-del-proyecto.git
   cd nombre-del-proyecto

    Crea un entorno virtual y actívalo:

python -m venv env
source env/bin/activate

Instala las dependencias:

pip install -r requirements.txt

Configura PostgreSQL y crea la base de datos para el proyecto.

Crea un archivo .env en la raíz del proyecto y agrega las variables necesarias:

SECRET_KEY='tu_clave_secreta'
DEBUG=True
DB_NAME='nombre_base_de_datos'
DB_USER='usuario_base_de_datos'
DB_PASSWORD='contraseña_base_de_datos'
DB_HOST='localhost'
DB_PORT='5432'

Realiza las migraciones de la base de datos:

python manage.py migrate

Crea un superusuario para acceder al panel de administración:

    python manage.py createsuperuser

Configuración

Asegúrate de que el archivo .env esté correctamente configurado con las credenciales de la base de datos y otros parámetros necesarios. Puedes cambiar DEBUG=True a DEBUG=False en producción.
Uso

Para iniciar el servidor local de Django, usa:

python manage.py runserver

El servidor estará disponible en http://localhost:8000.
Autenticación JWT

Este proyecto usa SimpleJWT para la autenticación mediante tokens JWT. Usa los siguientes endpoints para autenticación:

    Obtener token de acceso y de refresco: POST /api/token/
    Refrescar token de acceso: POST /api/token/refresh/

Estructura del Proyecto

CRM/
├── CRM/                  # Configuración principal de Django
│   ├── settings.py       # Configuración del proyecto
│   ├── urls.py           # URLs principales del proyecto
│   └── wsgi.py           # Configuración WSGI
├── users/                # App para la gestión de usuarios
│   ├── models.py         # Modelos de usuario, perfil, etc.
│   ├── views.py          # Vistas de la API de usuarios
│   ├── serializers.py    # Serializadores de usuario y perfiles
│   └── urls.py           # URLs para la app de usuarios
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto

API Endpoints

Algunos de los endpoints básicos incluyen:

    Usuarios:
        POST /api/users/register/ – Registrar un nuevo usuario
        GET /api/users/<id>/ – Obtener información de un usuario

    Autenticación:
        POST /api/token/ – Obtener tokens de acceso y de refresco
        POST /api/token/refresh/ – Refrescar el token de acceso

Más detalles sobre los endpoints están disponibles en el código o puedes usar herramientas como Postman para probar la API.

Claro, aquí tienes un ejemplo de cómo podrías estructurar el README.md para un proyecto de CRM en Django. Esto incluirá una descripción, instrucciones de instalación y ejecución, dependencias, y más.

# CRM Project

Este es un sistema de CRM (Customer Relationship Management) desarrollado en Django, diseñado para gestionar relaciones con clientes, seguimiento de ventas y gestión de usuarios, roles y permisos.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [API Endpoints](#api-endpoints)
- [Dependencias](#dependencias)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción

Este CRM permite a las empresas gestionar la información de sus clientes, realizar un seguimiento de sus ventas y gestionar la autenticación de usuarios con roles y permisos. El proyecto utiliza Django y Django REST Framework para la creación de la API y está diseñado para ser extensible y seguro.

## Instalación

Para ejecutar este proyecto localmente, sigue estos pasos:

1. Clona este repositorio:

   ```bash
   git clone https://github.com/usuario/nombre-del-proyecto.git
   cd nombre-del-proyecto

    Crea un entorno virtual y actívalo:

python -m venv env
source env/bin/activate

Instala las dependencias:

pip install -r requirements.txt

Configura PostgreSQL y crea la base de datos para el proyecto.

Crea un archivo .env en la raíz del proyecto y agrega las variables necesarias:

SECRET_KEY='tu_clave_secreta'
DEBUG=True
DB_NAME='nombre_base_de_datos'
DB_USER='usuario_base_de_datos'
DB_PASSWORD='contraseña_base_de_datos'
DB_HOST='localhost'
DB_PORT='5432'

Realiza las migraciones de la base de datos:

python manage.py migrate

Crea un superusuario para acceder al panel de administración:

    python manage.py createsuperuser

Configuración

Asegúrate de que el archivo .env esté correctamente configurado con las credenciales de la base de datos y otros parámetros necesarios. Puedes cambiar DEBUG=True a DEBUG=False en producción.
Uso

Para iniciar el servidor local de Django, usa:

python manage.py runserver

El servidor estará disponible en http://localhost:8000.
Autenticación JWT

Este proyecto usa SimpleJWT para la autenticación mediante tokens JWT. Usa los siguientes endpoints para autenticación:

    Obtener token de acceso y de refresco: POST /api/token/
    Refrescar token de acceso: POST /api/token/refresh/

Estructura del Proyecto

CRM/
├── CRM/                  # Configuración principal de Django
│   ├── settings.py       # Configuración del proyecto
│   ├── urls.py           # URLs principales del proyecto
│   └── wsgi.py           # Configuración WSGI
├── users/                # App para la gestión de usuarios
│   ├── models.py         # Modelos de usuario, perfil, etc.
│   ├── views.py          # Vistas de la API de usuarios
│   ├── serializers.py    # Serializadores de usuario y perfiles
│   └── urls.py           # URLs para la app de usuarios
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto

API Endpoints

Algunos de los endpoints básicos incluyen:

    Usuarios:
        POST /api/users/register/ – Registrar un nuevo usuario
        GET /api/users/<id>/ – Obtener información de un usuario

    Autenticación:
        POST /api/token/ – Obtener tokens de acceso y de refresco
        POST /api/token/refresh/ – Refrescar el token de acceso

Más detalles sobre los endpoints están disponibles en el código o puedes usar herramientas como Postman para probar la API.
Dependencias

Principales dependencias usadas en este proyecto:

    Django
    Django REST Framework
    Django REST Framework SimpleJWT
    PostgreSQL

Consulta requirements.txt para ver todas las dependencias.
