from flask import Flask, jsonify
from servidor_central import alertas

app = Flask(__name__)

@app.route('/alertas', methods=['GET'])
def listar_alertas():
    return jsonify(alertas)

if __name__ == "__main__":
    app.run(debug=True)