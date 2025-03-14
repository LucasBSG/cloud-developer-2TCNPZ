# app.py - Microserviço de Avaliações (versão simplificada)
from flask import Flask, jsonify, request
from datetime import datetime

# Inicialização da aplicação Flask
app = Flask(__name__)

# Dados de exemplo
sample_reviews = [
    {
        "id": "rev-001",
        "product_id": "prod-001",
        "user_id": "user-001",
        "title": "Smartphone excelente!",
        "comment": "Comprei este smartphone e estou muito satisfeito. A câmera é incrível e a bateria dura o dia todo.",
        "rating": 5,
        "review_date": "2023-01-15T14:30:00",
        "photos": ["https://example.com/photos/review1-1.jpg", "https://example.com/photos/review1-2.jpg"],
        "helpfulness": {"likes": 12, "dislikes": 2},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"camera": 5, "battery": 4, "design": 5, "performance": 4}
    },
    {
        "id": "rev-002",
        "product_id": "prod-001",
        "user_id": "user-002",
        "title": "Bom, mas com alguns problemas",
        "comment": "O smartphone é bom, mas esquenta muito quando uso por muito tempo. A câmera é excelente!",
        "rating": 3,
        "review_date": "2023-02-20T10:15:00",
        "photos": [],
        "helpfulness": {"likes": 5, "dislikes": 1},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"camera": 5, "battery": 2, "design": 4, "performance": 3}
    },
    {
        "id": "rev-003",
        "product_id": "prod-002",
        "user_id": "user-003",
        "title": "Notebook perfeito para trabalho",
        "comment": "Comprei para trabalho e atendeu todas as expectativas. Rápido e com boa duração de bateria.",
        "rating": 5,
        "review_date": "2023-03-05T16:45:00",
        "photos": ["https://example.com/photos/review3-1.jpg"],
        "helpfulness": {"likes": 8, "dislikes": 0},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"performance": 5, "battery": 4, "design": 5, "keyboard": 4}
    },
    {
        "id": "rev-004",
        "product_id": "prod-003",
        "user_id": "user-004",
        "title": "Camiseta de boa qualidade",
        "comment": "O material é bom e não desbotou após várias lavagens. Recomendo!",
        "rating": 4,
        "review_date": "2023-02-28T09:30:00",
        "photos": [],
        "helpfulness": {"likes": 3, "dislikes": 0},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"quality": 4, "comfort": 5, "sizing": 4}
    },
    {
        "id": "rev-005",
        "product_id": "prod-001",
        "user_id": "user-005",
        "title": "Aguardando moderação",
        "comment": "Esta é uma avaliação que ainda não foi moderada.",
        "rating": 2,
        "review_date": "2023-03-10T11:20:00",
        "photos": [],
        "helpfulness": {"likes": 0, "dislikes": 0},
        "status": "pending",
        "verified_purchase": False,
        "attributes": {"camera": 2, "battery": 3, "design": 2, "performance": 2}
    }
]

# Respostas às avaliações
sample_responses = [
    {
        "id": "resp-001",
        "review_id": "rev-002",
        "user_id": "seller-001",
        "comment": "Agradecemos seu feedback. O aquecimento pode ocorrer em uso intenso. Sugerimos atualizar o software para a versão mais recente que melhorou este aspecto.",
        "response_date": "2023-02-22T14:30:00",
        "is_seller": True,
        "status": "active"
    },
    {
        "id": "resp-002",
        "review_id": "rev-003",
        "user_id": "user-006",
        "comment": "Concordo totalmente! Também uso para trabalho e é excelente.",
        "response_date": "2023-03-07T10:15:00",
        "is_seller": False,
        "status": "active"
    }
]

# Resumo de avaliações por produto
sample_summaries = {
    "prod-001": {
        "product_id": "prod-001",
        "average_rating": 4.0,
        "total_reviews": 3,
        "distribution": {"5": 1, "4": 0, "3": 1, "2": 1, "1": 0},
        "attribute_averages": {"camera": 4.0, "battery": 3.0, "design": 3.67, "performance": 3.0},
        "last_updated": "2023-03-10T11:20:00"
    },
    "prod-002": {
        "product_id": "prod-002",
        "average_rating": 5.0,
        "total_reviews": 1,
        "distribution": {"5": 1, "4": 0, "3": 0, "2": 0, "1": 0},
        "attribute_averages": {"performance": 5.0, "battery": 4.0, "design": 5.0, "keyboard": 4.0},
        "last_updated": "2023-03-05T16:45:00"
    },
    "prod-003": {
        "product_id": "prod-003",
        "average_rating": 4.0,
        "total_reviews": 1,
        "distribution": {"5": 0, "4": 1, "3": 0, "2": 0, "1": 0},
        "attribute_averages": {"quality": 4.0, "comfort": 5.0, "sizing": 4.0},
        "last_updated": "2023-02-28T09:30:00"
    }
}

# Rotas do microserviço

@app.route('/avaliacoes/produtos/<product_id>', methods=['GET'])
def get_product_reviews(product_id):
    """
    Retorna as avaliações de um produto
    """
    # Parâmetros opcionais
    status = request.args.get('status', 'approved')  # Por padrão, retorna apenas aprovadas
    
    # Filtra as avaliações
    if status == 'all':
        reviews = [r for r in sample_reviews if r['product_id'] == product_id]
    else:
        reviews = [r for r in sample_reviews if r['product_id'] == product_id and r['status'] == status]
    
    # Para cada avaliação, adiciona suas respostas
    reviews_with_responses = []
    for review in reviews:
        review_data = dict(review)
        review_data['responses'] = [r for r in sample_responses if r['review_id'] == review['id'] and r['status'] == 'active']
        reviews_with_responses.append(review_data)
    
    return jsonify({
        'reviews': reviews_with_responses,
        'total': len(reviews_with_responses),
        'product_id': product_id
    })

@app.route('/avaliacoes/produtos/<product_id>/resumo', methods=['GET'])
def get_product_review_summary(product_id):
    """
    Retorna o resumo de avaliações de um produto
    """
    if product_id not in sample_summaries:
        return jsonify({
            'product_id': product_id,
            'average_rating': 0,
            'total_reviews': 0,
            'distribution': {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0},
            'attribute_averages': {},
            'message': 'Produto sem avaliações'
        })
    
    return jsonify(sample_summaries[product_id])

@app.route('/avaliacoes', methods=['POST'])
def create_review():
    """
    Simula a criação de uma nova avaliação
    """
    data = request.get_json()
    
    # Validação básica
    required_fields = ['id', 'product_id', 'user_id', 'title', 'rating']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo obrigatório ausente: {field}'}), 400
    
    # Validação de classificação
    if not 1 <= data['rating'] <= 5:
        return jsonify({'error': 'Classificação deve ser entre 1 e 5'}), 400
    
    # Simula a criação (em um sistema real, salvaria no banco de dados)
    # Todas as avaliações começam como pendentes para moderação
    review_data = {
        'id': data['id'],
        'product_id': data['product_id'],
        'user_id': data['user_id'],
        'title': data['title'],
        'comment': data.get('comment', ''),
        'rating': data['rating'],
        'review_date': datetime.now().isoformat(),
        'photos': data.get('photos', []),
        'helpfulness': {"likes": 0, "dislikes": 0},
        'status': 'pending',
        'verified_purchase': data.get('verified_purchase', False),
        'attributes': data.get('attributes', {})
    }
    
    # Em um sistema real, adicionaríamos à base de dados
    # sample_reviews.append(review_data)
    
    return jsonify({
        'id': data['id'],
        'message': 'Avaliação criada com sucesso, aguardando moderação',
        'status': 'pending'
    }), 201

@app.route('/avaliacoes/<review_id>/aprovar', methods=['PUT'])
def approve_review(review_id):
    """
    Simula a aprovação de uma avaliação pendente
    """
    review = next((r for r in sample_reviews if r['id'] == review_id), None)
    if not review:
        return jsonify({'error': 'Avaliação não encontrada'}), 404
    
    if review['status'] != 'pending':
        return jsonify({'error': 'Apenas avaliações pendentes podem ser aprovadas'}), 400
    
    # Simula a aprovação (em um sistema real, atualizaria no banco de dados)
    # review['status'] = 'approved'
    
    return jsonify({'message': 'Avaliação aprovada com sucesso'})

@app.route('/avaliacoes/<review_id>/rejeitar', methods=['PUT'])
def reject_review(review_id):
    """
    Simula a rejeição de uma avaliação pendente
    """
    review = next((r for r in sample_reviews if r['id'] == review_id), None)
    if not review:
        return jsonify({'error': 'Avaliação não encontrada'}), 404
    
    if review['status'] != 'pending':
        return jsonify({'error': 'Apenas avaliações pendentes podem ser rejeitadas'}), 400
    
    # Simula a rejeição (em um sistema real, atualizaria no banco de dados)
    # review['status'] = 'rejected'
    
    return jsonify({'message': 'Avaliação rejeitada com sucesso'})

@app.route('/avaliacoes/<review_id>/respostas', methods=['POST'])
def create_review_response(review_id):
    """
    Simula a adição de uma resposta a uma avaliação
    """
    review = next((r for r in sample_reviews if r['id'] == review_id), None)
    if not review:
        return jsonify({'error': 'Avaliação não encontrada'}), 404
    
    data = request.get_json()
    
    # Validação básica
    required_fields = ['id', 'user_id', 'comment']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo obrigatório ausente: {field}'}), 400
    
    # Simula a criação da resposta (em um sistema real, salvaria no banco de dados)
    response_data = {
        'id': data['id'],
        'review_id': review_id,
        'user_id': data['user_id'],
        'comment': data['comment'],
        'response_date': datetime.now().isoformat(),
        'is_seller': data.get('is_seller', False),
        'status': 'active'
    }
    
    # Em um sistema real, adicionaríamos à base de dados
    # sample_responses.append(response_data)
    
    return jsonify({
        'id': data['id'],
        'message': 'Resposta adicionada com sucesso'
    }), 201

@app.route('/avaliacoes/<review_id>/utilidade', methods=['PATCH'])
def update_review_helpfulness(review_id):
    """
    Simula a atualização da utilidade de uma avaliação (likes/dislikes)
    """
    review = next((r for r in sample_reviews if r['id'] == review_id), None)
    if not review:
        return jsonify({'error': 'Avaliação não encontrada'}), 404
    
    data = request.get_json()
    current_helpfulness = dict(review['helpfulness'])
    
    if 'likes' in data:
        current_helpfulness['likes'] = data['likes']
    if 'dislikes' in data:
        current_helpfulness['dislikes'] = data['dislikes']
    
    # Simula a atualização (em um sistema real, atualizaria no banco de dados)
    # review['helpfulness'] = current_helpfulness
    
    return jsonify({
        'helpfulness': current_helpfulness,
        'message': 'Utilidade atualizada com sucesso'
    })

@app.route('/avaliacoes/usuarios/<user_id>', methods=['GET'])
def get_user_reviews(user_id):
    """
    Retorna todas as avaliações de um usuário
    """
    reviews = [r for r in sample_reviews if r['user_id'] == user_id]
    
    return jsonify([{
        'id': review['id'],
        'product_id': review['product_id'],
        'title': review['title'],
        'rating': review['rating'],
        'review_date': review['review_date'],
        'status': review['status']
    } for review in reviews])

@app.route('/avaliacoes/pendentes', methods=['GET'])
def get_pending_reviews():
    """
    Retorna todas as avaliações pendentes de moderação
    """
    reviews = [r for r in sample_reviews if r['status'] == 'pending']
    
    return jsonify([{
        'id': review['id'],
        'product_id': review['product_id'],
        'user_id': review['user_id'],
        'title': review['title'],
        'comment': review['comment'],
        'rating': review['rating'],
        'review_date': review['review_date']
    } for review in reviews])

# Rota para verificar a saúde do serviço
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificação de saúde do serviço
    """
    return jsonify({'status': 'ok', 'service': 'reviews'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6003)