"""
Django settings for gym_app project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
from decouple import config
#import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

####################################################################
# SECURITY WARNING: keep the secret key used in production secret! #### Moved secret keys to a local file ####
####################################################################

# SECRET_KEY = os.environ['SECRET_KEY']  <-- Use this if you store your secret keys as an environment variable (EX. export SECRET_KEY="mYsEcReTkEy")
AIPSA_USER = os.environ['AIPSA_USER']  #<-- Similarly, use this if you store your AIPSA/Mongo username as an environment variable
AIPSA_PASS = os.environ['AIPSA_PASS']  #<-- Same thing for password
#AIPSA_USER = config('AIPSA_USER')
#AIPSA_PASS = config('AIPSA_PASS')

###################################################################
# SECURITY WARNING: don't run with debug turned on in production! #
###################################################################
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'bootstrap4',
    'crispy_forms',
    # 'Calendar',

    'gym_app.core',
    'gym_app',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'gym_app.urls'

TEMPLATES = [{
    'BACKEND' : 'django.template.backends.django.DjangoTemplates',
    'DIRS'    : [],  # 'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\','/')],
    'APP_DIRS': True,
    'OPTIONS' : {
        'context_processors': ['django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages', ],
    },
}, ]

WSGI_APPLICATION = 'gym_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

###################################################################
#          Moved database credentials to a local file             #
###################################################################

DATABASES = {
    'default': {
        'ENGINE'  : 'djongo',
        'NAME'    : 'AIPSA',
        'HOST'    : 'mongodb+srv://' + AIPSA_USER + ':' + AIPSA_PASS + '@aipsa-cftw0.mongodb.net/test?retryWrites=true',
        'USER'    : AIPSA_USER,
        'PASSWORD': AIPSA_PASS,
    }
}
#DATABASES['default'] = dj_database_url.config()

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [{
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
}, ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication',],
    'DEFAULT_PERMISSION_CLASSES'    : ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly']
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
