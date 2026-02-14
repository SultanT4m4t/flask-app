import os


class Config:
    # Database connection
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # App settings
    FLASK_ENV = os.environ.get('FLASK_ENV', 'production')