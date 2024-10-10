from flask import Flask, request, jsonify
import requests
import google.generativeai as genai
import os

app = Flask(__name__)

# Configuração da API Gemini
API_KEY = 'AIzaSyC3Jfet2c3Q28eU7BNDskRa_05rT0EvkcU'
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyC3Jfet2c3Q28eU7BNDskRa_05rT0EvkcU'

# Rota para exibir a página HTML
@app.route('/templates')
def index():
    return render_template('index.html')  # Renderiza o arquivo index.html

# Rota para buscar filmes
@app.route('/buscar', methods=['POST'])
def buscar_filmes():
    dados = request.json
    
    genero = dados.get('genero')
    faixa_etaria = dados.get('faixa_etaria')
    ano = dados.get('ano')
    
    # Configurar parâmetros para a requisição à API Gemini
    params = {
        'genre': genero,
        'age_rating': faixa_etaria,
        'release_year': ano,
        'api_key': API_KEY
    }

    # Requisição GET para a API Gemini
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        # Retornar os dados de filmes para o frontend
        filmes = response.json()
        return jsonify(filmes)
    else:
        return jsonify({'error': 'Não foi possível buscar os filmes no momento.'}), 500

if __name__ == '__main__':
    app.run(debug=True)