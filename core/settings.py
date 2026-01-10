from pathlib import Path
from decouple import config
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# -------------------- BASE DIRECTORY --------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------- SECURITY --------------------
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)



# -------------------- INSTALLED APPS --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'users',  # your custom app
]

# -------------------- MIDDLEWARE --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

     'whitenoise.middleware.WhiteNoiseMiddleware',  
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------- URL CONFIG --------------------
ROOT_URLCONF = 'core.urls'

# -------------------- TEMPLATES --------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom context processors
                'users.context_processors.app_user',
                'users.context_processors.recruiter_job_count',
                'users.context_processors.freelancer_notifications',
            ],
        },
    },
]

# -------------------- WSGI --------------------
WSGI_APPLICATION = 'core.wsgi.application'

# -------------------- DATABASE --------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# -------------------- AUTH --------------------
LOGIN_URL = "/login-page/"
LOGIN_REDIRECT_URL = "/dashboard/"

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------- INTERNATIONALIZATION --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",   # where your CSS, JS, images live
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------- MEDIA FILES --------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# -------------------- CORS --------------------
CORS_ALLOW_ALL_ORIGINS = True  # change to False in production if needed

# -------------------- CSRF & SESSION --------------------
CSRF_COOKIE_SECURE = False  # True if using HTTPS
SESSION_COOKIE_SECURE = False  # True if using HTTPS
CSRF_COOKIE_HTTPONLY = False
ALLOWED_HOSTS = ['.onrender.com']

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com'
]

# -------------------- EMAIL --------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
