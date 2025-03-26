import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('MY_SECRET_KEY', 'fallback-secret-key')

DEBUG = True  # Change to False in production

ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1',
    'your-production-domain.com',
    '.azurewebsites.net'  # If deploying to Azure App Service
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'files',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Should be first
    'corsheaders.middleware.CorsMiddleware',         # Before CommonMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',    # After SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

# settings.py
# Add to the existing settings

# Azure Blob Storage Settings
AZURE_STORAGE_ACCOUNT_NAME = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
AZURE_STORAGE_ACCOUNT_KEY = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')
AZURE_STORAGE_CONTAINER_NAME = os.getenv('AZURE_STORAGE_CONTAINER_NAME')

AZURE_STORAGE_CONNECTION_STRING = f"DefaultEndpointsProtocol=https;AccountName={AZURE_STORAGE_ACCOUNT_NAME};AccountKey={AZURE_STORAGE_ACCOUNT_KEY};EndpointSuffix=core.windows.net"

WSGI_APPLICATION = 'backend.wsgi.application'

CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# Replace your current CONNECTION_STR parsing with:
CONNECTION_STR = dict(pair.split('=', 1) for pair in CONNECTION.split(' ') if '=' in pair)
# Azure PostgreSQL database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONNECTION_STR.get('dbname'),  # Azure PostgreSQL typically uses 'dbname' in connection string
        'USER': CONNECTION_STR.get('user'),
        'PASSWORD': CONNECTION_STR.get('password'),
        'HOST': CONNECTION_STR.get('host'),
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
        'CONN_MAX_AGE': 600,
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = ["https://victorious-plant-03e42600f.6.azurestaticapps.net"]
