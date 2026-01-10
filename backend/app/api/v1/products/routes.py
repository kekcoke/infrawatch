from flask import Blueprint, jsonify
from app.models.product import Product
from datetime import datetime, timezone

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    """Get a list of products - simulated data for demonstration."""
    # Simulate product data; in prod this would query a database
    mock_products = [
        Product(
            id=f'prod-{i}',
            name=f'Product {i}',
            price=round(10.0 + i * 2.5, 2),
            description=f'Description for product {i}',
            category="Electronics",
            stock_quantity=100 - i * 5,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        ) for i in range(1, 6)
    ]

    return jsonify({
        'products': [product.to_dict() for product in mock_products],
        'total_count': len(mock_products),
        'timestamp': datetime.now(timezone.utc).isoformat()
    })

@products_bp.route('/<uuid:product_id>', methods=['GET'])
def get_product(product_id):
    """Get details of a specific product by ID - simulated data for demonstration."""
    # Simulate fetching a single product; in prod this would query a database
    product = Product(
        id=product_id,
        name="Sample Product",
        price=19.99,
        description="Sample product description",
        category="Electronics",
        stock_quantity=100,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )

    return jsonify({
        'product': product.to_dict(),
        'timestamp': datetime.now(timezone.utc).isoformat()
    })

@products_bp.route('/', methods=['POST'])
def create_product():
    """Create a new product - simulated action for demonstration."""
    # In prod, you would extract data from request and save to a database
    new_product = Product(
        id='prod-new',
        name='New Product',
        price=19.99,
        description='Description for new product',
        category="Electronics",
        stock_quantity=100,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )

    return jsonify({
        'message': 'Product created successfully',
        'product': new_product.to_dict(),
        'timestamp': datetime.now(timezone.utc).isoformat()
    }), 201

@products_bp.route('/<uuid:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product - simulated action for demonstration."""
    # In prod, you would extract data from request and update in a database
    updated_product = Product(
        id=product_id,
        name=f'Updated Product ',
        price=29.99,
        description=f'Updated description for product {product_id}',
        category="Electronics",
        stock_quantity=75,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )

    return jsonify({
        'message': 'Product updated successfully',
        'product': updated_product.to_dict(),
        'timestamp': datetime.now(timezone.utc).isoformat()
    })

@products_bp.route('/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product - simulated action for demonstration."""
    # In prod, you would delete the product from a database

    return jsonify({
        'message': f'Product {product_id} deleted successfully',
        'timestamp': datetime.now(datetime.timezone.utc).isoformat()
    })