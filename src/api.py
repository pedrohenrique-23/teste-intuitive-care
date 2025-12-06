from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Libera acesso para o Frontend (Vue.js)

# Configuração do Banco de Dados
# Se sua senha for diferente de 'root', altere aqui
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'intuitive_db'
}

def get_db_connection():
    """Abre uma conexão com o banco a cada requisição."""
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/operadoras', methods=['GET'])
def buscar_operadoras():
    # Pega o termo digitado na URL (ex: /operadoras?q=unimed)
    search_term = request.args.get('q', '')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) # dictionary=True faz o resultado vir como JSON bonitinho

    try:
        if search_term:
            # Busca textual: Procura no Nome Fantasia OU Razão Social
            query = """
                SELECT Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade 
                FROM operadoras 
                WHERE Razao_Social LIKE %s OR Nome_Fantasia LIKE %s 
                LIMIT 20
            """
            # O %s é substituído pelo termo de busca de forma segura
            params = (f"%{search_term}%", f"%{search_term}%")
            cursor.execute(query, params)
        else:
            # Se não digitar nada, retorna as 20 primeiras
            cursor.execute("SELECT Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia FROM operadoras LIMIT 20")

        results = cursor.fetchall()
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        # Sempre fecha a conexão para não travar o banco
        cursor.close()
        conn.close()

if __name__ == '__main__':
    # Roda o servidor na porta 5000
    print("🚀 Servidor rodando em http://localhost:5000")
    app.run(debug=True)