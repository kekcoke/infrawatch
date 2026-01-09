# app/api/__init__.py
from .v1 import health_bp, infrastructure_bp, metrics_bp
from .v1.products import products_bp
from .v1.categories import categories_bp
__all__ = [
    "health_bp",
    "infrastructure_bp",
    "metrics_bp",
    "products_bp",
    "categories_bp",
]