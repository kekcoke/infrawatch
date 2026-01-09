# backend/app/api/v1/categories/routes.py
from flask import Blueprint, jsonify, request
from app.models.category import Category
from app.services.categories_service import CategoriesService

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')

@categories_bp.route('/', methods=['GET'])
def get_categories():
    """Endpoint to retrieve all product categories."""
    service = CategoriesService()
    categories = service.get_all_categories()
    return jsonify([category.__dict__ for category in categories])

@categories_bp.route('/<category_id>', methods=['GET'])
def get_category(category_id):
    """Endpoint to retrieve a specific category by ID."""
    service = CategoriesService()
    category = service.get_category_by_id(category_id)
    if category:
        return jsonify(category.__dict__)
    else:
        return jsonify({'error': 'Category not found'}), 404
    
@categories_bp.route('/', methods=['POST'])
def create_category():
    """Endpoint to create a new product category."""
    data = request.get_json()
    service = CategoriesService()
    new_category = service.create_category(
        name=data.get('name'),
        description=data.get('description')
    )
    return jsonify(new_category.__dict__), 201

@categories_bp.route('/<category_id>', methods=['PUT'])
def update_category(category_id):
    """Endpoint to update an existing product category."""
    data = request.get_json()
    service = CategoriesService()
    updated_category = service.update_category(
        category_id,
        name=data.get('name'),
        description=data.get('description')
    )
    if updated_category:
        return jsonify(updated_category.__dict__)
    else:
        return jsonify({'error': 'Category not found'}), 404
    
@categories_bp.route('/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Endpoint to delete a product category."""
    service = CategoriesService()
    success = service.delete_category(category_id)
    if success:
        return jsonify({'message': 'Category deleted successfully'})
    else:
        return jsonify({'error': 'Category not found'}), 404
