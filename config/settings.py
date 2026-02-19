# Django settings for multi-tenancy, Elasticsearch, Channels, and REST Framework

# Add your apps here
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'channels',
    'your_app_name',  # Replace with your actual app name
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# Channels settings
ASGI_APPLICATION = 'your_project_name.asgi.application'  # Replace with your actual project name

# Elasticsearch settings
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200',
    }
}

# Your multi-tenancy setup (use django-tenant-schemas or similar)
TENANT_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
]

SHARED_APPS = [
    'tenant_users',
    'django_tenants',
]

# Additional settings
# Add any other settings you require for your project here.
