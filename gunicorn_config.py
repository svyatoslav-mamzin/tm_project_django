command = '/home/mamzin/code/tm_project_django/venv/bin/gunicorn'
pythonpath = '/home/mamzin/code/tm_project_django/'
bind = '127.0.0.1:8001'
workers = 5
user = 'mamzin'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=tm_project_django.settings'

