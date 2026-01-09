from flask import Blueprint, jsonify
from app.models.product import Product
from datetime import datetime

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('', methods=['GET'])
def get_products():
    """Get a list of products - simulated data for demonstration."""
    # Simulate product data; in prod this would query a database
    mock_products = [
        Product(
            id=f'prod-{i}',
            name=f'Product {i}',
            description=f'Description for product {i}',
            price=round(10.0 + i * 2.5, 2),
            stock_quantity=100 - i * 5,
            created_at=datetime.utcnow()
        ) for i in range(1, 6)
    ]

    return jsonify({
        'products': [product.to_dict() for product in mock_products],
        'total_count': len(mock_products),
        'timestamp': datetime.utcnow().isoformat()
    })

@products_bp.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    """Get details of a specific product by ID - simulated data for demonstration."""
    # Simulate fetching a single product; in prod this would query a database
    product = Product(
        id=product_id,
        name=f'Product {product_id.split("-")[-1]}',
        description=f'Description for product {product_id.split("-")[-1]}',
        price=round(10.0 + int(product_id.split("-")[-1]) * 2.5, 2),
        stock_quantity=100 - int(product_id.split("-")[-1]) * 5,
        created_at=datetime.utcnow()
    )

    return jsonify({
        'product': product.to_dict(),
        'timestamp': datetime.utcnow().isoformat()
    })

@products_bp.route('', methods=['POST'])
def create_product():
    """Create a new product - simulated action for demonstration."""
    # In prod, you would extract data from request and save to a database
    new_product = Product(
        id='prod-new',
        name='New Product',
        description='Description for new product',
        price=19.99,
        stock_quantity=50,
        created_at=datetime.utcnow()
    )

    return jsonify({
        'message': 'Product created successfully',
        'product': new_product.to_dict(),
        'timestamp': datetime.utcnow().isoformat()
    }), 201

@products_bp.route('/<product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product - simulated action for demonstration."""
    # In prod, you would extract data from request and update in a database
    updated_product = Product(
        id=product_id,
        name=f'Updated Product {product_id.split("-")[-1]}',
        description=f'Updated description for product {product_id.split("-")[-1]}',
        price=29.99,
        stock_quantity=75,
        created_at=datetime.utcnow()
    )

    return jsonify({
        'message': 'Product updated successfully',
        'product': updated_product.to_dict(),
        'timestamp': datetime.utcnow().isoformat()
    })

@products_bp.route('/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product - simulated action for demonstration."""
    # In prod, you would delete the product from a database

    return jsonify({
        'message': f'Product {product_id} deleted successfully',
        'timestamp': datetime.utcnow().isoformat()
    })