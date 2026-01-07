# backend/app/core/config.py
import os 
from datetime import timedelta

class Config:
    """Production-ready configuration management"""
    SECRET_KEY = os.environ.get('SECRET_KEY' or 'dev-secret-key-change-me-in-production')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL' or 'sqlite:///infrawatch.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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

class ProductionConfig(Config):
    """Production configuration with enhanced security"""
    DEBUG = False
    # SESSION_COOKIE_SECURE = True
    # REMEMBER_COOKIE_SECURE = True
    # PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

class TestingConfig(Config):
    """Testing configuration with in-memory database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
