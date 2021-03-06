"""
Django settings for certificates123 project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'certficates123.settings')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c*knngm)lb=@a#lpn8cb2-#=g#5+cd!*2lh@x^!)#o!ietv=rs'

#Database
#DATABASES['default'] = dj_database_url.config(default='postgres://yhvdpkfvpqnzxi:37351074f05f81549ae71d5ed40a56c7315a3fb961a89612555729e8604d1939@ec2-54-195-252-243.eu-west-1.compute.amazonaws.com:5432/dcrdb5615hiabo')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.102', '127.0.0.1', 'certificates123.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'create'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'certificates123.urls'

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

WSGI_APPLICATION = 'certificates123.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #':@:5432/',
        'NAME': os.environ.get('DB_NAME', 'd9kn62i1imu22c'),
        'USER': os.environ.get('DB_USER', 'gxctwpkslxfhmb'),
        'PASSWORD': os.environ.get('DB_PASS', '8040fa29bac79a58b7f6877bb765fa2b8e89b1d0d48f987001b33e88651fca25'),
        'HOST': 'ec2-54-75-238-138.eu-west-1.compute.amazonaws.com',
        'PORT': '5432'
        #'NAME': os.environ.get('DB_NAME', 'certificates123'),
        #'USER': os.environ.get('DB_USER', 'admin'),
        #'PASSWORD': os.environ.get('DB_PASS', 'helloworld'),
        #'HOST': 'localhost',
        #'PORT': '5433'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
#DROPBOX_OAUTH2_TOKEN = '3MYZ9WTJyZAAAAAAAAAAC10o7EClAds_OWqymF46kosFrjdX35HYJKCTd9y4S-Jm'
#DROPBOX_ROOT_PATH = 'static'
