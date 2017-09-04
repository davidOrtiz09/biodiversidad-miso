# Replace this values with your local settings
import os
import dj_database_url

# Please use this dict when deploying to heroku

DATABASE_DICT = dj_database_url.config(default=os.environ.get('DATABASE_URL', ''))

# Please use this dict for locale tests


DATABASE_DICT = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'biodiversidad_db',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': '127.0.0.1',
    'PORT': '5432',
}



