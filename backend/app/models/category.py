# backend/app/models/category.py
from datetime import datetime, timezone
from dataclasses import dataclass, field

def utc_now():
    return datetime.now(timezone.utc)

@dataclass
class Category:
    """Represents a product category in the system"""
    id: str
    name: str
    description: str
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)