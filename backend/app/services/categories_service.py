# app/services/categories_service.py
from datetime import datetime
import uuid
from typing import List, Optional
from app.models.category import Category

class CategoriesService:
    """Service layer for category-related operations"""

    def __init__(self):
        # Initialize with sample categories as dictionary
        temp_categories = [
            {
                "id": str(uuid.uuid4()),
                "name": "Electronics",
                "description": "Electronic gadgets and devices",
                "created_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Books",
                "description": "Various kinds of books and literature",
                "created_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Clothing",
                "description": "Apparel and accessories",
                "created_at": datetime.utcnow()
            },  
            {
                "id": str(uuid.uuid4()),
                "name": "Home",
                "description": "Home appliances and furniture",
                "created_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Sports",
                "description": "Sporting goods and outdoor equipment",
                "created_at": datetime.utcnow()
            }
        ]
        # Convert to dictionary with id as key
        self.categories = {cat["id"]: Category(**cat) for cat in temp_categories}

    def get_all_categories(self) -> List[Category]:
        """Retrieve all categories"""
        return list(self.categories.values())

    def get_category_by_id(self, category_id: str) -> Optional[Category]:
        """Retrieve a category by its ID"""
        return self.categories.get(category_id)

    def create_category(self, name: str, description: str) -> Category:
        """Create a new category"""
        category_id = str(uuid.uuid4())
        new_category = Category(
            id=category_id,
            name=name,
            description=description,
            created_at=datetime.utcnow()
        )
        self.categories[category_id] = new_category
        return new_category

    def update_category(self, category_id: str, name: str, description: str) -> Optional[Category]:
        """Update an existing category"""
        category = self.categories.get(category_id)
        if category:
            category.name = name
            category.description = description
            category.updated_at = datetime.utcnow()
            return category
        return None
    
    def delete_category(self, category_id: str) -> bool:
        """Delete a category by its ID"""
        if category_id in self.categories:
            del self.categories[category_id]
            return True
        return False