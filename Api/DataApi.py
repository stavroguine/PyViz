from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

engine = create_engine('mysql+mysqldb://root:root@localhost/Pyviz')
app = Flask(__name__)
api = Api(app)

class DataApi(Resource):
    #La methode get de l'api recupere chaque entree de la table choisie
    #retourne un fichier json
    def get(self):
        conn = engine.connect()
        query = conn.execute("select commune, occurrence from postes")
        result = {'postes': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(DataApi, '/youplaboum')

if __name__ == '__main__':
    app.run(port=1440)

