import json
import os

import requests
from flask import Blueprint, request, Response, jsonify
from flask_cors import CORS

from config import app, pharma_engine

blueprint = Blueprint('app', __name__, url_prefix='/idrugs-app')

CORS(app)

# USER
@blueprint.route('/pharma/product', methods=['POST', 'PUT', 'DELETE', 'GET'])
def CRUD_product_route():
    url = pharma_engine + 'product'
    print("User: ")
    print(url)
    if request.method == 'POST':
        data = json.dumps(request.json)
        response = requests.post(url, json=data)
    elif request.method == 'PUT':
        data = json.dumps(request.json)
        response = requests.put(url, json=data)
    elif request.method == 'DELETE':
        data = json.dumps(request.json)
        response = requests.delete(url, json=data)
    elif request.method == 'GET':
        data = json.dumps(request.args)
        response = requests.get(url, json=data)
    return Response(response, mimetype='application/json', status=response.status_code)

@blueprint.route('/pharma/user', methods=['POST', 'PUT', 'DELETE', 'GET'])
def CRUD_user_route():
    url = pharma_engine + 'user'
    print("User: ")
    print(url)
    if request.method == 'POST':
        data = json.dumps(request.json)
        response = requests.post(url, json=data)
    elif request.method == 'PUT':
        data = json.dumps(request.json)
        response = requests.put(url, json=data)
    elif request.method == 'DELETE':
        data = json.dumps(request.json)
        response = requests.delete(url, json=data)
    elif request.method == 'GET':
        data = json.dumps(request.args)
        response = requests.get(url, json=data)
    return Response(response, mimetype='application/json', status=response.status_code)

@blueprint.route('/pharma/type', methods=['POST', 'PUT', 'DELETE', 'GET'])
def CRUD_type_route():
    url = pharma_engine + 'type'
    print("User: ")
    print(url)
    if request.method == 'POST':
        data = json.dumps(request.json)
        response = requests.post(url, json=data)
    elif request.method == 'PUT':
        data = json.dumps(request.json)
        response = requests.put(url, json=data)
    elif request.method == 'DELETE':
        data = json.dumps(request.json)
        response = requests.delete(url, json=data)
    elif request.method == 'GET':
        data = json.dumps(request.args)
        response = requests.get(url, json=data)
    return Response(response, mimetype='application/json', status=response.status_code)

@app.route('/')
def status():
    return jsonify({"message": "IDRUGS-APP: Aplicação rodando na porta 8080. CORS ativo"})

app.register_blueprint(blueprint)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)