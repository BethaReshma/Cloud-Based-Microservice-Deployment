from flask import Flask, jsonify, request
from datetime import datetime
import uuid
import os

app = Flask(__name__)

# In-memory storage for demonstration
items = {}

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask Microservice API", 
        "version": "1.0",
        "status": "healthy"
    })

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({"items": items, "count": len(items)})

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    item_id = str(uuid.uuid4())
    items[item_id] = {
        "id": item_id,
        "name": data['name'],
        "description": data.get('description', ''),
        "created_at": datetime.utcnow().isoformat()
    }
    return jsonify(items[item_id]), 201

@app.route('/api/items/<item_id>', methods=['GET'])
def get_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(items[item_id])

@app.route('/api/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()
    if 'name' in data:
        items[item_id]['name'] = data['name']
    if 'description' in data:
        items[item_id]['description'] = data['description']
    
    return jsonify(items[item_id])

@app.route('/api/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    
    del items[item_id]
    return jsonify({"message": "Item deleted successfully"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
