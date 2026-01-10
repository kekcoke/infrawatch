# backend/app/api/v1/categories/routes.py
from flask import Blueprint, jsonify, request
from app.models.category import Category
from app.services.categories_service import CategoriesService

categories_bp = Blueprint('categories', __name__)
service = CategoriesService()

@categories_bp.route('/', methods=['GET'])
def get_categories():
    """Endpoint to retrieve all product categories."""
    categories = service.get_all_categories()
    return jsonify([category.__dict__ for category in categories])

@categories_bp.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """Endpoint to retrieve a specific category by ID."""
    category = service.get_category_by_id(category_id)
    if category is None:
        return jsonify({'error': 'Category not found'}), 404

    return jsonify(category), 200
    
@categories_bp.route('/', methods=['POST'])
def create_category():
    """Endpoint to create a new product category."""
    data = request.get_json()
    new_category = service.create_category(
        name=data.get('name'),
        description=data.get('description')
    )
    return jsonify(new_category), 201

@categories_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """Endpoint to update an existing product category."""
    data = request.get_json()
    updated_category = service.update_category(
        category_id,
        name=data.get('name'),
        description=data.get('description')
    )
    if updated_category is None:
        return jsonify({'error': 'Category not found'}), 404

    return jsonify(updated_category)
    
@categories_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Endpoint to delete a product category."""
    success = service.delete_category(category_id)
    if success is None or False:
        return jsonify({'error': 'Category not found'}), 404
    
    return jsonify({'message': 'Category deleted successfully'})
