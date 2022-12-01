"""
Django settings for restaurante project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from os import environ
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t7b%p&%wp%=+dh(t@222#vbisyrk8dn@qx6k#eklh$v9knmz_^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Cuando ya utilicemos un servidor de produccion ingresara a validar los host (dominios) permitidos
#que pueden consultar mi backend y del mismo si definimos un host para el modo de desarrollo tambien
#hara la validacion
ALLOWED_HOSTS = ['restaurante-django-yohan.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion',
    'corsheaders',# para trabajar con el uso de los cors
    'rest_framework',#para django rest-framework pueda devolver la informacion por el navegador
    #usando css y js
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restaurante.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'restaurante.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ.get('DB_NAME'),
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Sirve para indicar cual sera el modelo que utilizaremos para el auth_user en nuestra bd
AUTH_USER_MODEL = "gestion.UsuarioModel"

#Libreria Django RestFramewok utilizara todas las fonciguraciones que definamos
#en esta variable para este proyecto
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #indicamos que la libreria de autenticacion que va a utilizar DRF para poder autenticar al usuario entrante sera de la libreria simplejwt que acabamos de instalar        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

#Sirve para modificar todas las configuracion de la libreria simple-jwt
SIMPLE_JWT = {
    #la token de acceso tendra una duracion de 1h, 30min y 5seg
    'ACCESS_TOKEN_LIFETIME' : timedelta(days= 1,hours=1, minutes=30, seconds = 5),
    #Es la firma que se utilizara para firmar y verificar las tokens
    'SIGNING_KEY': environ.get('TOKEN_SECRET'),
    #Es el nombre con el cual se guardara en el payload el id del usuario
    'USER_ID_CLAIM': 'id_del_usuario'
}

#Sirve para indicar a los CORS que origenes estan permitios de hacer consultas
CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:5500', 'https://www.google.com']

#Sirve para indicar los metodos que puede consultar mi backend
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT']

#Sirve para indicar donde se guardaran los archivos estatis(CSS, JS, HTML) UTILIZA DJANGO y DRF
STATIC_ROOT = BASE_DIR / 'archivos_estaticos'