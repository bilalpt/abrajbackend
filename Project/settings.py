import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables (only used locally)
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "your_local_secret_key")

# ⚙️ Debug mode
DEBUG = os.getenv("DEBUG", "True") == "True"

# 🌍 Allowed Hosts
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1,abrajbackend.onrender.com"
).split(",")

# 🔒 CSRF Trusted Origins (for frontend + backend)
CSRF_TRUSTED_ORIGINS = [
    "https://abrajfrontend-bgdh.vercel.app",
    "https://abrajfrontend-bgdh-git-main-bilalpts-projects.vercel.app",
    "https://abrajbackend.onrender.com",
]

# ------------------------------------------------
# 📦 Application Definition
# ------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'firstapp',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be placed before CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'

# ------------------------------------------------
# 🗄️ Database (Use PostgreSQL on Render)
# ------------------------------------------------

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),  # ✅ no fallback to sqlite
        conn_max_age=600,
        ssl_require=True
    )
}


# ------------------------------------------------
# 🔑 Password Validation
# ------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------
# 🌐 Internationalization
# ------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------
# 🧾 Static Files
# ------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ------------------------------------------------
# 🔓 CORS Configuration
# ------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://abrajfrontend-bgdh.vercel.app",
    "https://abrajfrontend-bgdh-git-main-bilalpts-projects.vercel.app",
]

# ✅ Automatically allow all Vercel preview URLs
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://abrajfrontend-bgdh-.*\.vercel\.app$",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']

# ------------------------------------------------
# 🧱 Default Auto Field
# ------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
