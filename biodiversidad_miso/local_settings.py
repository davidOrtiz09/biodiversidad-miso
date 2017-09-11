# Replace this values with your local settings
import os
import dj_database_url

# Please change this value when deploying to heroku
is_deployed = False

if is_deployed:
    DATABASE_DICT = dj_database_url.config(default=os.environ.get('DATABASE_URL', ''))
else:
    DATABASE_DICT = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BD2',
        'USER': 'UsuarioApp',
        'PASSWORD': '12345a',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }

EMAIL_SETTINGS = {
    'EMAIL_HOST': 'in-v3.mailjet.com',
    'EMAIL_HOST_USER': '510bda2c0fea067ab966740d06885c90',
    'EMAIL_HOST_PASSWORD': '37530af72c68ced2106ba8d1b9d2904e',
    'EMAIL_PORT': 587,
    'EMAIL_USE_TLS': True,
    'DEFAULT_FROM_EMAIL': 'Biodiversidad G2 <{0}>'.format('jc.tangarife1927@uniandes.edu.co')
}
