# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@172.22.0.2:5432/'