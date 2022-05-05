import urllib

from flask import Blueprint, request, Response

from config import app, pharma_engine
import json

import requests

blueprint = Blueprint('app', __name__, url_prefix='/idrugs-app')

# USER
@blueprint.route('/product', methods=['POST', 'PUT', 'DELETE', 'GET'])
def CRUD_product_route():
    url = pharma_engine + 'product'
    if request.method == 'POST':
        data = json.dumps(request.json)
        response = requests.post(url, data=data)
    elif request.method == 'PUT':
        data = json.dumps(request.json)
        response = requests.put(url, data=data)
    elif request.method == 'DELETE':
        data = json.dumps(request.json)
        response = requests.delete(url, data=data)
    elif request.method == 'GET':
        data = json.dumps(request.args)
        response = requests.get(url, data=data)
    return Response(response, mimetype='application/json', status=response.status_code)

@blueprint.route('/user', methods=['POST', 'PUT', 'DELETE', 'GET'])
def CRUD_user_route():
    url = pharma_engine + 'user'
    if request.method == 'POST':
        data = json.dumps(request.json)
        response = requests.post(url, data=data)
    elif request.method == 'PUT':
        data = json.dumps(request.json)
        response = requests.put(url, data=data)
    elif request.method == 'DELETE':
        data = json.dumps(request.json)
        response = requests.delete(url, data=data)
    elif request.method == 'GET':
        data = json.dumps(request.args)
        response = requests.get(url, data=data)
    return Response(response, mimetype='application/json', status=response.status_code)

@blueprint.route('/type', methods=['POST', 'PUT', 'DELETE', 'GET'])
def CRUD_type_route():
    url = pharma_engine + 'type'
    if request.method == 'POST':
        data = json.dumps(request.json)
        response = requests.post(url, data=data)
    elif request.method == 'PUT':
        data = json.dumps(request.json)
        response = requests.put(url, data=data)
    elif request.method == 'DELETE':
        data = json.dumps(request.json)
        response = requests.delete(url, data=data)
    elif request.method == 'GET':
        data = json.dumps(request.args)
        response = requests.get(url, data=data)
    return Response(response, mimetype='application/json', status=response.status_code)

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(port=8080, debug=True)