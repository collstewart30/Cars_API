# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&0jzdt)tewvkodzrwn@vef@glyj$wge8kw1-k4r=qr$=p5o4*%'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password'
    }
}