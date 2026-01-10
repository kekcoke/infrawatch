# backend/app/core/config.py
import os 
from datetime import timedelta

class Config:
    """Production-ready configuration management"""
    SECRET_KEY = os.environ.get('SECRET_KEY' or 'dev-secret-key-change-me-in-production')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL' or 'sqlite:///infrawatch.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = os.getenv('FLASK_DEBUG', '0') == '1'

    # Production-performance settings
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }

    # API versioning & rate limiting
    API_VERSION = 'v1'
    RATE_LIMIT_ENABLED = True

class DevelopmentConfig(Config):
    """Development configuration with debug settings"""
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    """Production configuration with enhanced security"""
    DEBUG = False
    FLASK_ENV = 'production'
    # SESSION_COOKIE_SECURE = True
    # REMEMBER_COOKIE_SECURE = True
    # PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

class TestingConfig(Config):
    """Testing configuration with in-memory database"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}