import os

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 加密秘钥   用户系统    session
SECRET_KEY = '#2c)du6f276utabqt5(zuh=(deb^c1bscc@qrw@+8#bw*%hm2x'

# 开发的时候用的  上线的时候要改成False
DEBUG = True
# 允许所有的ip都能访问我们的服务器
ALLOWED_HOSTS = ['*']

# 注册app
SYS_APPS = ['django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles', ]
EXT_APPS = [
    # xamdin 核心的app
    'xadmin',
    'crispy_forms',
    # 主题相关的app
    'reversion'
]
# 自定义的app
CUSTOM_APPS = [
    'apps.home.apps.HomeConfig',
    'apps.account',
    'apps.search',
    'apps.cars',
]

INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS
# 注册中间的
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TmallProjects.urls'
# 模板相关的配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
# 部署时候启动的对象
WSGI_APPLICATION = 'TmallProjects.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# 数据配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tmall',
        'PASSWORD': 'root',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 修改语言
LANGUAGE_CODE = 'zh-Hans'
# 设置时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# 访问上传文件访问的的跟路径
MEDIA_URL = '/media/'
# 配置文件上传的跟目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 缓存的配置
# pip install django-redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存的连接地址  指定索引为0数据库
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'TIMEOUT': 300,
        'OPTIONS': {
            # 'PASSWORD':''
        }
    },
    # 'session_cache': {
    #     'BACKEND': 'django_redis.cache.RedisCache',
    #     # 缓存的连接地址  指定索引为0数据库
    #     'LOCATION': 'redis://127.0.0.1:6379/3',
    #     'TIMEOUT': 300,
    #     'OPTIONS': {
    #         # 'PASSWORD':''
    #     }
    # }
}
# 设置 redis存储session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# 用户认证相关的
# 邮件的相关的配置
# session默认相关的配置
