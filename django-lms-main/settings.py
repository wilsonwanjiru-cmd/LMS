settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bird_app_db_qdks',
        'USER': 'wilson',
        'PASSWORD': 'WilsonWanjiru@2021',  # <-- Updated password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


SECRET_KEY = '7c9b052fff91b73de81de991c4eb6aef7fb25c703a855bb6717eaee431c4ba38e221cf6e'
DEBUG = True
