# SECRET KEY
SECRET_KEY = ''

# NUMBER OF RECIPES PER PAGE AT HOME
PER_PAGE = 9

# NUMBER OF RECIPES PER PAGE AT DASHBOARD
PER_PAGE_USER = 6

# 0 True - 1 False
DEBUG = 1

# 0 True - 1 False
SELENIUM_HEADLESS = 0

# ------ DATABASE SETTINGS ------
# FROM SQLite
DATABASE_ENGINE = 'django.db.beckends.sqlite3'
DATABASE_NAME = './db.sqlite3'

# FROM Postgres
DATABASE_ENGINE = 'django.db.beckends.postgresql'
DATABASE_NAME = 'database'
DATABASE_USER = 'user'
DATABASE_PASSWORD = 'password'
DATABASE_HOST = 'host'
DATABASE_PORT = 'port'