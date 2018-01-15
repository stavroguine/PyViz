import json
import MySQLdb
import requests
import pandas as pd
import matplotlib.pyplot as plt

class DataProcess:

    """DataProcess :
    -envoie un appel get à l'api opendata de Lille
    -renvoie les données brut sous forme de dataframes
    -traite les données pour ne retourner que les communes avec plus de une occurrence
    -stocke les données en base
    -créé un graphique à barres pour la visualisation"""

    #fonction init
    def __init__(self):
        self = ""

    #fonction d'appel à l'api, renvoie les dataframes
    def dataQuery(self):
        baseUrl = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset="
        paramUrl = "&rows=120"
        # on définit une liste vide qui sera incrémentée à chaque nouvelle dataframe
        dataFrames = []
        # dictionnaire numéroté pour concaténer l'url avec les nom de services à analyser
        services = { 0: "bureaux-de-poste",
                     1: "localisation-hopitaux",
                     2: "postes-securite",
                     3: "cinemas-theatres-mel",
                     4: "adresse-et-geolocalisation-des-etablissements-denseignement-du-premier-et-second",
                     }
        # pour chaque service, la boucle créé l'url d'appel correspondant puis normalise le résultat du json et le classe dans une dataframe
        for i in range(5):
            urlApi = baseUrl + services[i] + paramUrl
            dataFrames.append(pd.DataFrame.from_dict(pd.io.json.json_normalize(json.loads(requests.get(urlApi).text)['records']), orient='columns'))
            print ("Querying for service " + str(i) )
        return dataFrames

    #Pour chaque service, on tâchera de répertorier dans un dictionnaire uniquement les villes contenant plus de 1 référence
    #La fonction prend en argument les dataFrames retournées par dataQuery() ainsi que l'index et le champ correspondant au service voulu
    def dataHandler(self, dataFrames, index, field):
        print ("Handling data " + str(index) + " with field : " + field)
        townCountValues = dataFrames[index][field].value_counts()
        townCountDict = {}
        for key, townCountValue in townCountValues.items():
            if townCountValue > 1:
                townCountDict.update({key:townCountValue})
        return townCountDict

    #on stocke les résultats obtenus en base mysql
    def dataInsert(self, townCountDict, db, table):
        conn = MySQLdb.connect(host= "localhost",
                               user="root",
                               passwd="root",
                               db=db)
        x = conn.cursor()

        for key, townCountValue in townCountDict.items():
            x.execute("""INSERT INTO postes(occurrence, commune) VALUES (%s, %s)""", (townCountValue, key))

        conn.commit()
        conn.close()

    #on visualise le nombre d'occurence d'un service donné avec un diagramme à barre
    # def dataViz(self, townCountDict):
    #     fig = plt.figure(figsize=(25,15))
    #     plt.bar(list(townCountDict.keys()), townCountDict.values(), color='g')
    #     plt.show()

#les appels
# dataQuery(self)
#dataHandler(dataQuery(), 0, 'fields.commune')
#dataViz(dataHandler(dataQuery(), 0, 'fields.commune'))
process = DataProcess()
#process.dataQuery()
townCountDict = process.dataHandler(process.dataQuery(), 0, 'fields.commune')
process.dataInsert(townCountDict, 'Pyviz', 'postes')
