import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'csv'}
    USER_DATABASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'user_data.db')
    METRICS_DATABASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'solar_data.db')

