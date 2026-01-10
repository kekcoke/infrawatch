# app/services/categories_service.py
from datetime import datetime, timezone
import uuid
import random
from typing import List, Optional
from app.models.category import Category

class CategoriesService:
    """Service layer for category-related operations"""

    def __init__(self):
        # Initialize with sample categories as dictionary
        self.categories = { 
            1 : {
                "name": "Electronics",
                "description": "Electronic gadgets and devices",
                "created_at": datetime.now(timezone.utc)
            },
            2 : {
                "name": "Books",
                "description": "Various kinds of books and literature",
                "created_at": datetime.now(timezone.utc)
            },
            3 : {
                "name": "Clothing",
                "description": "Apparel and accessories",
                "created_at": datetime.now(timezone.utc)
            },
            4: {
                "name": "Home",
                "description": "Home appliances and furniture",
                "created_at": datetime.now(timezone.utc)
            },
            5: {
                "name": "Sports",
                "description": "Sporting goods and outdoor equipment",
                "created_at": datetime.now(timezone.utc)
            }
        }
        
        temp_categories_array= [
            {
                "id": 1,
                "name": "Electronics",
                "description": "Electronic gadgets and devices",
                "created_at": datetime.now(timezone.utc)
            },
            {
                "id": 2,
                "name": "Books",
                "description": "Various kinds of books and literature",
                "created_at": datetime.now(timezone.utc)
            },
            {
                "id": 3,
                "name": "Clothing",
                "description": "Apparel and accessories",
                "created_at": datetime.now(timezone.utc)
            },  
            {
                "id": 4,
                "name": "Home",
                "description": "Home appliances and furniture",
                "created_at": datetime.now(timezone.utc)
            },
            {
                "id": 5,
                "name": "Sports",
                "description": "Sporting goods and outdoor equipment",
                "created_at": datetime.now(timezone.utc)
            }
        ]
        # Convert to dictionary with id as key
        self.categories = {cat["id"]: Category(**cat) for cat in temp_categories_array}

    def get_all_categories(self) -> List[Category]:
        """Retrieve all categories"""
        return list(self.categories.values())

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        """Retrieve a category by its ID"""
        if category_id not in self.categories:
            raise KeyError(f"Category with key {category_id} not found")
        return self.categories[category_id]

    def create_category(self, name: str, description: str) -> Category:
        """Create a new category"""
        category_id = self.categories.__len__() + 1
        new_category = Category(
            id=category_id,
            name=name,
            description=description,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        self.categories[category_id] = new_category
        return new_category

    def update_category(self, category_id: int, name: str, description: str) -> Optional[Category]:
        """Update an existing category"""
        category = self.categories.get(category_id)
        if category:
            category.name = name
            category.description = description
            category.updated_at = datetime.now(timezone.utc)
            return category
        return None
    
    def delete_category(self, category_id: int) -> bool:
        """Delete a category by its ID"""
        if category_id in self.categories:
            del self.categories[category_id]
            return True
        return False