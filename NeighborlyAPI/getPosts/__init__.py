import logging

import azure.functions as func
import pymongo
import json
from  bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:

        url = os.environ['MyDBConnection']
        client = pymongo.MongoClient(url)
        database = client['ghneighborlydb']
        collection = database['posts']
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset="utf-8")

    except ConnectionError:
        return func.HttpResponse("Unable to connect to mongodb", status_code=400)

    
