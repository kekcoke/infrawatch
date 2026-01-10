from flask import Blueprint, jsonify, request, g
from datetime import datetime, timezone
from app.models.product import Product
from app.services.products_service import ProductsService
from uuid import UUID, uuid4

products_bp = Blueprint('products', __name__)
service = ProductsService()

@products_bp.route('/', methods=['GET'])
def get_products():
    """Get a list of products - simulated data for demonstration."""
    # Simulate product data; in prod this would query a database

    result = service.get_all_products()

    return jsonify({
        'products': result,
        'total_count': len(result),
        'timestamp': datetime.now(timezone.utc).isoformat()
    }), 200

@products_bp.route('/<uuid:product_id>', methods=['GET'])
def get_product(product_id):
    """Get details of a specific product by ID - simulated data for demonstration."""
    # Simulate fetching a single product; in prod this would query a database
    
    product = service.get_product_by_id(product_id)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({
        'product': product.to_dict(),
        'timestamp': datetime.now(timezone.utc).isoformat()
    }), 200

@products_bp.route('/', methods=['POST'])
def create_product():
    """Create a new product - simulated action for demonstration."""
    payload = request.get_json(silent=True) #remove once validation present

    if not payload:
        return jsonify({"error": "Invalid JSON body"}), 400
    
    try:
        product = Product(
            id= uuid4(), # delegate to ORM
            name=payload['name'],
            price=payload['price'],
            description=payload['description'],
            category=payload['category'],
            stock_quantity=payload['stock_quantity'],
            created_at=datetime.now(timezone.utc), # delegate to ORM model
            updated_at=datetime.now(timezone.utc),
    )
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({"error": "Invalid request payload"}), 400

    try:
        result = service.create_product(product)

    except Exception as e:
        print(e)
        return jsonify({"error": 'Error creating product'}), 500

    return jsonify({
        'message': 'Product created successfully',
        'product': result.to_dict(),
        'timestamp': datetime.now(timezone.utc).isoformat()
    }), 201

@products_bp.route('/<uuid:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product - simulated action for demonstration."""
    payload = request.get_json()

    if not payload:
        return jsonify({"error": "Request body must be JSON"}), 400

    try:
        updated_product = Product(
            id=product_id,
            name=payload['name'],
            price=payload['price'],
            description=payload['description'],
            category=payload['category'],
            stock_quantity=payload['stock_quantity'],
            updated_at=datetime.now(timezone.utc),
        )
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Invalid request payload"}), 400

    result = service.update_product(product_id, updated_product)

    if result is None:
        return jsonify({'error': 'Product not found'}), 404

    return jsonify(result.to_dict()), 200

@products_bp.route('/<uuid:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    deleted = service.delete_product(product_id)

    if not deleted:
        return jsonify({'error': 'Product not found'}), 404

    return '', 204

@products_bp.route("/multiple", methods=['DELETE'])
def delete_products():
    product_ids = request.json['product_ids']
    service.delete_products(product_ids)
    return "", 204