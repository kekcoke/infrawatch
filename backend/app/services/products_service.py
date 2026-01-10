# backend/app/services/products_service.py

from datetime import datetime, timezone
import uuid 
import random
from typing import List
from app.models.product import Product

class ProductsService:
    """Service layer for product-related operations"""

    def __init__(self):
        self.products = [
            Product(
                id= uuid.UUID("d5496969-b666-430f-91e9-a3a910a36a2f"),
                name="A",
                price=45.55,
                description="A product",
                category=1,
                stock_quantity=5,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            ),
            Product(
                id= uuid.UUID("2ae80eca-fdb1-4d25-9922-483e2ee8567e"),
                name="B",
                price=55.55,
                description="A product",
                category=1,
                stock_quantity=5,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
        ]

    def get_all_products(self) -> List[Product]:
        """Retrieve all products. Note this can be paginated/filters in the future"""
        return list(self.products)
    
    def get_product_by_id(self, product_id: uuid):
        """Retrieve product by id"""
        product = next(product for product in self.products 
                       if product.id == product_id)
        if not product:
            return None

        return product
    
    def create_product(self, product: Product) -> Product:
        """Adds product to inventory"""

        self.products.append(product)

        return product
    
    def update_product(self, product_id: uuid.UUID, product: Product) -> Product | None:
        product_index = next(
            (i for i, existing in enumerate(self.products)
            if existing.id == product_id),
            -1
        )

        if product_index == -1:
            return None

        existing = self.products[product_index]
        product.created_at = existing.created_at

        self.products[product_index] = product
        return product
        
    def delete_product(self, product_id: uuid) -> bool:
        """Delete a category by its id"""
        product_index = next(
            (i for i, product in enumerate(self.products)
            if product.id == product_id),
            -1
        )

        if product_index != -1:
            self.products.pop(product_index)
            return True

        return False
        
    def delete_products(self, product_ids: list[uuid.UUID]) -> bool:
        return True
