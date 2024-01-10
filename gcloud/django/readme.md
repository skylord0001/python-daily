```python
from pathlib import Path
import os
from google.cloud import secretmanager
from google.auth import exceptions

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True
PRODUCTION = False

def get_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/yourAppName/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode('UTF-8')

if PRODUCTION:
    SECRET_KEY = get_secret('DJANGO_SECRET_KEY')
    ALLOWED_HOSTS = ['yourAppName.uc.r.appspot.com']
else:
    SECRET_KEY = 'random23454k01*(&*^()(&%^-development-secret-key'
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']


INSTALLED_APPS = [
    'storages',
]

if PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': get_secret('DB_HOST'),
            'NAME': get_secret('DB_NAME'),
            'USER': get_secret('DB_USER'),
            'PASSWORD': get_secret('DB_PASSWORD'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': get_secret('DB_HOST_IP'),
            'NAME': get_secret('DB_NAME'),
            'USER': get_secret('DB_USER'),
            'PASSWORD': get_secret('DB_PASSWORD'),
        }
    }



MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]
if PRODUCTION:
    import google.auth, json
    from google.oauth2 import service_account

    GS_BUCKET_NAME = get_secret("GS_BUCKET_NAME")
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(os.path.join(BASE_DIR, get_secret("GS_CREDENTIALS")))

    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
        'prefix': 'admin/*',
    }
    GS_OBJECT_PARAMETERS_2 = {
        'CacheControl': 'max-age=0, no-cache, no-store, must-revalidate',
        'prefix': 'media/*',
    }
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


```