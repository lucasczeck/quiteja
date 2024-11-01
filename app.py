from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

tipos = pd.read_csv('script/tipos.csv')
tipos_dict = dict(zip(tipos['id'], tipos['nome']))


@app.route('/tipo/<int:id>', methods=['GET'])
def get_tipo(id):
    if id in tipos_dict:
        return jsonify({'id': id, 'nome': tipos_dict[id]}), 200
    else:
        return jsonify({'error': 'Type not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
