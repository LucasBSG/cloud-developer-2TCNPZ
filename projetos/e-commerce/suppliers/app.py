# app.py - Microserviço de Fornecedores (versão simplificada)
from flask import Flask, jsonify, request
from datetime import datetime

# Inicialização da aplicação Flask
app = Flask(__name__)

# Dados de exemplo
sample_suppliers = [
    {
        "id": "sup-001",
        "legal_name": "Tech Solutions Ltda",
        "trading_name": "TechSol",
        "tax_id": "12.345.678/0001-90",
        "email": "contato@techsol.com",
        "phone": "(11) 3456-7890",
        "address": {
            "street": "Av. Paulista",
            "number": "1000",
            "complement": "Sala 301",
            "neighborhood": "Bela Vista",
            "city": "São Paulo",
            "state": "SP",
            "zip_code": "01310-000",
            "country": "Brasil"
        },
        "status": "active",
        "registration_date": "2022-01-15T10:30:00",
        "representative": "João Silva",
        "payment_terms": "30 dias"
    },
    {
        "id": "sup-002",
        "legal_name": "Informática Global S.A.",
        "trading_name": "InfoGlobal",
        "tax_id": "23.456.789/0001-12",
        "email": "vendas@infoglobal.com",
        "phone": "(11) 2345-6789",
        "address": {
            "street": "Rua Vergueiro",
            "number": "500",
            "complement": "Andar 5",
            "neighborhood": "Liberdade",
            "city": "São Paulo",
            "state": "SP",
            "zip_code": "01504-000",
            "country": "Brasil"
        },
        "status": "active",
        "registration_date": "2022-03-10T14:15:00",
        "representative": "Maria Oliveira",
        "payment_terms": "15 dias"
    },
    {
        "id": "sup-003",
        "legal_name": "Vestuário Express Ltda",
        "trading_name": "VestEx",
        "tax_id": "34.567.890/0001-23",
        "email": "fornecedor@vestex.com",
        "phone": "(21) 3456-7891",
        "address": {
            "street": "Av. Rio Branco",
            "number": "150",
            "complement": "Loja 23",
            "neighborhood": "Centro",
            "city": "Rio de Janeiro",
            "state": "RJ",
            "zip_code": "20040-002",
            "country": "Brasil"
        },
        "status": "active",
        "registration_date": "2022-05-20T09:45:00",
        "representative": "Carlos Mendes",
        "payment_terms": "à vista"
    }
]

# Contatos de fornecedores
sample_contacts = [
    {
        "id": "cont-001",
        "supplier_id": "sup-001",
        "name": "João Silva",
        "position": "Gerente de Vendas",
        "email": "joao.silva@techsol.com",
        "phone": "(11) 98765-4321",
        "department": "Vendas",
        "is_primary": True
    },
    {
        "id": "cont-002",
        "supplier_id": "sup-001",
        "name": "Ana Santos",
        "position": "Suporte Técnico",
        "email": "ana.santos@techsol.com",
        "phone": "(11) 91234-5678",
        "department": "Suporte",
        "is_primary": False
    },
    {
        "id": "cont-003",
        "supplier_id": "sup-002",
        "name": "Maria Oliveira",
        "position": "Diretora Comercial",
        "email": "maria.oliveira@infoglobal.com",
        "phone": "(11) 99876-5432",
        "department": "Comercial",
        "is_primary": True
    }
]

# Entregas de fornecedores
sample_deliveries = [
    {
        "id": "del-001",
        "supplier_id": "sup-001",
        "delivery_date": "2023-03-15T14:00:00",
        "products": [
            {"product_id": "prod-001", "quantity": 20, "unit_price": 1800.00},
            {"product_id": "prod-002", "quantity": 10, "unit_price": 4200.00}
        ],
        "status": "completed",
        "invoice_number": "NF-12345",
        "notes": "Entrega realizada com sucesso"
    },
    {
        "id": "del-002",
        "supplier_id": "sup-002",
        "delivery_date": "2023-04-10T10:30:00",
        "products": [
            {"product_id": "prod-002", "quantity": 5, "unit_price": 4300.00}
        ],
        "status": "completed",
        "invoice_number": "NF-23456",
        "notes": "Entrega parcial, restante agendado para o próximo mês"
    },
    {
        "id": "del-003",
        "supplier_id": "sup-003",
        "delivery_date": "2023-05-01T09:00:00",
        "products": [
            {"product_id": "prod-003", "quantity": 100, "unit_price": 55.00}
        ],
        "status": "pending",
        "invoice_number": None,
        "notes": "Aguardando confirmação de recebimento"
    }
]

# Rotas do microserviço

@app.route('/suppliers', methods=['GET'])
def get_all_suppliers():
    """
    Retorna todos os fornecedores
    """
    return jsonify([{
        'id': supplier['id'],
        'legal_name': supplier['legal_name'],
        'trading_name': supplier['trading_name'],
        'tax_id': supplier['tax_id'],
        'email': supplier['email'],
        'status': supplier['status']
    } for supplier in sample_suppliers])

@app.route('/suppliers/<supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    """
    Retorna um fornecedor específico pelo ID
    """
    supplier = next((s for s in sample_suppliers if s['id'] == supplier_id), None)
    if supplier:
        return jsonify(supplier)
    return jsonify({'error': 'Fornecedor não encontrado'}), 404

@app.route('/suppliers', methods=['POST'])
def create_supplier():
    """
    Simula a criação de um novo fornecedor
    """
    data = request.get_json()
    
    # Validação básica
    required_fields = ['id', 'legal_name', 'tax_id', 'email', 'phone', 'address']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo obrigatório ausente: {field}'}), 400
    
    # Simula a criação (em um sistema real, salvaria no banco de dados)
    return jsonify({
        'id': data['id'],
        'message': 'Fornecedor criado com sucesso'
    }), 201

@app.route('/suppliers/ativos', methods=['GET'])
def get_active_suppliers():
    """
    Retorna todos os fornecedores ativos
    """
    active_suppliers = [s for s in sample_suppliers if s['status'] == 'active']
    return jsonify([{
        'id': supplier['id'],
        'legal_name': supplier['legal_name'],
        'trading_name': supplier['trading_name'],
        'email': supplier['email'],
        'phone': supplier['phone']
    } for supplier in active_suppliers])

@app.route('/suppliers/<supplier_id>/contacts', methods=['GET'])
def get_supplier_contacts(supplier_id):
    """
    Retorna todos os contatos de um fornecedor
    """
    # Verifica se o fornecedor existe
    supplier = next((s for s in sample_suppliers if s['id'] == supplier_id), None)
    if not supplier:
        return jsonify({'error': 'Fornecedor não encontrado'}), 404
    
    contacts = [c for c in sample_contacts if c['supplier_id'] == supplier_id]
    return jsonify(contacts)

@app.route('/suppliers/<supplier_id>/contacts', methods=['POST'])
def create_supplier_contact(supplier_id):
    """
    Simula a criação de um novo contato para um fornecedor
    """
    # Verifica se o fornecedor existe
    supplier = next((s for s in sample_suppliers if s['id'] == supplier_id), None)
    if not supplier:
        return jsonify({'error': 'Fornecedor não encontrado'}), 404
    
    data = request.get_json()
    
    # Validação básica
    required_fields = ['id', 'name', 'email', 'phone']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo obrigatório ausente: {field}'}), 400
    
    # Simula a criação (em um sistema real, salvaria no banco de dados)
    return jsonify({
        'id': data['id'],
        'message': 'Contato criado com sucesso'
    }), 201

@app.route('/suppliers/<supplier_id>/deliveries', methods=['GET'])
def get_supplier_deliveries(supplier_id):
    """
    Retorna todas as entregas de um fornecedor
    """
    # Verifica se o fornecedor existe
    supplier = next((s for s in sample_suppliers if s['id'] == supplier_id), None)
    if not supplier:
        return jsonify({'error': 'Fornecedor não encontrado'}), 404
    
    deliveries = [d for d in sample_deliveries if d['supplier_id'] == supplier_id]
    return jsonify(deliveries)

@app.route('/suppliers/<supplier_id>/deliveries', methods=['POST'])
def create_supplier_delivery(supplier_id):
    """
    Simula a criação de uma nova entrega para um fornecedor
    """
    # Verifica se o fornecedor existe
    supplier = next((s for s in sample_suppliers if s['id'] == supplier_id), None)
    if not supplier:
        return jsonify({'error': 'Fornecedor não encontrado'}), 404
    
    data = request.get_json()
    
    # Validação básica
    required_fields = ['id', 'delivery_date', 'products']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo obrigatório ausente: {field}'}), 400
    
    # Simula a criação (em um sistema real, salvaria no banco de dados)
    return jsonify({
        'id': data['id'],
        'message': 'Entrega criada com sucesso'
    }), 201

@app.route('/suppliers/<supplier_id>/pedidos', methods=['POST'])
def create_supplier_order(supplier_id):
    """
    Simula a criação de um novo pedido para um fornecedor
    """
    # Verifica se o fornecedor existe
    supplier = next((s for s in sample_suppliers if s['id'] == supplier_id), None)
    if not supplier:
        return jsonify({'error': 'Fornecedor não encontrado'}), 404
    
    data = request.get_json()
    
    # Validação básica
    if 'products' not in data:
        return jsonify({'error': 'Campo products é obrigatório'}), 400
    
    # Simula a criação de um pedido (em um sistema real, salvaria no banco de dados)
    order_id = f"order-{supplier_id.split('-')[1]}"
    
    return jsonify({
        'order_id': order_id,
        'supplier_id': supplier_id,
        'products': data['products'],
        'status': 'pending',
        'created_at': datetime.now().isoformat(),
        'message': 'Pedido criado com sucesso'
    }), 201

# Rota para verificar a saúde do serviço
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificação de saúde do serviço
    """
    return jsonify({'status': 'ok', 'service': 'suppliers'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6004)