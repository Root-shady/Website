"""
Django settings for myWeb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j@n6d^(#p-o-m&j(q=9rqrm(*vx&e)2mi*gl1*5xg%#dvyic)f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['159.203.228.69','rootshady.com']


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdown_deux',
    'crispy_forms',
    'home',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'myWeb.urls'

WSGI_APPLICATION = 'myWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default':{
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'shady_blog',
            'USER': 'shady',
            'PASSWORD':'Virblog6566619!',
        }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_in_env','static_root')
STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static_in_pro', 'our_static'),
        )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_in_env', 'media_root') # absolute path to the media directory

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # insert your TEMPLATE_DIRS here
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]
#'TEMPLATE_DEBUG' : True,
# Setting for markdown_deux 
MARKDOWN_DEUX_STYLES = {
        "trusted" :{    
            "extras":{
                    "code-friendly": None,
                    "html-classes": {"pre":"prettyprint", "code":"codesnippet","img":"postimage"},
                    "fenced-code-blocks": None,
                    "header-ids": None,
                    },
            "safe_mode": "escape",
            }
        }
# Setting the CSS frameworks that crispy-form used.
CRISPY_TEMPLATE_PACK = 'bootstrap3' 
