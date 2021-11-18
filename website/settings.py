"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#Enter domain name and IP addresses below
ALLOWED_HOSTS = ['ec2-18-117-33-76.us-east-2.compute.amazonaws.com','18.117.33.76','172.31.16.21','127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    'mysite.apps.MysiteConfig',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOWED_ORIGINS = [
    '[2603:7080:1d02:e040:2bff:3a61:ad66:482a]:80',
    '[2603:7080:1d02:e040:2bff:3a61:ad66:482a]:22',
    '18.117.33.76',
    '18.117.33.76:443',
    '18.117.33.76:80',
    '18.117.33.76:8080',
    '18.117.33.76:8000',
    '172.31.16.21',
    '172.31.16.21:80',
    '172.31.16.21:8080',
    '172.31.16.21:8000',
    '172.31.16.21:443',
    'http://localhost',
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost:80',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:80',
    'http://127.0.0.1',
    'https://feeds.npr.org',
    'https://feeds.arstechnica.com',
    'https://www.wgrz.com',
]
CSRF_TRUSTED_ORIGINS = [
    '[2603:7080:1d02:e040:2bff:3a61:ad66:482a]:80',
    '[2603:7080:1d02:e040:2bff:3a61:ad66:482a]:22',
    '18.117.33.76',
    '18.117.33.76:443',
    '18.117.33.76:80',
    '18.117.33.76:8080',
    '18.117.33.76:8000',
    '172.31.16.21',
    '172.31.16.21:80',
    '172.31.16.21:8080',
    '172.31.16.21:8000',
    '172.31.16.21:443',
    'http://localhost',
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost:80',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:80',
    'http://127.0.0.1',
    'https://feeds.npr.org',
    'https://feeds.arstechnica.com',
    'https://www.wgrz.com',
]
