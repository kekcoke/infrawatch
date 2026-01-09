# backend/app/models/category.py
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Category:
    """Represents a product category in the system"""
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime = field(default_factory=datetime.utcnow)