# backend/app/models/product.py
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
import uuid
    
def utc_now():
        return datetime.now(timezone.utc)
@dataclass
class Product:
    """Represents a product in the system"""
    id: uuid
    name: str
    price: float
    description: str
    category: int
    stock_quantity: int = 0
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    @property
    def inStock(self) -> bool:
        return self.stock_quantity > 0
    
    def to_dict(self):
        return asdict(self)