# backend/app/models/product.py
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Product:
    """Represents a product in the system"""
    id: str
    name: str
    price: float
    description: str
    category: str
    inStock: bool
    stock_quantity: int
    created_at: datetime
    updated_at: datetime = field(default_factory=datetime.utcnow)
