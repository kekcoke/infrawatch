# backend/app/__init__.py
import os
from flask import Flask
from flask_cors import CORS
from app.core.config import Config
from app.api.v1 import (
    health_bp,
    infrastructure_bp,
    metrics_bp,
)
from app.api.v1.products import products_bp
from app.api.v1.categories.routes import categories_bp
from app.core.middleware.request_timer import request_timer
from app.models.infrastructure import Metrics


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Configure CORS based on environment
    configure_cors(app)

    # Instantiate infra-level services
    metrics = Metrics(
        metric_type="infra",
        metric_name="request_duration_seconds",
        source="request_timer",
        window_seconds=60)

    # Register middleware
    request_timer(app, metrics)

    # Register Blueprints
    app.register_blueprint(health_bp, url_prefix='/api/v1')
    app.register_blueprint(infrastructure_bp, url_prefix='/api/v1')
    app.register_blueprint(metrics_bp, url_prefix='/api/v1')
    app.register_blueprint(products_bp, url_prefix='/api/v1/products')
    app.register_blueprint(categories_bp, url_prefix='/api/v1/categories')

    print(app.url_map)

    return app

def configure_cors(app):
    """
    Configure CORS based on environment.
    Development: Allow all origins
    Production: Restrict to specific origins
    """
    flask_env = os.getenv('FLASK_ENV', 'production')
    
    if flask_env == 'development':
        # Development: Allow all origins for easier testing
        CORS(app, resources={
            r"/api/*": {
                "origins": "*",
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "expose_headers": ["Content-Range", "X-Content-Range"],
                "supports_credentials": False,
                "max_age": 3600
            }
        })
        app.logger.info("CORS enabled for development - allowing all origins")
    else:
        # Production: Restrict to specific origins
        allowed_origins = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')
        allowed_origins = [origin.strip() for origin in allowed_origins if origin.strip()]
        
        if not allowed_origins:
            app.logger.warning("No CORS_ALLOWED_ORIGINS set in production!")
            allowed_origins = []
        
        CORS(app, resources={
            r"/api/*": {
                "origins": allowed_origins,
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "expose_headers": ["Content-Range", "X-Content-Range"],
                "supports_credentials": True,  # Enable for production with proper auth
                "max_age": 3600
            }
        })
        app.logger.info(f"CORS enabled for production - allowed origins: {allowed_origins}")