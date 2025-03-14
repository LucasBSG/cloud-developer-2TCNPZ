# app.py - Microserviço de Categorias (versão simplificada)
from flask import Flask, jsonify

# Inicialização da aplicação Flask
app = Flask(__name__)

# Dados de exemplo
sample_categories = [
    {
        "id": "cat-001",
        "name": "Eletrônicos",
        "description": "Produtos eletrônicos em geral",
        "image_url": "https://example.com/images/electronics.jpg",
        "parent_id": None,
        "level": 1,
        "status": "active",
        "url_slug": "eletronicos"
    },
    {
        "id": "cat-002",
        "name": "Smartphones",
        "description": "Telefones celulares inteligentes",
        "image_url": "https://example.com/images/smartphones.jpg",
        "parent_id": "cat-001",
        "level": 2,
        "status": "active",
        "url_slug": "smartphones"
    },
    {
        "id": "cat-003",
        "name": "Roupas",
        "description": "Vestuário em geral",
        "image_url": "https://example.com/images/clothing.jpg",
        "parent_id": None,
        "level": 1,
        "status": "active",
        "url_slug": "roupas"
    }
]

# Rotas do microserviço

@app.route('/categories', methods=['GET'])
def get_all_categories():
    """
    Retorna todas as categorias
    """
    return jsonify(sample_categories)

@app.route('/categories/<category_id>', methods=['GET'])
def get_category(category_id):
    """
    Retorna uma categoria específica pelo ID
    """
    category = next((cat for cat in sample_categories if cat["id"] == category_id), None)
    if category:
        return jsonify(category)
    return jsonify({"error": "Categoria não encontrada"}), 404

@app.route('/categories/hierarquia', methods=['GET'])
def get_hierarchy():
    """
    Retorna a hierarquia de categorias
    """
    # Encontrar categorias raiz
    root_categories = [cat for cat in sample_categories if cat["parent_id"] is None]
    
    # Construir hierarquia
    result = []
    for root in root_categories:
        category_tree = {
            "id": root["id"],
            "name": root["name"],
            "url_slug": root["url_slug"],
            "subcategories": []
        }
        
        # Adicionar subcategorias
        for cat in sample_categories:
            if cat["parent_id"] == root["id"]:
                category_tree["subcategories"].append({
                    "id": cat["id"],
                    "name": cat["name"],
                    "url_slug": cat["url_slug"]
                })
        
        result.append(category_tree)
    
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificação de saúde do serviço
    """
    return jsonify({'status': 'ok', 'service': 'categories'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)