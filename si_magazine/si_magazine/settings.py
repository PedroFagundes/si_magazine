import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'og4dtgmngi5k15ng7q@6vskqvq$=fkae_zs!d3lbf4uco3yuf='

DEBUG = True

ALLOWED_HOSTS = ['fasainforma.aethersolucoes.com.br']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    'social.apps.django_app.default',

    'posts',
    'homesite',
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

ROOT_URLCONF = 'si_magazine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                #python-social-app context processors
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'si_magazine.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fasa_informa',
	'USER': 'fasainforma',
	'PASSWORD': 'fasainforma',
	'HOST': 'localhost',
    }
}

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = 'homesite/static/'

CKEDITOR_UPLOAD_PATH = "uploads/"

MEDIA_URL = os.path.join(BASE_DIR, 'homesite/static/media/')

# django-ckeditor
CKEDITOR_JQUERY_URL = 'http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# python-social-auth backends
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'

SOCIAL_AUTH_TWITTER_KEY = 'fKSDtmJYPj6YdqaIAkxDg8CMY'
SOCIAL_AUTH_TWITTER_SECRET = 'uDQwZIGTxxH028EccWeNFMokHuJJii2KKYREo6xUQ9RMlJFNGc'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '861896151943-9j8vlmd6nocho1f29b8u22nk60k2k7s7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'fdkWtkSuPCAPLum0Bdz_mL7M'

SOCIAL_AUTH_FACEBOOK_KEY = '815093458588258'
SOCIAL_AUTH_FACEBOOK_SECRET = 'abe970c6068b98e71526533104b371a0'
