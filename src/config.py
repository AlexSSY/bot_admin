import os

from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
TIME_ZONE = 'Europe/Kiev'
DB_NAME = 'db.sqlite3'

ADMIN = {
    'MODELS_PER_PAGE': 3,
    'RECORDS_PER_PAGE': 5,
    'READONLY_FIELDS': ('id', 'created_at', 'updated_at', )
}
