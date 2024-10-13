from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from fileUtils import leerFichero
import os 

load_dotenv()

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#la bbdd es diferente a cluster pero mismo nombre
#db = client.CalPal "si bbd ya existe, lo de abajo para crearla sino existe"
db = client["CalPal"]
#referencia a coleccion
alimentos_base_collection=db["alimentos_base"]

#metodo para borrar y resubir datos
def resubida_alimentos_base():
    fichero_alimentos_base="ficheros/alimentosBase.json"
    alimentos_base=leerFichero(fichero_alimentos_base)
     
    try:
        alimentos_base_collection.delete_many({}) #{} para especificar deleteAll
        alimentos_base_collection.insert_many(alimentos_base)
        
    except Exception as e:
        print(f"Error al subir los datos: {e}")