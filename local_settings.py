# Пример local_settings
# Измените данные на свои

DEBUG = True
ALLOWED_HOSTS = ['*']

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

TINKOFF_API_KEY = 'your-api-key'
ENDPOINT_TINKOFF = 'your-secret-key'
API_KEY_TINKOFF = 'your-api-key'
SECRET_KEY_TINKOFF = 'your-secret-key'
NGROK_URL = 'http://localhost:8000'
OPEN_AI_API_KEY = 'your-api-key'


APP_SETTINGS = LocalSettingsClass(
    portal_domain='b24-ltn86p.bitrix24.ru',
    app_domain='127.0.0.1:8000',
    app_name='bitrix_app',
    salt='wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF',
    secret_key='wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf',
    application_bitrix_client_id='local.688369a2aadbc2.95607662',
    application_bitrix_client_secret='9gko35Fk5u3yi3CDiZLs7770i3T1H4YxiLPYnsL640M0daIk1y',
    application_index_path='/',
)

DOMAIN = "56218ef983f3-8301993767665431593.ngrok-free.app"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bitrix_app',
        'USER': 'bitrix_user',
        'PASSWORD': 'PvXRiXd+J6rkCWiTEWd4mQ',
        'HOST': 'localhost',
        'PORT': '5433'
    },
}