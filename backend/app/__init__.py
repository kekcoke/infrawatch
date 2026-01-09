# backend/app/__init__.py
from flask import Flask
from app.core.config import Config
from app.api.v1 import health_bp, infrastructure_bp, metrics_bp, products_bp
from app.core.middleware.request_timer import request_timer
from app.models.infrastructure import Metrics


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

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
    app.register_blueprint(products_bp, url_prefix='/api/v1')

    return app